

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


import os
import errno

filename = "experiments/testing_pso_ann_rand/asdasd/asd/asd/ola"

def save_result(filename, data):
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    with open(filename, "w") as f:
        f.write("FOOBAR")
#      save de data .csv 



save_result(filename, None)

from multiprocessing import Pool, TimeoutError
from optpool import RandomGlass
from optpool import OptPool
import numpy as np
import time
import os

def apply_opt(i):

    matrix = {'Al2O3': [0.0, 1.0],
              'BaO': [0.0, 1.0],
              'Ag2O': [0.0, 1.0],
              'As2O3': [0.0, 1.0],
              'SiO2': [0.0, 1.0]}
    tsp = RandomGlass(tg=1200/1452.0, maxit=50000, min_max_dic=matrix)

    result = tsp.run()
    result = result.get_result()
    return result[0]

# start 4 worker processes
with Pool(processes=4) as pool:

    # launching multiple evaluations asynchronously *may* use more processes
    multiple_results = [pool.apply_async(apply_opt, (i,)) for i in range(10)]
    print([res.get() for res in multiple_results])

