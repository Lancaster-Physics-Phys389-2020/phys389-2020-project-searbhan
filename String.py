import decimal

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import math as math

class string_unloaded:
    def __init__(self, density, length, tension):
        self.density = density
        self.length = length
        self.tension = tension

    def freq(self):
        p = self.density
        l = self.length
        T = self.tension
        f=1/(2*l)*math.sqrt(T/p)
        return f

    def nodePlacer(self, b):
        #b is the position of the node on the string
        #l-b is the distance to the right boundary and b is the distance to the left boundary
        l = self.length
        frac = (l-b)/b

        if (l-b).is_integer() & b.is_integer():
            ##reduce
            d = decimal.Decimal(l)  # self.length)
            print(abs(d.as_tuple().exponent))
        else:
            d = decimal.Decimal(l)  # self.length)
            print(abs(d.as_tuple().exponent))

        return

    def displacementPlot(self, n):
        #assuming the string is bounded so frequency is set I can just use it to find wave speed.
        p = self.density
        l = self.length
        T = self.tension
        f = math.sqrt(T/p)*n/(2*l)
        c = math.sqrt(T/p)
        timeTotal = 2/f
        t = 0

        while t<timeTotal:
            x=0
            print(t)
            while x < l:
                sine = math.sin(n*math.pi*x/(l))
                cosine = math.cos(n*math.pi*c*t/(l))
                sine2 = math.sin(n*math.pi*c*t/l)
                y = sine*(cosine)# +sine2)
                x += l/500
                plt.plot(x, y, 'r.')
            plt.show()
            t+=1/(2*f)
            print(t)
        return


string1 = string_unloaded(0.13,50.125,2.6)
print(string1.density)
print(string1.length)
print(string1.tension)

f = string1.freq()
#string1.displacementPlot(1)
#string1.displacementPlot2()
print(f)
string1.nodePlacer(5.1)