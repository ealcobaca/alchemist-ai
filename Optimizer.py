# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 17:35:16 2018

@author: Bruno Pimentel
"""

from GP import GPClass

class OptimizerClass(object):
    def __init__(self):
        pass
    
    def soma(self,x,y):
        s = x+y
        print s
        return 
    
    def run_parallel(self,type_method, parameters, fit_function, size_final_population):
        retorno = 0
        if(type_method == 'GP'):
            gp = GPClass()
            retorno = gp.run_parallel(parameters, fit_function, size_final_population)
            print('GP:', retorno)
        elif(type_method == 'other'):
            retorno = 0
        return retorno
    

#opt = OptimizerClass()
#opt.run_parallel('GP',0,0,0)
