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

matrix = {'Al2O3': [0.0, 1.0], 'SiO2': [0.0, 1.0]}
tsp = AnnealingGlass(tg=1200/1452.0, budget=120, min_max_dic=matrix,
                     save_preds=False, save_states=False)

result = tsp.run()
result = result.get_result()

