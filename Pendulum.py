import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def f(y, t, params):
    y1, v = y      # unpack current values of y
    kappa, M, k, T = params  # unpack parameters
    derivs = [v,      # list of dy/dt=f functions
             -y1*k*3/M - T*kappa*2*np.cos(kappa*t/(2*np.sqrt(T)))/(M*np.tan(kappa/2))]
    return derivs

# Parameters
kappa = 1.3*np.pi   #frequency
M =1.0
k =1.0
T =1.0

# Initial values
v0 = 1.0     # initial angular displacement
y0 = 0.0     # initial angular velocity

# Bundle parameters for ODE solver
params = [kappa, M, k, T]

# Bundle initial conditions for ODE solver
y0 = [v0, y0]

# Make time array for solution
tStop = 200.
tInc = 0.01
t = np.arange(0., tStop, tInc)

# Call the ODE solver
psoln = odeint(f, y0, t, args=(params,))

# Plot results
fig = plt.figure(1, figsize=(8,8))

# Plot theta as a function of time
ax1 = fig.add_subplot(311)
ax1.plot(t, psoln[:,0])
ax1.set_xlabel('time')
ax1.set_ylabel('y')

# Plot omega as a function of time
ax2 = fig.add_subplot(312)
ax2.plot(t, psoln[:,1])
ax2.set_xlabel('time')
ax2.set_ylabel('v')

# Plot omega vs theta
ax3 = fig.add_subplot(313)
twopi = 4.0*np.pi
ax3.plot(psoln[:,0]%twopi, psoln[:,1], '.', ms=1)
ax3.set_xlabel('y')
ax3.set_ylabel('v')
ax3.set_xlim(0., twopi)

plt.tight_layout()
plt.show()