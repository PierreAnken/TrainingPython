# t1
import math
from pprint import pprint

import numpy
import matplotlib.pyplot
import random

from scipy.optimize import curve_fit


# t2
def f(x, a, b, c):
    return a * math.e ** (-b * x) + c


# t3
xdata = numpy.arange(0, 4, 0.1)

# t4
ydata = []
for x in xdata:
    ydata.append(f(x, 2.5, 1.3, 0.5) + random.uniform(-0.1, 0.1))

# t5
popt, pcov = curve_fit(f, xdata, ydata)

# t6
matplotlib.pyplot.plot(xdata, ydata)

# t7
matplotlib.pyplot.plot(xdata, f(xdata,popt[0],popt[1],popt[2]))
