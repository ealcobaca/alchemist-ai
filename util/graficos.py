# -*- coding: utf-8 -*-
"""
Created on Tue May 29 14:23:00 2018

@author: Bruno Pimentel
"""

import csv
import numpy as np
import matplotlib.pyplot as plt

def read_file(file_name):
        reader = csv.reader(open(file_name, "r"), delimiter="\t")
        x = list(reader)
        result = np.array(x)
        return result
    
def var(matriz):
    m = []
    n = len(matriz)
    p = len(matriz[0])
    for i in range(p):
#        mm = -1.0
        mm = np.std([float(matriz[j][i]) for j in range(n)])
        m.append(mm)
    return m
    
def maximo(matriz):
    m = []
    index = []
    n = len(matriz)
    p = len(matriz[0])
    for i in range(p):
#        mm = -1.0
        mm, ind = maximo_lista([matriz[j][i] for j in range(n)])
#        for j in range(n):
#            if float(matriz[j][i]) > mm:
#                mm = matriz[j][i]
        m.append(mm)
        index.append(ind)
    return m

def maximo_lista(lista):
    n = len(lista)
    mm = -1.0
    index = -1
    for j in range(n):
        if float(lista[j]) > mm:
            mm = float(lista[j])
            index = j
    return mm, index

def gerarParalelas(file_names):
    dados = []
    for file_name in file_names:
        dados.append(read_file(file_name))
        
    #print maximo(dados[0])
    
    #print maximo(dados[1])
    
    
    t = range(len(dados[0][0]))
    fig = plt.figure()
    ax = plt.subplot(111)
    ms = 0.5
    lw = 0.2
    print len(dados[0])
    for i in range(len(dados[0])):
        #print dados[0][i]
        line, = ax.plot(t, dados[0][i], label='Real', linestyle='--', linewidth=lw, marker='.', color='k', markersize=ms)
    for i in range(100):#len(dados[1])):
        print i
        line, = ax.plot(t, dados[1][i], label='PSO', linestyle='--', linewidth=lw, marker='.', color='g', markersize=ms)
  
    #line, = ax.plot(t, media_desempenho_final[1], label='Proposed2', linestyle='--', linewidth=1.5, marker='s', color='b')
    #box = ax.get_position()
    #ax.set_position([box.x0, box.y0 + box.height * 0.1,box.width, box.height * 0.9])
    #legend = ax.legend(loc='upper center', bbox_to_anchor=(0.47, -0.2),fancybox=True, shadow=True, ncol=5, fontsize=12)
    #legend.get_frame().set_facecolor('#FFFFFF')
    plt.xlabel('Atom', fontsize=12)
    plt.ylabel('Proportion', fontsize=12)
    tt = t#['Real', 'PSO']
    plt.xticks(t, tt, fontsize=5)
    plt.yticks(fontsize=12)
    # Turn off tick labels
    ax.set_yticklabels([])
    ax.set_title('Real x PSO', fontsize=12)
    plt.show()
    pasta = "C:/Users/Bruno Pimentel/Desktop/paralelas.png"
    fig.savefig(pasta, dpi=300, format="png", bbox_inches="tight")
    
def gerarPontos(TG, file_names, nomes):
    dados = []
    for file_name in file_names:
        dados.append(read_file(file_name))
     
    fig = plt.figure()
    ax = plt.subplot(111)
    v = var(dados[1])
    print(v)
    index = np.argsort([-v[i] for i in range(len(v))])
    print(index)
    var_x = index[0]
    var_y = index[1]
    x_real = [float(dados[0][i][var_x]) for i in range(len(dados[0]))]
    y_real = [float(dados[0][i][var_y]) for i in range(len(dados[0]))]    
    x_pso = [float(dados[1][i][var_x]) for i in range(len(dados[1]))]
    y_pso = [float(dados[1][i][var_y]) for i in range(len(dados[1]))]
    plt.scatter(x_real, y_real, c='r', s=15, marker='s', alpha=0.5, label='Real')
    plt.scatter(x_pso, y_pso, c='b', s=15, marker='o', alpha=0.5, label = 'PSO')
    
    ax.set_title('TG = '+str(TG), fontsize=12)
    plt.xlabel(nomes[var_x], fontsize=12)
    plt.ylabel(nomes[var_y], fontsize=12)
    
    plt.legend()
#    plt.grid(True)
    
#    box = ax.get_position()
#    ax.set_position([box.x0, box.y0 + box.height * 0.1,box.width, box.height * 0.9])
#    legend = ax.legend(loc='upper center', bbox_to_anchor=(0.47, -0.2),fancybox=True, shadow=True, ncol=5, fontsize=12)
#    legend.get_frame().set_facecolor('#FFFFFF')
    
    plt.show()
    
#    print (maximo_lista(x_real), maximo_lista(y_real))
#    print (maximo_lista(x_pso), maximo_lista(y_pso))
    
    print(len(dados[0]))
    print(len(dados[1]))
    
    pasta = "C:/Users/Bruno/Desktop/TG_"+str(TG)[2]+".png"
    fig.savefig(pasta, dpi=300, format="png", bbox_inches="tight")
    

TG = 0.9
nomes = ['Cd', 'Yb', 'Cs', 'N', 'Mn', 'S', 'Ce', 'Er', 'I', 'Mo',
         'Cl', 'As', 'Ga', 'Cu', 'Sn', 'Ag', 'Ta', 'Y', 'Gd', 'Ge',
         'V', 'Fe', 'W', 'F', 'Sb', 'Sr', 'Te', 'Nb', 'Bi', 'La',
         'Pb', 'Zr', 'Ti', 'Mg', 'Ba', 'K', 'Ca', 'Zn', 'Li', 'P',
         'Al', 'Na', 'B', 'Si', 'O'] 
real = "C:/Users/Bruno/Downloads/Glass/util/output_real_9.csv"
pso = "C:/Users/Bruno/Downloads/Glass/util/output_PSO_9.csv"
file_names = [real, pso]
#gerarParalelas(file_names)
gerarPontos(TG, file_names, nomes)
