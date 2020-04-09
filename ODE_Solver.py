import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def f1(l, b, t, wv, C, T, x, M):
    return wv*C*T*np.cos(wv*x)*np.cos(w*t)/(M*np.sin(wv*b))

def f2(l, b, t, wv, C, T, x, M):
    return -wv*C*T*np.cos(wv*(l-x))*np.cos(w*t)/(M*np.sin(wv*(l-b)))

def ode(y, t, wv, C, T, x, l, b, w, M, k):
    f1 = (wv*C*T*np.cos(wv*x)*np.cos(w*t)/(M*np.sin(wv*b)))
    f2 = (wv*C*T*np.cos(wv*(l-x))*np.cos(w*t)/(M*np.sin(wv*(l-b))))
    y, y2 = y

    derivs = [y2, -y*k/M +f1  +f2 ]
    return derivs

# Call the ODE solver
soln = odeint(ode, y0, t, args=(params))

# Plot results
fig = plt.figure(1, figsize=(8,8))

# Plot theta as a function of time
ax1 = fig.add_subplot(311)
ax1.plot(t, soln[:,0])
ax1.set_xlabel('time')
ax1.set_ylabel('theta')