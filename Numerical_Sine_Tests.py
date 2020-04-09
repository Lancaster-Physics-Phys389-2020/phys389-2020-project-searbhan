import numpy as np

class Sine:

    def __init__(self, l, b, k, T, p, M):
        self.l = l
        self.b = b
        self.k = k
        self.T = T
        self.p = p
        self.M = M
        #self.wv = wv

    def value(self, wv):
        l = self.l
        b = self.b
        k = self.k
        T = self.T
        p = self.p
        M = self.M
        v = np.sqrt(T/p)
        f1 = (M*wv*wv*v*v) - k
        f2 = np.sin(wv*b)*np.sin(wv*(l-b))
        f3 = wv*T*np.sin(wv*l)
        return (f1*f2 - f3)