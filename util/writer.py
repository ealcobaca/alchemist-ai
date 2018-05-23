"""
File.....: writer.py
Author...: Bruno Pimentel
Email....: bappimentel@gmail.com
Github...: https://github.com/bapimentel
Description:
"""

import csv

class Writer():
  def __init__(self):
    self.type = "writer"

  def write_file(self, file_name, data):
    ofile  = open(file_name, "w")
    writer = csv.writer(ofile, delimiter='\t')
    n_row = len(data)
    for i in range(n_row): 
      #row = ''.join(str(e)+' ' for e in data[i])
      row = data[i]
      writer.writerow(row) 
    ofile.close()  
