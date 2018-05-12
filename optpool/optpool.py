#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File.....: optimizer.py
Author...: Bruno Pimentel, Edesio Alcobaça
Email....: bappimentel@gmail.com, e.alcobaca@gmail.com
Github...: https://github.com/bapimentel, https://github.com/ealcobaca
Description:
"""

import multiprocessing as mp


class OptPool(object):
    """ TODO """

    def __init__(self, optmizers):
        self.optmizers = optmizers

    def run(self, n_processes=1):
        """TODO: Docstring for run.
        :returns: TODO

        """
        results = []
        for opt in self.optmizers:
            results.append(opt.run())
        return results
