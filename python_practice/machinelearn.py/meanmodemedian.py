'''#Finding mean and median using numpy
import numpy as np
s=[99,86,87,88,111,86,103,87,94,78,77,85,86]
med=np.median(s)
print(f"Median for the s : {med}")

mea=np.mean(s)
print(f"Mean for the s : {mea : 2f}")

#Finding mode by using scipy
import scipy
from scipy import stats
mod=stats.mode(s)
print(f"Mode for the given s : {mod}")'''
import sys
import matplotlib
matplotlib.use('Agg')

import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 250)

plt.hist(x, 5)
plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()