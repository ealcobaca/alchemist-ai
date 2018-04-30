"""
File.....: PSO.py
Author...: Bruno Pimentel
Email....: bappimentel@gmail.com
Github...: https://github.com/bapimentel
Description:
"""


from optpool import PSO
import random
import numpy as np
import time


print("Executando PSO")
tamanhoVetor = 45
tamanhoAmostra = 10
valorAlvo = 0.1
start = time.time()
pso = PSO(tamanhoVetor, tamanhoAmostra, valorAlvo)
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
    print(" %.4f" % solucoes[i][j], end='')
  print("")

print("\n--- VALORES ---")
print(valores)

print("\n--- ERROS ---")
print(erros)

print("\n--- SOMAS ---")
for i in range(tamanhoAmostra):
  print(sum(solucoes[i]), end=' ')
