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
import numpy as np

TSP = AnnealingGlass(state=np.random.rand(45).tolist(),
                     qtd_distutb=20, tg=0.85, perc_disturb=1)
TSP.copy_trategy = "slice"
STATE, E = TSP.anneal()
PRED = TSP.predict(STATE)
