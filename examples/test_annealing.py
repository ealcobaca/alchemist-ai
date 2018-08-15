#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: test_annealing_glass.py
Author: E. Alcobaça
Email: e.alcobaca@gmail.com
Github: https://github.com/ealcobaca
Description: A simples test to the AnnealingGlass class
"""
from optpool import AnnealingGlass
from optpool import OptPool
import numpy as np
import matplotlib.pyplot as plt
import re

# np.random.seed(123)
# with restriction

def compounddic2atomsfraction(compounds):

    def createNewDic(dic, multiplyby):
        values = list(dic.values())
        keys = dic.keys()
        newValues = np.array(values)*multiplyby
        newDic = dict(zip(keys, newValues))
        return newDic

    def composition2atoms(cstr):
        lst = re.findall(r'([A-Z][a-z]?)(\d*\.?\d*)', cstr)
        dic = {}
        for i in lst:
            if len(i[1]) > 0:
                try:
                    dic[i[0]] = int(i[1])
                except ValueError:
                    dic[i[0]] = float(i[1])
            else:
                dic[i[0]] = 1
        return dic

    dic = {}

    for key in compounds.keys():
        baseValue = compounds[key]
        atoms = composition2atoms(key)
        for a in atoms.keys():
            dic[a] = dic.get(a, 0) + atoms[a]*baseValue

    multiplyby = 1/np.sum(list(dic.values()))
    atomsF = createNewDic(dic, multiplyby)

    return atomsF

matrix = {'Al2O3': [0.0, 1.0], 'SiO2': [0.0, 1.0]}
tsp = RandomGlass(tg=1200/1452.0, budget=120, min_max_dic=matrix)

result = tsp.run()
result = result.get_result()

