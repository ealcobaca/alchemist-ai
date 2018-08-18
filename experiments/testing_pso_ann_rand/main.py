
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
from optpool import PSO
from optpool import OptPool
from optpool import Optimizer
import pandas as pd
import numpy as np
import time
import os
import errno
import gc

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
    l = [{} for i in range(len(comp))]
    for i in comp.keys():
        for j in range(count,len(comp)):
            l[j][i] = comp[i]
        count +=1
    return l


def apply_opt(alg, time, comp, itera, tg, error):

    if alg == 'ann':
        tsp = AnnealingGlass(tg=tg, budget=time, min_max_dic=comp, error=error)
    elif alg == 'ran':
        tsp = RandomGlass(tg=tg, budget=time, min_max_dic=comp, error=error)
    elif alg == 'pso':
        tsp = PSO(sizeVector=1, target=tg, budget=time, max_min_comp=comp, error=error)

    result = tsp.run()
    result = result.get_result()

    filename = alg+'-tg'+str(round(tg,2))+'-c'+str(len(comp))+'-time'+str(time)+'-'+str(itera)+'.csv'
    path_name = 'experiments/testing_pso_ann_rand/result/'+alg+'/tg'+str(round(tg,2))+'/c'+str(len(comp))+'/time'+str(time)+'/'+filename

    if alg == 'pso':
        comp_vector = result[0][0]
        comp_vector = [comp_vector + [result[1]]]
    else:
        comp_vector = Optimizer.dic_to_vector_compound(result[1])
        comp_vector = [comp_vector + [result[0]]]

    columns = Optimizer.AVAILABLECOMPOUNDS+['TG']
    data = pd.DataFrame(comp_vector, columns=columns)
    save_result(path_name, data)

    tsp = result = filename = path_name = comp_vector = columns = data = None
    gc.collect()

    return 0

def main():

    alg = ['ann', 'ran', 'pso']
    times = [30, 60, 300, 600]
    # times = [30]
    comp = {'SiO2': [0.0, 1.0],
            'B2O3': [0.0, 1.0],
            'Na2O': [0.0, 1.0],
            'Al2O3': [0.0, 1.0],
            'P2O5': [0.0, 1.0],
            'Li2O': [0.0, 1.0],
            'ZnO': [0.0, 1.0],
            'CaO': [0.0, 1.0],
            'K2O': [0.0, 1.0],
            'BaO': [0.0, 1.0],
            'MgO': [0.0, 1.0]}
    tgs = [1100/1452.0, 750/1452.0, 900/1452.0, 400/1452.0]
    # tgs = [1100/1452.0]
    reps = range(1,31)
    error=0.01

    # start 4 worker processes
    with Pool(processes=None) as pool:

        print("Start")
        all_comb_comp = ger_all_comb(comp)
        del all_comb_comp[0]
        multiple_results = []
        # launching multiple evaluations asynchronously *may* use more processes
        for algorithm in alg:
            for tg in tgs:
                for compound in all_comb_comp:
                    for time in times:
                        for repetitions in reps:
                            multiple_results.append(
                                pool.apply_async(apply_opt,(
                                    algorithm, time, compound, repetitions, tg, error)))
        print([res.get() for res in multiple_results])
        print("END")


if __name__ == "__main__":
    main()
