import matplotlib.pyplot as plt
import numpy as np
import time

def f1(wv, b, l, t, x):
    return np.sin(wv*x)*np.cos(wv*t)/np.sin(wv*b)

def f2(wv, b, l, t, x):
    return np.sin(wv*(l-x))*np.cos(wv*t)/np.sin(wv*(l-b))


def plotter(kappas, b, l, t):
    for wv in kappas:
        i = np.linspace(0, l, 1001)
        f1_list = []
        f2_list = []
        x1 = []
        x2 = []
        for x in i:
            if x<b:
                f1_list.append(f1(wv, b, l, t, x))
                x1.append(x)
            elif x>b:
                f2_list.append(f2(wv, b, l, t, x))
                x2.append(x)

        plt.plot(x1, f1_list)
        plt.plot(x2, f2_list)
        plt.show()
    return

def points(kappas, b, l, t):
    for wv in kappas:
        i = np.linspace(0, l, 1001)
        f1_list = []
        f2_list = []
        x1 = []
        x2 = []
        for x in i:
            if x<b:
                f1_list.append(f1(wv, b, l, t, x))
                x1.append(x)
            elif x>b:
                f2_list.append(f2(wv, b, l, t, x))
                x2.append(x)
        return f1_list, f2_list, x1, x2

def maxPoints(wv, b, l, t):
    i = np.linspace(0, l, 1001)
    f1_max = []
    f2_max = []
    for x in i:
        f1_max.append(f1(wv, b, l, 0, x))
        f2_max.append(f2(wv, b, l, 0, x))
    a = max(f1_max)
    c = max(f2_max)
    return a, c

def pointsSingleTone(wv, b, l, t):
    i = np.linspace(0, l, 1001)
    f1_list = []
    f2_list = []
    x1 = []
    x2 = []
    a, c = maxPoints(wv, b, l, 0)
    for x in i:
        if x<b:
            f1_list.append(f1(wv, b, l, t, x))
            x1.append(x)
        elif x>b:
            f2_list.append(f2(wv, b, l, t, x))
            x2.append(x)
    return f1_list, f2_list, x1, x2



def animatorAllTones(kappas, b, l):
    wv0, wv1, wv2, wv3, wv4 = kappas
    kap =[wv0, wv1, wv2, wv3, wv4]
    for wv in kappas:
        timespan = np.arange(0, 5, 0.05)

        plt.ion()

        fig = plt.figure()
        ax1 = fig.add_subplot()
        ax2 = fig.add_subplot()
        ax3 = fig.add_subplot()
        ax4 = fig.add_subplot()
        ax5 = fig.add_subplot()
        plt.show()

        for t in timespan:
            f1_list, f2_list, x1, x2 = pointsSingleTone(wv, b, l, t)
            ax1.clear()
            ax1.set_ylim(-8, 8)
            ax1.plot(x1, f1_list)
            ax1.plot(x2, f2_list)
            plt.draw()
            #time.sleep(0.001)
            plt.pause(0.00001)

def animatorAllTonesSimultaneously(kappas, b, l):
    wv0, wv1, wv2, wv3, wv4 = kappas
    kap =[wv0, wv1, wv2, wv3, wv4]
    timespan = np.arange(0, 5, 0.005)

    plt.ion()

    fig = plt.figure()
    ax1 = fig.add_subplot(221)
    ax2 = fig.add_subplot(222)
    ax3 = fig.add_subplot(223)
    ax4 = fig.add_subplot(224)
    #ax5 = fig.add_subplot(515)
    plt.show()

    for t in timespan:
        for wv in kappas:
            if wv == wv0:
                f1_list, f2_list, x1, x2 = pointsSingleTone(wv, b, l, t)
                ax1.clear()
                ax1.set_ylim(-1.2, 1,2)
                ax1.plot(x1, f1_list)
                ax1.plot(x2, f2_list)
                plt.draw()
                #time.sleep(0.001)
                plt.pause(0.00000001)
            if wv == wv1:
                f1_list, f2_list, x1, x2 = pointsSingleTone(wv, b, l, t)
                ax2.clear()
                ax2.set_ylim(-8, 8)
                ax2.plot(x1, f1_list)
                ax2.plot(x2, f2_list)
                plt.draw()
                #time.sleep(0.001)
                plt.pause(0.00000001)
            if wv == wv2:
                f1_list, f2_list, x1, x2 = pointsSingleTone(wv, b, l, t)
                ax3.clear()
                ax3.set_ylim(-600, 600)
                ax3.plot(x1, f1_list)
                ax3.plot(x2, f2_list)
                plt.draw()
                #time.sleep(0.001)
                plt.pause(0.00000001)
            if wv == wv3:
                f1_list, f2_list, x1, x2 = pointsSingleTone(wv, b, l, t)
                ax4.clear()
                ax4.set_ylim(-10, 10)
                ax4.plot(x1, f1_list)
                ax4.plot(x2, f2_list)
                plt.draw()
                #time.sleep(0.001)
                plt.pause(0.00000001)
            """if wv == wv4:
                f1_list, f2_list, x1, x2 = pointsSingleTone(wv, b, l, t)
                ax5.clear()
                ax5.set_ylim(-8, 8)
                ax5.plot(x1, f1_list)
                ax5.plot(x2, f2_list)
                plt.draw()
                #time.sleep(0.001)
                plt.pause(0.00001)"""


def animator(kappas, b, l):
    timespan = np.arange(0, 10, 0.05)

    plt.ion()

    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
    plt.show()

    for t in timespan:
        f1_list, f2_list, x1, x2 = points(kappas, b, l, t)
        print('yo')
        ax1.clear()
        ax1.set_ylim(-2, 2)
        ax1.plot(x1, f1_list)
        ax1.plot(x2, f2_list)
        plt.draw()
        #time.sleep(0.001)
        plt.pause(0.00001)
