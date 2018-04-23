# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 20:44:16 2018

@author: Bruno
"""

from Optimizer import OptimizerClass

class Opt_pool(object):
    def __init__(self):
        pass
    
    def main_loop(self):
        opt = OptimizerClass()
        metodos = ['GP']
        for mtd in metodos:
            opt.run_parallel(mtd,0,0,0)
        return 0
    
opt_pool = Opt_pool()
opt_pool.main_loop()
            
        