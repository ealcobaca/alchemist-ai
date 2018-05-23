from util import Reader
from util import Writer
#from util import KNN

class Run_real(object):
    def run(self):
      self.size_vector = 45
      self.index_target = 46
      self.index_predicted_target = 47
      r = Reader()
      data = r.get_data('data/traindata.csv')
      #knn = KNN()
      #knn.get_TG(data, [0.1, 0.3, 0.5, 0.7, 0.9], 0.01)
      list_TG = [0.1, 0.3, 0.5, 0.7, 0.9]
      sd = 0.01
      data2 = []
      for i in range(len(data)):
          row = []
          for j in range(self.size_vector):
              row.append(data[i][j])
          data2.append(row)
      vectors = []
      for TG in list_TG:
          for i in range(len(data)):
            TG_data = data[i][self.index_predicted_target]
            if TG - sd <= TG_data <= TG + sd:
                  vectors.append(data2[i])
          writer = Writer()
          nomeArq = 'output_real_'+str(TG)[2]+'.csv'
          writer.write_file('util/'+nomeArq, vectors)
