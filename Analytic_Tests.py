import numpy as np

class tan:
    def __init__(self, l, k, T, p, M):
        self.l = l
        self.k = k
        self.T = T
        self.p = p
        self.M = M
        #self.wv = wv

    def value(self, wv):
        l = self.l
        k = self.k
        T = self.T
        p = self.p
        M = self.M
        v = np.sqrt(T / p)
        f1 = np.tan(wv * l / 2)
        f2 = 2 * wv * T
        f3 = (M * wv * wv * v * v) - k

        return (f1*f3 - f2)
        