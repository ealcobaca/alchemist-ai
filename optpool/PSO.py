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
#from .resultopt import ResultOpt
from optpool import ResultOpt
from optpool import Optimizer
import multiprocessing

#--- COST FUNCTION ------------------------------------------------------------+

# function we are attempting to optimize (minimize)
def func1(x, target, predFunc):
    total=0
    total = predFunc(x)
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
            self.velocity_i.append(random.uniform(-1,1))
            self.position_i.append(x0[i])

    # evaluate current fitness
    def evaluate(self,costFunc, target, predFunc):  
        self.err_i, self.fit_i=costFunc(self.position_i, target, predFunc)

        # check to see if the current position is an individual best
        if self.err_i < self.err_best_i or self.err_best_i==-1:
            self.pos_best_i=self.position_i
            self.err_best_i=self.err_i

    # update new particle velocity
    def update_velocity(self,pos_best_g):
        w=0.5       # constant inertia weight (how much to weigh the previous velocity)
        c1=1        # cognative constant
        c2=1        # social constant

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
            if self.position_i[i]>bounds[i][1]:
                self.position_i[i]=bounds[i][1]

            # adjust minimum position if neseccary
            if self.position_i[i] < bounds[i][0]:
                self.position_i[i]=bounds[i][0]
        
        summatory = sum(self.position_i)
        self.position_i = [self.position_i[i]/summatory for i in range(0,num_dimensions)]
                
class PSO(Optimizer):
    def __init__(self, sizeVector, sizeSample, target, n_cpu=None):
        Optimizer.__init__(self)
        global num_dimensions
        self.sizeVector = sizeVector
        self.sizeSample = sizeSample
        self.target = target
        
        if n_cpu is None:
            self.n_cpu = multiprocessing.cpu_count()
        else:
            self.n_cpu = n_cpu
        
    def run(self):
        global num_dimensions
        
        costFunc = func1
        m = 0
        M = 1
        bounds=[(m,M)]*self.sizeVector  # input bounds [(x1_min,x1_max),(x2_min,x2_max)...]
        x0 = [random.random() for l in range(self.sizeVector)]   # initial starting location [x1,x2...]
        summatory = sum(x0)
        x0 = [x0[i]/summatory for i in range(self.sizeVector)]
        num_particles=50
        maxiter=10
        epsilon = 0.0000001
        
        solutions = []
        valuesFunction = []
        errors = []
        for i in range(self.sizeSample):
            self.pos_best_g = 0
            num_dimensions=len(x0)
            err_best_g=-1                   # best error for group
            pos_best_g=[]                   # best position for group
            fit_best_g=-1
    
            # establish the swarm
            swarm=[]
            for ii in range(0,num_particles):
                swarm.append(Particle(x0))
    
            # begin optimization loop
            iteration=0
            stopCriterion = False
            while iteration < maxiter and not stopCriterion:
                # cycle through particles in swarm and evaluate fitness
                for j in range(0,num_particles):
                    swarm[j].evaluate(costFunc, self.target, self.predict)
    
                    # determine if current particle is the best (globally)
                    if swarm[j].err_i < err_best_g or err_best_g == -1:
                        self.pos_best_g=list(swarm[j].position_i)
                        err_best_g=float(swarm[j].err_i)
                        fit_best_g=float(swarm[j].fit_i)
                        if err_best_g < epsilon:
                          stopCriterion = True
    
                # cycle through swarm and update velocities and position
                for j in range(0,num_particles):
                    swarm[j].update_velocity(self.pos_best_g)
                    swarm[j].update_position(bounds)
                iteration+=1
            print(iteration)
    
            # print final results
            #print ('FINAL:')
            #print (pos_best_g)
            #print (err_best_g)
            solutions.append(self.pos_best_g)
            valuesFunction.append(fit_best_g)
            errors.append(err_best_g)
            
        result = ResultOpt(type_opt='PSO', result=[solutions, valuesFunction, errors])
        
        #return solucoes, valoresFuncao, erros
        return result
        
    def getBest(self):
        return self.pos_best_g

if __name__ == "__PSO__":
    main()
