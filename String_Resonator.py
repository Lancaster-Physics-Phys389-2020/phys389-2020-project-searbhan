import numpy as np
from Numerical_Sine_Tests import *
from Analytic_Tests import *
import matplotlib.pyplot as plt
from Solution import *
from Displacement import *
from matplotlib.animation import FuncAnimation


b = 0.333
l = 1.0
k = 1.0
T = 1.0
p = 1.0
M = 1.0

t = 0.0

sinestring = Sine(l, b, k, T, p, M)
tanstring = tan(l, k, T, p, M)

kappas, sol, val, i = rangeFinder(sinestring.value, 0, 5*np.pi)

print(kappas)
#plotter(kappas, b, l, t)

animatorAllTonesSimultaneously(kappas, b, l)

#f1 = np.sin(wv*x)/np.sin(wv*b)
#f2 = np.sin(wv*(l-x))/np.sin(wv*(l-b))
"""print(recursive(sinestring.value, 16, 6.5))
print(sinestring.value(1.9203776))
print(sinestring.value(1.9203778))
print()
print(recursive(tanstring.value, 16, 6.5))
print(tanstring.value(1.9203776))
print(tanstring.value(1.9203778))"""

"""print()
print(*sol)
l=1
b=0.5
length = np.linspace(0, 1, 1001)
for wv in sol:
    wv1, wv2 = wv
    print(wv1, wv2)
    for x in length:
        if x<b:
            f1 = np.sin(wv1*x)/np.sin(wv1*b)
            plt.plot(x, f1, 'g+')
        elif x>b:
            f2 = np.sin(wv1 * (l-x)) / np.sin(wv1 * (l-b))
            plt.plot(x, f2, 'b+')
        else:
            print('fuck')
    plt.show()"""