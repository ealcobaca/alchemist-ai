#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File.....: optimizer.py
Author...: Edesio Alcobaça
Email....: e.alcobaca@gmail.com
Github...: https://github.com/ealcobaca
Description:
"""

import multiprocessing
import numpy as np
from .optimizer import Optimizer
from .resultopt import ResultOpt
import sys
import time


class RandomGlass(Optimizer):
    """ TODO  """

    def __init__(self, tg, min_max_dic, error=0.01, maxit=50000,
                 budget=None, seed=None, path=None):

        if path is None:
            Optimizer.__init__(self, tg=tg, min_max_dic=min_max_dic, seed=seed)
        else:
            Optimizer.__init__(self, tg=tg, min_max_dic=min_max_dic, seed=seed,
                               path=path)

        Optimizer.__init__(self, path=path, seed=seed)
        self.error = error
        self.maxit = maxit
        self.budget = budget

        if budget != None:
            self.t1 = time.clock()
            self.maxit=sys.maxsize

    def random(self):
        state = {}
        for key in self.min_max_dic.keys():
            state[key] = np.random.uniform(
                self.min_max_dic[key][0],
                self.min_max_dic[key][1])
        return state


    def run(self):
        """ DOCS """
        pred = self.predict(self.best)[0]
        best = None
        best_pred = sys.maxit
        end = 1
        count = 0

        while end == 1:
            state = self.random()
            pred = self.predict(state, self.tg)

            if pred > self.tg - self.erro and pred < self.tg + self.erro:
                 best = state
                 best_pred = state
                 end=0
            elif np.abs(pred - self.tg) < np.abs(best_pred - self.tg):
                 best_pred = pred
                 best = state

            if self.budget != None:
                t2 = time.clock()
                if t2-t1 >= self.budget:
                    end=0
            else:
                count +=1
                if count == self.maxit:
                    end=0


        result = ResultOpt(
            type_opt='random',
            result=[pred, self.best, self.all_preds, self.all_states])

        return result
