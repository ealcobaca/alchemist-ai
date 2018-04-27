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
        pool = mp.Pool(processes=n_processes)
        # launching multiple evaluations asynchronously
        results = []
        for opt in self.optmizers:
            results.append(pool.apply_async(opt.run, (opt,)))
        final = [result.get() for result in results]
        pool.close()
        pool.join()

        return final


class ResultOpt(object):
    """ TODO """

    def __init__(self, type_opt, result):
        self.type_opt = type_opt
        self.result = result

    def get_result(self):
        """TODO: Docstring for getResult.
        :returns: TODO

        """
        return self.result

    def get_type(self):
        """TODO: Docstring for getType.

        :returns: TODO

        """
        return self.type_opt
