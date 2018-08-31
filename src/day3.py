# Load CSV using Pandas from URL
from pandas import read_csv

filename = "../doc/pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
print(data.shape)
print(data.dtypes)
peek = data.head(20)
print(peek)
