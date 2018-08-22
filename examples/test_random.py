#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: test_annealing_glass.py
Author: E. Alcobaça
Email: e.alcobaca@gmail.com
Github: https://github.com/ealcobaca
Description: A simples test to the AnnealingGlass class
"""
from optpool import RandomGlass
from optpool import OptPool
import numpy as np

matrix = {'Al2O3': [0.0, 1.0],
          'Ag2O': [0.0, 1.0],
          'As2O3': [0.0, 1.0],
          'B2O3': [0.0, 1.0],
          'BaO': [0.0, 1.0],
          'CaO': [0.0, 1.0]}
matrix = {'SiO2': [0.0, 1.0],
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
tsp = RandomGlass(tg=1100/1452.0, budget=6000, min_max_dic=matrix)

result = tsp.run()
result = result.get_result()
print(result[0])
print(result[1])
