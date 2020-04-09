import scipy as sci
import numpy as np
import matplotlib.pyplot as plt
from math import *


class loaded_boyo:

    """Plots the straight line and tan graph to find analytical solutions for sprinf attached to string"""
    def eoq(self):#, M, p, T, k, l, b):
        #test = [31*x/60, 32*x/60, 33*x/60, 34*x/60, 35*x/60, 40*x/60, 45*x/60, 50*x/60, 55*x/60, x]
        xs = np.linspace(0, (2*pi), 3003)
        #xs2 = np.linspace(0, 45*pi/100, 303) + np.linspace(55*pi/100, pi, 303) + np.linspace(pi, 145*pi/100, 303)+ np.linspace(155*pi/100, 2*pi, 303)
        #x = xs
        """"(pi+0.01)/2"""
        F3 = -xs/(0.5)
        #x = np.linspace(math.pi/2, math.pi)
        #plt.plot(np.tan(np.array([-pi,pi/2,pi])))
        plt.plot(xs, np.tan(xs))
        plt.plot(xs, F3, 'r')
        plt.show()
        y = np.zeros(100)
        plt.plot(xs, np.sin(xs), 'y')
        plt.plot(xs, np.cos(xs), 'g')
        plt.plot(xs, np.tan(xs), 'r')
        #plt.plot(xs, y, 'r--')
        plt.vlines(x=pi, ymin=-1.1, ymax=1.1)
        plt.show()
        #print(xs)

        for i in xs:
            x = i
            #print(x)
            F = -2*x
            F2 = np.tan(x/2)
            #print(F, F2)
            #print('')

            if x > 0.005 and abs(abs(F)-abs(F2))<0.2:
                print('solution simplified')
                print(x)
                print(F, F2)

                return
            elif i == pi:
                return
            else:
                i+=1
        return

    """Finds solution by equating a complex function of sines to 1. Not very good. USes l, b, k and M"""
    def unsimplified(self, l, b, k, M):
        wv = np.linspace(0, 20*pi, 3003)


        for i in wv:
            Mp = M * i*i
            Sol = ((Mp-k)/i) * sin(i*l)*sin(i*(l-b))/(sin(i*b))
            plt.plot(i, Sol, 'b+')
            #print(i)
            #print(Sol)
            #print()
            if 1-abs(Sol)<0.001:
                print('the solution is kappa = ')
                print(i)
                return
            elif i == 2*pi:
                print("no solution found")
            else:
                i+=1

    """Returns the value for the complex sine function for given values. T and v are set to 1."""
    def solution(self, l, b, k, M, i):
        Mp = M*i*i
        Sol1 = ((Mp - k) / i) * sin(i * l) * sin(i * (l - b)) / (sin(i * b))
        print(i, Sol1)
        return

    """Returns values of the complex sine function for variables l and b with the wavevector scanned through -2pi to 2pi"""
    def sines(self, l, b):
        wv = np.linspace(-2*pi, 2*pi, 303)
        print(l, b, (l-b))
        for i in wv:
            Sines = sin(i*l)*sin(i*(l-b))/(sin(i*b))
            plt.plot(i, Sines, 'b+')
            plt.plot(i, sin(i), 'r+')
            #plt.plot(i, np.tan(i), 'r.')
            #plt.plot(i, -2*i, 'r.')
            print(i)
            #print(Sines)
            #print()
        return

    """Attempts to plot a graph of both the even and odd overtones for the simplified eqn of b=l/2"""
    def complicatedSolTans(self,l, b, k, M):
        wv = np.linspace(0, 2*pi, 62)

        for i in wv:
            Mp = M*i*i
            tanp = (Mp-k)*tan(i*l/2)/i
            F = sin(i*l/2)*(tanp - 2)
            plt.plot(i, F, 'r+')
        return

    """Solves and plots complex sine fuynction -1 and should show the points at which this function is zero."""
    def misimpliSines(self, l, b, k, M):
        wv = np.linspace(0, 2*pi, 63)

        for i in wv:
            Mp = M * i*i
            Sol = (((Mp-k)/i) * sin(i*l)*sin(i*(l-b))/(sin(i*b))) - 1
            plt.plot(i, Sol, 'b+')
            #print(i)
            #print(Sol)
            #print()

    """NUmerically solves the equation of sine terms. Returns many values of wavevector arounds its multiple minima"""
    def idk(self, l, b):
        wv = np.linspace(0, 2*pi, 63)
        wv2 = np.linspace (0, 0.001, 100)
        wv3 = np.linspace(1.5, 1.8, 3000)
        wv4 = np.linspace(3.141, 3.142, 100)
        wv5 = np.linspace(4.6, 5.0, 4000)
        wv6 = np.linspace(6.28, 6.29, 500)
        for i in wv:
            f1 = -sin(i)*sin(i)
            f2 = 2*i*sin(2*i)
            plt.plot(i, f1, 'g+')
            plt.plot(i, f2, 'b+')
            plt.plot(i, f2-f1, 'r+')
        plt.show()
        for i in wv2:
            f1 = -sin(i)*sin(i)
            f2 = 2*i*sin(2*i)
            plt.plot(i, f2-f1, 'g+')
            if abs(f2-f1) < 0.001:
                print('solution is:')
                print(i)
        for i in wv3:
            f1 = -sin(i)*sin(i)
            f2 = 2*i*sin(2*i)
            plt.plot(i, f2-f1, 'g+')
            if abs(f2-f1) < 0.001:
                print('solution is:')
                print(i)
        for i in wv4:
            f1 = -sin(i)*sin(i)
            f2 = 2*i*sin(2*i)
            plt.plot(i, f2-f1, 'g+')
            if abs(f2-f1) < 0.001:
                print('solution is:')
                print(i)
        for i in wv5:
            f1 = -sin(i)*sin(i)
            f2 = 2*i*sin(2*i)
            plt.plot(i, f2-f1, 'g+')
            if abs(f2-f1) < 0.001:
                print('solution is:')
                print(i)
        for i in wv6:
            f1 = -sin(i)*sin(i)
            f2 = 2*i*sin(2*i)
            plt.plot(i, f2-f1, 'g+')
            if abs(f2-f1) < 0.001:
                print('solution is:')
                print(i)
        return
    
    """Sames as above? Not sure of the difference"""
    def idk2(self, l, b):
        wv = np.linspace(0, 4*pi, 63)
        wv2 = np.linspace (0, 0.001, 100)
        wv3 = np.linspace(1.5, 1.8, 3000)
        wv4 = np.linspace(3.141, 3.142, 100)
        wv5 = np.linspace(4.6, 5.0, 4000)
        wv6 = np.linspace(6.28, 6.29, 500)
        for i in wv:
            f1 = -sin(i/2)*sin(i/2)
            f2 = i*sin(i)
            plt.plot(i/2, f1, 'g+')
            plt.plot(i/2, f2, 'b+')
            plt.plot(i/2, f2-f1, 'r+')
        plt.show()
        for i in wv2:
            f1 = -sin(i/2)*sin(i/2)
            f2 = i*sin(i)
            plt.plot(i, f2-f1, 'g+')
            if abs(f2-f1) < 0.001:
                print('solution is:')
                print(i)
        for i in wv3:
            f1 = -sin(i/2)*sin(i/2)
            f2 = i*sin(i)
            plt.plot(i, f2-f1, 'g+')
            if abs(f2-f1) < 0.001:
                print('solution is:')
                print(i)
        for i in wv4:
            f1 = -sin(i/2)*sin(i/2)
            f2 = i*sin(i)
            plt.plot(i, f2-f1, 'g+')
            if abs(f2-f1) < 0.001:
                print('solution is:')
                print(i)
        for i in wv5:
            f1 = -sin(i/2)*sin(i/2)
            f2 = i*sin(i)
            plt.plot(i, f2-f1, 'g+')
            if abs(f2-f1) < 0.001:
                print('solution is:')
                print(i)
        for i in wv6:
            f1 = -sin(i/2)*sin(i/2)
            f2 = i*sin(i)
            plt.plot(i, f2-f1, 'g+')
            if abs(f2-f1) < 0.001:
                print('solution is:')
                print(i)
        return

    """Finds solutions from numerically equating sine terms. 
    Tightened around the known values for a b = l/2 string."""
    def test20(self, l, b):
        wv = np.linspace(0, 4*pi, 63)
        wv2 = np.linspace (0, 0.001, 100)
        wv3 = np.linspace(3.0, 3.6, 3000)
        wv4 = np.linspace(6.282, 6.284, 100)
        wv5 = np.linspace(9.2, 10.0, 4000)
        wv6 = np.linspace(12.56, 12.58, 500)
        for i in wv:
            f1 = -sin(i*b)*sin(i*(l-b))
            f2 = i*sin(i*l)

            plt.plot(i*l/2, f1, 'g+')
            plt.plot(i*l/2, f2, 'b+')
            plt.plot(i*l/2, f2-f1, 'r+')
        plt.show()
        for i in wv2:
            f1 = -sin(i*b)*sin(i*(l-b))
            f2 = i*sin(i*l)
            #plt.plot(i, f2-f1, 'g+')
            if abs(f2-f1) < 0.001:
                print('solution is:')
                print(i*l/2)
        for i in wv3:
            f1 = -sin(i*b)*sin(i*(l-b))
            f2 = i*sin(i*l)
            #plt.plot(i, f2-f1, 'g+')
            if abs(f2-f1) < 0.001:
                print('solution is:')
                print(i*l/2)
        for i in wv4:
            f1 = -sin(i*b)*sin(i*(l-b))
            f2 = i*sin(i*l)
            #plt.plot(i, f2-f1, 'g+')
            if abs(f2-f1) < 0.001:
                print('solution is:')
                print(i*l/2)
        for i in wv5:
            f1 = -sin(i*b)*sin(i*(l-b))
            f2 = i*sin(i*l)
            #plt.plot(i, f2-f1, 'g+')
            if abs(f2-f1) < 0.001:
                print('solution is:')
                print(i*l/2)
        for i in wv6:
            f1 = -sin(i*b)*sin(i*(l-b))
            f2 = i*sin(i*l)
            #plt.plot(i, f2-f1, 'g+')
            if abs(f2-f1) < 0.001:
                print('solution is:')
                print(i*l/2)
        return

    """Finds solutions by equating sine terms again but includes k and T variables"""
    def kandTincl(self,l, b, k, T):
        wv = np.linspace(0, 4*pi, 50000)
        for i in wv:
            f1 = -k*sin(i*b)*sin(i*(l-b))
            f2 = i*T*sin(i*l)
            if abs(f2-f1) < 0.001:
                print(f"solution is {i} while kl/2 is  {i*l/2}")
        return

    """Analytically solves a simplified case with b = l/2 and M=0. Returns many values for differences smaller than 1 part in a thousand."""
    def tan(self, l, k, T):
        wv = np.linspace(0, 5*pi, 1000000)
        for i in wv:
            f1 = tan(i*(l)/2)
            f2 = -2*T*i/k
            if abs(-f2+f1) < 0.001:
                print(f"Tan solution is {i} while kl/2 is  {i*l/2}")
        return

    """Numerically solves by equating sine terms. Mass, tension, k, density and length all given. Returns a wavevector value"""
    def kTMandvincl(self,l, b, k, T, M, p):
        wv = np.linspace(0, 4*pi, 50000)
        v = sqrt(T/p)
        for i in wv:
            f1 = (M*i*i*v*v) - k
            f2 = sin(i*b)*sin(i*(l-b))
            f3 = i*T*sin(i*l)
            if abs(f3-f1*f2) < 0.001:
                print(f"solution is {i} while kl/2 is  {i*l/2}")
        return

    """Analytical solution using tans where k=0  and b=l/2. v=1"""
    def MassonString(self, l, M, p):
        wv = np.linspace(0, 4 * pi, 50000)
        for i in wv:
            f1 = tan(i*l/2)
            f2 = 2*p*l/(M*i*l)
            #plt.plot(i*l/2, f1, 'g+')
            #plt.plot(i*l/2, f2, 'b+')
            if abs(f2 - f1) < 0.001:
                print(f"Textbook solution is {i} while kl/2 is  {i * l / 2}")
        return


    """Solves the problem of a string loaded with a resonator numerically by equating sine terms. Returns many values of wavevectors around the functions minima"""
    def resonator(self,l, b, k, T, M, p):
        wv = np.linspace(0, 5*pi, 1000000)
        v = sqrt(T/p)
        sol = []
        for i in wv:
            f1 = (M*i*i*v*v) - k
            f2 = sin(i*b)*sin(i*(l-b))
            f3 = i*T*sin(i*l)
            if abs(f3-f1*f2) < 0.001:
                print(f"solution is {i} while kl/2 is  {i*l/2}")
            sol.append((f3-f1*f2))
        plt.plot(wv,sol)
        plt.show()
        return

    """Analytically solves the same problem as above and plots a graph that can be compared with the one on page 334"""
    def resonatorAnalytical(self, l, k, T, M, p):
        wv= np.linspace(0, 5*pi, 1000)
        v = sqrt(T/p)
        for i in wv:
            f1 = tan(i*l/2)
            f2 = 2*i*T
            f3 = (M*i*i*v*v) - k
            if f1 < 10 and f1 > -10:
                plt.plot(i*l/2, f1, 'r.')
            if f2/f3 < 10 and f2/f3 > -10:
                plt.plot(i*l/2, f2/f3, 'b+')
            plt.vlines(x=sqrt(k*p/(T*M))*l/2, ymin=-10, ymax=10, colors='g', linestyles='dashdot')
            plt.vlines(x=pi/2, ymin=-10, ymax=10, colors='k', linestyles='dashed')
            plt.vlines(x=3*pi/2, ymin=-10, ymax=10, colors='k', linestyles='dashed')
            if abs(f1 - (f2/f3)) < 0.0001:
                print(f"solution is this here buddy {i} aka kl/2 {i*l/2}")
                print(f"f1 is {f1}, f2/f3 is {f2/f3}")
                print()

string3 = loaded_boyo()
#string3.eoq()
#string3.unsimplified(1, 0.5, 1, 0)
#string3.sines(1,0.5)
#string3.solution(1, 0.5, 1, 0, 0.000000000000000000000001)

""" """
#string3.misimpliSines(1,0.5,1,0)
#string3.complicatedSolTans(1,0.5,1,0)
#string3.idk(1, 0.5)

"""th th"""
#string3.test20(1, 0.5)
#string3.kandTincl(1, 0.5, 1, 1)
#string3.tan(1,1,1)

"""working with mass and velocity now too, first one is a check that all still works if mass is zero"""
#string3.kTMandvincl(1,0.5,0,1,0.5,1) # l b k T M p
#string3.MassonString(1, 0.5, 1) #l M p


"""working with an attached resonator now"""
string3.resonator(1, 0.5, 1, 1, 1, 1) # l b k T M p
#string3.resonatorAnalytical(1,20,1,1,1) # l k T M p

#plt.hlines(y=1, xmin=0, xmax=6)
#plt.hlines(y=-1, xmin=0, xmax=6)
#plt.xlabel('kappa')
plt.axvline(x=0, color='k')
plt.axhline(y=0, color='k')
plt.grid()
plt.show()