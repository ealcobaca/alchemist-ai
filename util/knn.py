"""
File.....: knn.py
Author...: Bruno Pimentel
Email....: bappimentel@gmail.com
Github...: https://github.com/bapimentel
Description:
"""

from util import Reader
from scipy.spatial import distance
import numpy as np

class KNN():
    def __init__(self):
        self.type = "knn"
        self.size_vector = 45
        self.index_target = 46
        self.index_predicted_target = 47
    
    #Dado um vetor, retorna k vetores mais proximos a ele
    #e seus respectivos TG
    def get_closest_vector(self, data, k, vector):
        data2 = []
        for i in range(len(data)):
            row = []
            for j in range(self.size_vector):
                row.append(data[i][j])
            data2.append(row)
        distances = []
        for i in range(len(data)):
            d = distance.euclidean(vector, data2[i])
            distances.append(d)
        indices = np.argsort(distances)
        closest_indices = indices[0:k]
        closest_vectors = [data2[indices[i]] for i in range(k)]
        closest_target = [data[indices[i]][self.index_target] for i in range(k)] #Pega o TG
        return closest_vectors, closest_target
        
    #Dado um TG, retorna k TGs mais proximos a ele
    #e seus respectivos vetores
    def get_closest_TG(self, data, k, TG):
        data2 = []
        for i in range(len(data)):
            row = []
            for j in range(self.size_vector):
                row.append(data[i][j])
            data2.append(row)
        distances = []
        for i in range(len(data)):
            d = distance.euclidean([TG], [data[i][self.index_predicted_target]])
            distances.append(d)
        indices = np.argsort(distances)
        closest_indices = indices[0:k]
        closest_vectors = [data2[indices[i]] for i in range(k)]
        closest_target = [data[indices[i]][self.index_target] for i in range(k)] #Pega o TG
        closest_predicted_target = [data[indices[i]][self.index_predicted_target] for i in range(k)]
        return closest_vectors, closest_target, closest_predicted_target
            
