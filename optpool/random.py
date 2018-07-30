#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: random.py
Author: E. Alcobaça
Email: e.alcobaca@gmail.com
Github: https://github.com/ealcobaca
Description: 
"""

from .optimizer import Optimizer
from .resultopt import ResultOpt
import numpy as np


class RandomOpt(Optimizer):

    """Docstring for RandomOpt. """

    def __init__(self, tg, min_max_dic, error=0.01, n_iters=5000,
                 path=None, seed=None):
        """TODO: to be defined1. """
        # Optimizer(tg, min_max_dic).__init__(self)

        if path is None:
            Optimizer.__init__(self, tg=tg, min_max_dic=min_max_dic, seed=seed)
        else:
            Optimizer.__init__(self, tg=tg, min_max_dic=min_max_dic, seed=seed,
                               path=path)
        self.error = error
        self.n_iters = n_iters
        self. solution = None

    def random(self):
        self.solution = {}
        for key in self.min_max_dic.keys():
            self.solution[key] = np.random.uniform(
                self.min_max_dic[key][0],
                self.min_max_dic[key][1])
        return self.solution

    def run(self):

        error = self.error + 1
        best_solution = self.solution
        best_error = 1000000
        while self.n_iters > 0 and best_error > self.error:
            # print(self.solution)
            self.n_iters -= 1
            self.random()
            pred = self.predict(self.solution)[0]
            if pred < 0:
                pred = 100
            error = np.abs(pred - self.tg)

            if error < best_error:
                best_error = error
                best_solution = self.solution
                print(best_error)

        best_solution = self.compounddic2atomsfraction(best_solution)
        print(best_solution)
        pred = self.predict(best_solution)[0]
        result = ResultOpt(
            type_opt='randomopt',
            result=[pred, best_error, best_solution.copy()])
        return result
