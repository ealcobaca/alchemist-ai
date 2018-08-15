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
from simanneal import Annealer
from .optimizer import Optimizer
from .resultopt import ResultOpt
import sys
import time


class AnnealingGlass(Annealer, Optimizer):
    """ TODO  """
    model_input_length = 45

    def __init__(self, tg, min_max_dic, seed=None, maxit=50000, error=0.01,
                 budget=None, save_states=False, save_preds=False, path=None):

        if path is None:
            Optimizer.__init__(self, tg=tg, min_max_dic=min_max_dic, seed=seed)
        else:
            Optimizer.__init__(self, tg=tg, min_max_dic=min_max_dic, seed=seed,
                               path=path)
        self.random()
        Annealer.__init__(self, initial_state=self.state)  # important!

        self.copy_trategy = "slice"
        self.steps = maxit
        self.budget = budget
        self.error = error
        if budget != None:
            self.t1 = time.clock()
            maxit=sys.maxsize

        self.save_states = save_states
        self.save_preds = save_preds
        self.all_states = []
        self.all_preds = []

        self.ranges = {key: (min_max_dic[key][1] - min_max_dic[key][0])
                       for key in min_max_dic}

    @staticmethod
    def rand(min_value, max_value):
        """ DOCS """
        return ((max_value - min_value) * np.random.rand()) + min_value

    def random(self):
        self.state = {}
        for key in self.min_max_dic.keys():
            self.state[key] = np.random.uniform(
                self.min_max_dic[key][0],
                self.min_max_dic[key][1])
        return self.state

    def move(self):
        """ DOCS """
        # self.random()
        aux = self.state.copy()
        flag = True
        while(flag == True):
            self.state = aux.copy()
            for key in self.state:
                max_perc = 0.1 * self.ranges[key]
                delta = np.random.uniform(-max_perc, max_perc, 1)[0]
                new = self.state[key] + delta
                if new < self.min_max_dic[key][0]:
                    new = self.min_max_dic[key][0]
                elif new > self.min_max_dic[key][1]:
                    new = self.min_max_dic[key][1]
                self.state[key] = new
            aux2 = [self.state[i] for i in self.state]
            flag=False
            if np.sum(aux2) == 0:
                flag = True


    def energy(self):
        """Calculates the length of the route."""
        pred = self.predict(self.state, self.tg)
        if np.isnan(pred):
            print("NAN")
            print(pred)
            print(self.state)
        if self.save_preds:
            self.all_preds.append(pred)
        if self.save_states:
            self.all_states.append(self.state.copy())
        if self.budget != None:
            t2 = time.clock()
            if t2-self.t1 > self.budget:
                self.set_user_exit(None, None)
        if pred > self.tg - self.error and pred < self.tg + self.error:
                self.set_user_exit(None, None)

        if pred < 0:
            pred = 100

        return np.abs(pred - self.tg)

    def run(self):
        """ DOCS """
        state, energy = self.anneal()
        pred = self.predict(state, self.tg)[0]
        #state = self.compounddic2atomsfraction(state)

        result = ResultOpt(
            type_opt='annealing',
            result=[pred, energy, state, self.all_preds, self.all_states])

        return result
