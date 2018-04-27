#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File.....: optimizer.py
Author...: Bruno Pimentel, Edesio Alcobaça
Email....: bappimentel@gmail.com, e.alcobaca@gmail.com
Github...: https://github.com/bapimentel, https://github.com/ealcobaca
Description:
"""

import numpy as np
from simanneal import Annealer
from .optimizer import Optimizer


class AnnealingGlass(Annealer, Optimizer):
    """ TODO  """
    model_input_length = 45

    def __init__(self, state, tg, qtd_distutb=1, perc_disturb=0.01):
        Annealer.__init__(self, initial_state=state)  # important!
        Optimizer.__init__(self)  # important!
        self.tg = tg
        self.qtd_distutb = qtd_distutb
        self.perc_disturb = perc_disturb

    def move(self):
        """Swaps two cities in the route."""

        values = (np.random.rand(self.qtd_distutb)*2 - 1)*self.perc_disturb
        values /= np.sum(values)

        ind = np.random.randint(self.model_input_length-1,
                                size=self.qtd_distutb)
        size = len(values)
        for i in range(size):
            if self.state[ind[i]] + values[i] >= 0:
                self.state[ind[i]] += values[i]

    def energy(self):
        """Calculates the length of the route."""
        pred = self.predict(self.state)
        return np.abs(pred - self.tg)

    def run(self):
        """ TODO """
        pass
