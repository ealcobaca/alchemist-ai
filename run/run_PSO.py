from optpool import PSO
import random
import time
import numpy as np
from util import Reader
from util import Writer

class Run_PSO(object):
    def run(self):
        r = Reader()
        Mm = r.get_max_min_comp('data/AtomFrequency.csv')
        print("Executando PSO")
        tamanhoVetor = 45
        tamanhoAmostra = 500
        valoresAlvo = [0.1, 0.3, 0.5, 0.7, 0.9] 
        for valorAlvo in valoresAlvo:
            print("\n\nValor alvo: "+str(valorAlvo)) 
            start = time.time()
            initialVectors = [np.random.rand(45).tolist() for i in range(tamanhoAmostra)]
            pso = PSO(tamanhoVetor, initialVectors, valorAlvo, Mm)
            result = pso.run()
            results = result.get_result()
            solucoes = results[0]
            valores = results[1]
            erros = results[2]
            end = time.time()
            print(end - start)
            print("--- SOLUCOES ---")
            for i in range(tamanhoAmostra):
              print("P"+str(i+1)+":", end='')
              for j in range(tamanhoVetor):
                print("%.4f " % solucoes[i][j], end='')
              print("")

            print("\n--- VALORES ---")
            print(valores)

            print("\n--- ERROS ---")
            print(erros)

            print("\n--- SOMAS ---")
            for i in range(tamanhoAmostra):
              print(sum(solucoes[i]), end=' ')

            w = Writer()
            nomeArq = 'output_PSO_'+str(valorAlvo)[2]+'.csv'
            w.write_file('util/'+nomeArq, solucoes)
