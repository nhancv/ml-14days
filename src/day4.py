# Load CSV using Pandas from URL
from pandas import read_csv
from pandas import set_option

filename = "../doc/pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)

# Descriptive Statistics
"""
Count.
Mean.
Standard Deviation.
Minimum Value.
25th Percentile.
50th Percentile (Median).
75th Percentile.
Maximum Value.
"""
# set_option('display.width', 100)
# set_option('precision', 3)
description = data.describe()
print(description)

# Class Distribution
class_counts = data.groupby('class').size()
print(class_counts)

# Correlations Between Attributes
correlations = data.corr(method='pearson')
print(correlations)

# Skew of Univariate Distributions
skew = data.skew()
print(skew)
