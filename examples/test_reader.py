from util import Reader

r = Reader()
mM = r.get_max_min_comp('data/AtomFrequency.csv')
print(mM)

data = r.get_data('data/testdata.csv')
print(data)
