
########## experiment idea ##########
#####################################
#
#For each opt{PSO, Annealing, random}:
#    For each comp{C1+C2, C1+C2+C3, …, C1+C2+...+C15}:
#        For each maxit{0.5, 1, 5, 10}:
#            find a composition → opt(TG, comp, maxit, repetitions, error)
# result/
# result/pso
# result/ann
# result/ran
# result/pso/01+c1
# result/pso/02+c2
# ...
# result/pso/10+c10
# result/pso/01+c1/time30
# result/pso/01+c1/time60
# ...
# result/pso/01+c1/time600
# result/pso/01+c1/time-30/pso-01+c1-time30-30.csv


from multiprocessing import Pool, TimeoutError
from optpool import RandomGlass
from optpool import AnnealingGlass
from optpool import OptPool
from optpool import Optimizer
import pandas as pd
import numpy as np
import time
import os
import errno


def save_result(filename, data):
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    with open(filename, "w") as f:
        data.to_csv(filename, index=False)


def ger_all_comb(comp):
    count = 0
    l = [[] for i in range(len(comp))]
    for i in comp.keys():
        for j in range(count,len(comp)):
            l[j].append({i:comp[i]})
        count +=1
    return l


def apply_opt(alg, time, comp, itera, tg):

    if alg == 'ann':
        tsp = AnnealingGlass(tg=tg, budget=time, min_max_dic=comp)
    elif alg == 'ran':
        tsp = RandomGlass(tg=tg, budget=time, min_max_dic=comp)
    elif alg == 'pso':
        tsp = RandomGlass(tg=tg, budget=time, min_max_dic=comp)

    result = tsp.run()
    result = result.get_result()

    filename = alg+'-tg'+str(tg)+'-c'+str(len(comp))+'-time'+str(time)+'-'+str(itera)+'.csv'
    path_name = 'experiments/testing_pso_ann_rand/result/'+alg+'/tg'+str(tg)+'/c'+str(len(comp))+'/time'+str(time)+'/'+filename

    comp_vector = Optimizer.dic_to_vector_compound(result[1])
    comp_vector = [comp_vector + [result[0]]]
    columns = Optimizer.AVAILABLECOMPOUNDS+['TG']
    data = pd.DataFrame(comp_vector, columns=columns)
    save_result(path_name, data)

    return 0

def main():

    alg = ['ann', 'ran']
    times = [30, 60]
    # times = [30, 60, 300, 600]
    comp = {'SiO2': [0.0, 1.0],
            'Al2O3': [0.0, 1.0],
            'BaO': [0.0, 1.0],
            'Ag2O': [0.0, 1.0],
            'As2O3': [0.0, 1.0]}
    tgs = [1100]
    reps = range(1,31)

    # start 4 worker processes
    with Pool(processes=4) as pool:

        multiple_results = []
        # launching multiple evaluations asynchronously *may* use more processes
        for algorithm in alg:
            for tg in tgs:
                for compound in ger_all_comb(comp):
                    for time in times:
                        for repetitions in reps:
                            multiple_results.append(
                                pool.apply_async(apply_opt,(
                                    algorithm, time, compound[0], repetitions, tg)))
        print([res.get() for res in multiple_results])


