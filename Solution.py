import numpy as np



def recursive(methodToRun, upper, lower):
    wv = np.linspace(lower, upper, 1001)
    delta = abs(abs(upper)-abs(lower))/1001
    for wv in wv:
        #print(wv)
        if abs(abs(methodToRun(wv)) - abs(methodToRun(wv+delta))) < 0.000001 and ((np.sign(methodToRun(wv)) + np.sign(methodToRun(wv+delta)))) == 0:
            return wv
        elif (np.sign(methodToRun(wv)) + np.sign(methodToRun(wv+delta))) == 0:
            return recursive(methodToRun, (wv+delta), wv)


def rangeFinder(methodToRun, lower, upper):
    i = np.arange(lower, upper, 0.01)
    delta = 0.01#abs(abs(upper)-abs(lower))/10001
    val = []
    sol = []
    kappas = []
    for wv in i:

        val.append(methodToRun(wv))

        if (np.sign(methodToRun(wv)) + np.sign(methodToRun(wv+delta))) == 0:
            sol.append([wv, wv+delta])
            #print(wv, wv+delta)

    for j in sol:
        lower, upper = j
        print(recursive(methodToRun, upper, lower))
        kappas.append(recursive(methodToRun, upper, lower))

    return kappas, sol, val, i