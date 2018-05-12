#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File.....: optimizer.py
Author...: Edesio Alcobaça
Email....: e.alcobaca@gmail.com
Github...: https://github.com/ealcobaca
Description:
"""

import numpy as np
from simanneal import Annealer
from .optimizer import Optimizer
from .resultopt import ResultOpt
import multiprocessing
import copy
from multiprocessing import Process


class AnnealingGlass(Annealer, Optimizer, Process):
    """ TODO  """
    model_input_length = 45

    def __init__(self, state, tg, qtd_distutb=1,
                 perc_disturb=0.01, n_cpu=None):
        Annealer.__init__(self, initial_state=state)  # important!
        Optimizer.__init__(self)
        Process.__init__(self)

        self.tg = tg
        self.qtd_distutb = qtd_distutb
        self.perc_disturb = perc_disturb
        self.copy_trategy = "slice"
        self.states = state

        if isinstance(self.states[0], list):
            self.state = self.states[0]
            self.pop = len(self.states)
        else:
            self.pop = 1

        if n_cpu is None:
            self.n_cpu = multiprocessing.cpu_count()
        else:
            self.n_cpu = n_cpu

    def move(self):
        """Swaps two cities in the route."""

        values = (np.random.rand(self.qtd_distutb)*2 - 1)*self.perc_disturb

        ind = np.random.randint(self.model_input_length-1,
                                size=self.qtd_distutb)
        size = len(values)
        for i in range(size):
            if self.state[ind[i]] + values[i] >= 0:
                self.state[ind[i]] += values[i]
        self.state /= np.sum(self.state)

    def energy(self):
        """Calculates the length of the route."""
        pred = self.predict(self.state)
        return np.abs(pred - self.tg)

    def run(self):
        preds = []
        energys = []
        states = []
        i = 0

        while i < self.pop:
            if self.pop == 1:
                self.state = self.states
            else:
                self.state = self.states[i]

            state, energy = self.anneal()
            pred = self.predict(state)
            i += 1

            preds.append(pred[0])
            energys.append(energy[0])
            states.append(state.tolist())

        result = ResultOpt(type_opt='annealing',
                           result=[preds, energys, states])
        return result

    def clone(self):
        """TODO: Docstring for __cmp__.

        :returns: TODO
        """
        obj = AnnealingGlass(self.state, self.tg, self.qtd_distutb,
                             self.perc_disturb, self.pop, self.n_cpu)
        return obj
