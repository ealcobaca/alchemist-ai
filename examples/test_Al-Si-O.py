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

restriction = [[0.0, 0.0], [0.0, 1.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0],
        [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0],
        [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0],
        [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0],
        [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0],
        [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0],
        [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0],
        [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0],
        [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0],
        [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0],
        [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0],
        [0.0, 1.0], [0.0, 1.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0],
        [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0],
        [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0],
        [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0],
        [0.0, 0.0], [0.0, 0.0]]

matrix = {'Al2O3': [0.0, 1.0], 'SiO': [0.0, 1.0], 'SiO2': [0.0, 1.0]}
matrix = {'Al2O3': [0.0, 1.0], 'SiO': [0.0, 1.0]}
tsp = AnnealingGlass(tg=0.6887, min_max_dic=matrix, save_preds=True, save_states=True)

result = tsp.run()
result = result.get_result()

Y = np.array([i['SiO'] for i in result[4]])
X = np.array([i['Al2O3'] for i in result[4]])
C = np.array([i[0] for i in result[3]])

fig, axs = plt.subplots(2, 2)

#axs[0, 0].imshow(np.random.random((100, 100)))
axs[0, 1].imshow(np.random.random((100, 100)))
axs[1, 1].imshow(np.random.random((100, 100)))


axs[0,0].set_title('Al2O3_SiO_O', fontsize=20)
axs[0,0].set_xlabel('Al2O3')
axs[0,0].set_ylabel('SiO')

im1 = axs[0,0].scatter(X,Y, c=C, cmap='viridis_r')
fig.colorbar(im1, ax=axs[0,0])

values = [compounddic2atomsfraction(i) for i in result[4]]
YY = np.array([i['Si'] for i in values])
XX = np.array([i['Al'] for i in values])
im1 = axs[1,0].scatter(XX,YY, c=C, cmap='viridis_r')
fig.colorbar(im1, ax=axs[1,0])

plt.show()

# if __name__ == "__main__":
#    main()


