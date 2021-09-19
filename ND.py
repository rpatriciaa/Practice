
# normal distribution
# mean = 5, SD= 9, array size=10x10
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

x = random.normal(loc=5, scale=9, size=(10, 10))

print(x)
sns.distplot(x, hist=False)
plt.show()

#poisson
poisson = random.poisson(lam=8, size=1000),
sns.distplot(poisson, hist=False)
plt.show()
sns.distplot(poisson, kde=False)
plt.show()

#binomial
#20 trials, 0.76 probality, arraysize 10
binomial = random.binomial(n=20, p=0.76, size=10)
sns.distplot(binomial, hist=False)
plt.show()

#exponential

exp = random.exponential(scale=8, size=(10, 10))
sns.distplot(exp, hist=False)
plt.show()

# read from random values
# visualize
data = pd.read_csv('MOCK_DATA.csv')
print(data)
sns.distplot(data, hist=False)
plt.show()
