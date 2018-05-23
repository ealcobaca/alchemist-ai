"""
File.....: reader.py
Author...: Bruno Pimentel
Email....: bappimentel@gmail.com
Github...: https://github.com/bapimentel
Description:
"""

import csv
import numpy as np

class Reader():
    def __init__(self):
      self.type = "reader"
      
    def read_file(self, file_name):
        reader = csv.reader(open(file_name, "r"), delimiter="\t")
        x = list(reader)
        result = np.array(x)
        return result
    
    def get_max_min_comp(self, file_name):
        # file_name = "AtomFrequency.csv"
        result = self.read_file(file_name)
        selected_columns = [3,4]
        max_min_comp = []
        result = [result[i] for i in range(1,len(result))]
        for row in result:
            maximum = float(row[selected_columns[0]])
            minimum = float(row[selected_columns[1]])
            max_min_comp.append((maximum,minimum))
        return max_min_comp
        
    def get_data(self, file_name, header=True):
        result = self.read_file(file_name)
        begin = 0
        if header:
          begin = 1
        result = np.array([result[i] for i in range(begin,len(result))])          
        result = result.astype(np.float)
        return result
        
        
