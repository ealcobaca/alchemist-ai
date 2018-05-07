from util import Reader
from util import KNN

r = Reader()
data = r.get_data('data/testdata.csv')

knn = KNN()
k = 3
closest_vectors, closest_target, closest_predicted_target = knn.get_closest_TG(data, k, 0.7)
print('\n\nVetores')
print(closest_vectors)
print('\nTarget')
print(closest_target)
print('\nPredicted Target')
print(closest_predicted_target)
