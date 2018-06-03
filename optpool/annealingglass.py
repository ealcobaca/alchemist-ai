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


class AnnealingGlass(Annealer, Optimizer):
    """ TODO  """
    model_input_length = 45

    def __init__(self, tg, restriction, steps=50000,
                 save_states=False, save_preds=False, path=None):

        self.idx_elem = []  # pick up non-zero indices
        self.state = [0] * self.model_input_length
        self.restriction = restriction
        for i in range(self.model_input_length):
            if (self.restriction[i][0] >= 0) and (self.restriction[i][1] >= 0) and (self.restriction[i][1] > self.restriction[i][0]):
                self.idx_elem.append(i)
        self.random()

        Annealer.__init__(self, initial_state=self.state)  # important!
        if path is None:
            Optimizer.__init__(self)
        else:
            Optimizer.__init__(self, path=path)

        self.tg = tg
        self.copy_trategy = "slice"
        self.steps = steps

        self.save_states = save_states
        self.save_preds = save_preds
        self.all_states = []
        self.all_preds = []
        if self.save_states:
            self.all_states.append(self.state.copy())

    def minmax(self, value, i):
        """ DOCS """
        if self.restriction[i][0] <= value and value <= self.restriction[i][1]:
            return True
        return False

    def is_possible(self, value, i):
        """ DOCS """
        if self.restriction[i][0] <= value and value <= self.restriction[i][1]:
            return True
        return False

    @staticmethod
    def rand(min_value, max_value):
        """ DOCS """
        return ((max_value - min_value) * np.random.rand()) + min_value

    def random(self):
        """ DOCS """
        done = False
        while done is False:
            perc = 1

            idxs = np.random.choice(self.idx_elem, len(self.idx_elem),
                                    replace=False).tolist()
            for idx in idxs:
                if perc > self.min_(idx):
                    if perc > self.restriction[idx][1]:
                        new_value = self.rand(
                            self.restriction[idx][0], self.restriction[idx][1])
                    else:
                        new_value = self.rand(
                            perc, self.restriction[idx][0])
                    perc = perc - new_value
                else:
                    new_value = 0
                self.state[idx] = new_value

            idxs = np.random.choice(self.idx_elem, len(self.idx_elem),
                                    replace=False).tolist()
            for idx in idxs:
                if self.minmax(perc + self.state[idx], idx):
                    new_value = perc + self.state[idx]
                    self.state[idx] = new_value
                    perc = perc - perc
                    done = True
                    break

    def min_(self, i):
        """ DOCS """
        return self.restriction[i][0]

    def max_(self, i):
        """ DOCS """
        return self.restriction[i][1]

    def move(self):
        """ DOCS """
        self.random()
        if self.save_states:
            self.all_states.append(self.state.copy())
        # sum_state = sum(self.state)
        # if abs(1 - sum_state) > 0.0000001:
        #     print("Erro - soma diferente de 1")
        #     print(sum_state)
        # for i in self.idx_elem.copy():
        #     if self.minmax(self.state[i], i) is False:
        #         print("Erro - fora do intervalo")

    def energy(self):
        """Calculates the length of the route."""
        pred = self.predict(self.state)
        if self.save_preds:
            self.all_preds.append(pred)
        if pred < 0:
            pred = 100
        return np.abs(pred - self.tg)

    def run(self):
        """ DOCS """
        state, energy = self.anneal()
        pred = self.predict(state)[0]

        result = ResultOpt(
            type_opt='annealing',
            result=[pred, energy, state, self.all_preds, self.all_states])

        return result
