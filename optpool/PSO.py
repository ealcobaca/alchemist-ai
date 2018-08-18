"""
File.....: PSO.py
Author...: Bruno Pimentel
Email....: bappimentel@gmail.com
Github...: https://github.com/bapimentel
Description:
"""


#--- IMPORT DEPENDENCIES ------------------------------------------------------+

from __future__ import division
import random
import math
import numpy as np
from optpool import ResultOpt
from optpool import Optimizer
import multiprocessing
import time
import sys

#--- COST FUNCTION ------------------------------------------------------------+

# function we are attempting to optimize (minimize)
def func1(x, target, predFunc, keys):
    total=0
    x = Optimizer.vector_to_dic(x, keys)
    total = predFunc(x, target)
    error = abs(total-target)
    return error, total

#--- MAIN ---------------------------------------------------------------------+

class Particle:
    def __init__(self,x0):
        self.position_i=[]          # particle position
        self.velocity_i=[]          # particle velocity
        self.pos_best_i=[]          # best position individual
        self.err_best_i=-1          # best error individual
        self.err_i=-1               # error individual
        self.fit_i = -1

        for i in range(0,num_dimensions):
            self.velocity_i.append(random.uniform(-10,10))
            self.position_i.append(x0[i])

    # evaluate current fitness
    def evaluate(self,costFunc, target, predFunc, keys):  
        self.err_i, self.fit_i=costFunc(self.position_i, target, predFunc, keys)

        # check to see if the current position is an individual best
        if self.err_i < self.err_best_i or self.err_best_i==-1:
            self.pos_best_i=self.position_i
            self.err_best_i=self.err_i

    # update new particle velocity
    def update_velocity(self, pos_best_g):
        w=20       # constant inertia weight (how much to weigh the previous velocity)
        c1=50        # cognative constant
        c2=20        # social constant

        for i in range(0,num_dimensions):
            r1=random.random()
            r2=random.random()

            vel_cognitive=c1*r1*(self.pos_best_i[i]-self.position_i[i])
            vel_social=c2*r2*(pos_best_g[i]-self.position_i[i])
            self.velocity_i[i]=w*self.velocity_i[i]+vel_cognitive+vel_social

    # update the particle position based off new velocity updates
    def update_position(self,bounds):
        for i in range(0,num_dimensions):
            self.position_i[i]=self.position_i[i]+self.velocity_i[i]
            # adjust maximum position if necessary
            if self.position_i[i] < bounds[i][0]:
                self.position_i[i]=bounds[i][0]

            # adjust minimum position if neseccary
            if self.position_i[i] > bounds[i][1]:
                self.position_i[i]=bounds[i][1]
        summatory = sum(self.position_i)
        '''
        is_ok = False
        while not is_ok:
            coef = random.uniform(0.10001, 1.0)
            self.position_i[44] = summatory*coef#*0.101
            summatory = sum(self.position_i)
            if float(self.position_i[44])/float(summatory) > 0.1:
                is_ok = True
        '''
        summatory += 0.00000001
        self.position_i = [self.position_i[i]/summatory for i in range(0,num_dimensions)]
                
class PSO(Optimizer):
    def __init__(self, sizeVector, target, max_min_comp, n_cpu=None, path=None, clf_rf=None, limiar_rf=None, budget=None, error=0.01):
        if path is None:
            Optimizer.__init__(self, tg=target, min_max_dic=max_min_comp, clf_rf=clf_rf, limiar_rf=limiar_rf)
        else:
            Optimizer.__init__(self,
                               tg=target, min_max_dic=max_min_comp, path=path, clf_rf=clf_rf, limiar_rf=limiar_rf)

        global num_dimensions
        self.sizeVector = sizeVector
        self.target = target
        self.max_min_comp = max_min_comp
        self.limiar_rf = limiar_rf
        self.budget = budget

        if(type(self.max_min_comp)==dict):
            mMs = []
            for k in self.max_min_comp:
                a = self.max_min_comp[k][0]
                b = self.max_min_comp[k][1]
                mM = [a,b]
                mMs.append(mM)
            self.keys = self.max_min_comp.keys()
            self.max_min_comp = mMs

        #print(self.max_min_comp)

        # if not isinstance(initialVectors[0], list):
            # self.initialVectors = [initialVectors]
        # self.sizeSample = len(self.initialVectors)
        self.sizeSample = 1
        
        if n_cpu is None:
            self.n_cpu = multiprocessing.cpu_count()
        else:
            self.n_cpu = n_cpu

        if budget == None:
            self.budget=sys.maxsize
        
    def run(self):
        global num_dimensions
        
        costFunc = func1
        m = 0
        M = 1
        bounds=[(m,M)]*self.sizeVector  # input bounds [(x1_min,x1_max),(x2_min,x2_max)...]
        #x0 = [random.random() for l in range(self.sizeVector)]   # initial starting location [x1,x2...]
        #summatory = sum(x0)
        #x0 = [x0[i]/summatory for i in range(self.sizeVector)]
        num_particles=50000 #100
        maxiter=50000 #100
        epsilon = 0.01  
        max_time = 15.0      
        #print(self.target)
        solutions = []
        valuesFunction = []
        errors = []
        t0 = time.clock()
        for i in range(self.sizeSample):
            self.pos_best_g = 0
            # x0 = self.initialVectors[i]
            # summatory = sum(x0)
            # x0 = [x0[i]/summatory for i in range(self.sizeVector)]
            num_dimensions=len(self.max_min_comp)
            err_best_g=-1                   # best error for group
            pos_best_g=[]                   # best position for group
            fit_best_g=-1
    
            # establish the swarm
            swarm=[]
            for ii in range(0,num_particles):
                x0 = [np.random.uniform(i[0], i[1], 1)[0]
                      for i in self.max_min_comp]
                swarm.append(Particle(x0))
    
            # begin optimization loop
            iteration=0
            stopCriterion = False
            is_ok = False
            max_iter_equal = maxiter/5# maxiter/5
            count_iter_equal = 0
            err_best_g_before = err_best_g
            while iteration < maxiter and not stopCriterion:
                # cycle through particles in swarm and evaluate fitness
                for j in range(0,num_particles):
                    swarm[j].evaluate(costFunc, self.target, self.predict, self.keys)

                    err_best_g_before = err_best_g
    
                    # determine if current particle is the best (globally)
                    if swarm[j].err_i < err_best_g or err_best_g == -1:
                        self.pos_best_g=list(swarm[j].position_i)                        
                        err_best_g=float(swarm[j].err_i)
                        fit_best_g=float(swarm[j].fit_i)
                        #print(err_best_g)
                    if err_best_g/self.target < epsilon:
                      #print(err_best_g/self.target)
                      stopCriterion = True
                      is_ok = True
                      break
                    if err_best_g == err_best_g_before:
                        count_iter_equal = count_iter_equal + 1
                        # print(err_best_g_before, count_iter_equal)
                    else:
                        count_iter_equal = 0
                    if count_iter_equal == max_iter_equal:
                        stopCriterion = True
                        is_ok = True
                        break
                    t1 = time.clock()
                    delta_t = t1-t0
                    #print(delta_t)
                    #print(self.budget)
                    if delta_t >= self.budget:
                        #print(delta_t)
                        stopCriterion = True
                        is_ok = True
                        break
                #print(err_best_g, iteration)
    
                # cycle through swarm and update velocities and position
                for j in range(0,num_particles):
                    #is_ok = False
                    while not is_ok:
                        swarm[j].update_velocity(self.pos_best_g)
                        #swarm[j].update_position(bounds)
                        swarm[j].update_position(self.max_min_comp)
                        is_ok = True#self.check_restriction(swarm[j], self.max_min_comp)
                    
                iteration+=1
            #print(iteration)
    
            self.pos_best_g = self.vector_to_dic(self.pos_best_g, self.keys)
            #self.pos_best_g = self.compounddic2atomsfraction(
            #    self.pos_best_g)
            self.pos_best_g = self.dic_to_vector_compound(self.pos_best_g)
            solutions.append(self.pos_best_g)
            valuesFunction.append(fit_best_g)
            errors.append(err_best_g)
            
        # print(errors)
        result = ResultOpt(type_opt='PSO', result=[solutions, valuesFunction, errors])
        # result = ResultOpt(type_opt='PSO', result=[valuesFunction, solution, errors])
        
        #return solucoes, valoresFuncao, erros
        return result
        
    def check_restriction(self, particle, max_min_comp):
        is_ok = True
        i = 0
        while is_ok and i < num_dimensions:
            max_i = max_min_comp[i][0]
            min_i = max_min_comp[i][1]
            value_i = particle.position_i[i]
            is_ok = is_ok and (min_i <= value_i) and (value_i <= max_i)
            i = i + 1
        return is_ok
