## Parameters
# v_f = free-flow speed (m/s)
# tau = reaction time (s)
# d = minimum safety distance (m)
# N = number of vehicles in the system
# L = total length of the track (m)
# h = step-size
# T = horizon time
# d = the minimum safety distance between two car bumpers
# s = distance between the car and the one immediately in front
# x = total distance travelled by a car

import numpy as np
import matplotlib.pyplot as plt
import random
import math

def speed(s, v_f, tau, d):
    return v_f*(1-math.exp(-1/(v_f*tau)*max(s-d,0)))

#defining the ranges of the speed variables
v_f_max = 80/3.6
v_f_min = 100/3.6
tau_min = 0.5
tau_max = 0.8
d_min = 5
d_max = 8

#set the parameter values
N = 5
L = 100
T = 3600 
h = 0.1
H = int(T/h)

#Randomly selecting unique speed parameters for each driver
v_f = (v_f_max-v_f_min)*np.random.rand(N,1) + v_f_min
d = (d_max-d_min)*np.random.rand(N,1) + d_min
tau = (tau_max-tau_min)*np.random.rand(N,1) + tau_min

#'tau' should be in multiples of 'h'
tau = (np.rint(tau/h))*h
tau_h = np.rint(tau/h)

#Initializing the problem
s = np.zeros([N,H], dtype=float)
v = np.zeros([N,H], dtype=float)

s[:,0] = L/N
v[:,0] = v_f[:,0]
x = np.copy(s)

#Simulate Speeding Dynamics
for t in range (1,H):
    for n in range (0,N):
        if n==0:
            s[n,t] = s[n,t-1] + h*(v[N-1,t-1]-v[n,t-1]) 
        else:
            s[n,t] = s[n,t-1] + h*(v[n-1,t-1]-v[n,t-1])
        s[n,t] = max(s[n,t],d[n,0])

        #Speed Updates
        if t <= tau_h[n,0]:
            v[n,t] = v[n,t-1]
        else:
            v[n,t] = speed(s[n,int(t-tau_h[n,0])],v_f[n,0],tau[n,0],d[n,0])
        x[n,t] = x[n,t-1] + v[n,t-1]*h

#Plotting the Results
time = np.arange(start=0, stop=T, step=0.1)
for i in range(0,N):
    plt.plot(time, v[i,:])
plt.xlabel("Time (s)")
plt.ylabel("Speed (m/s)")
plt.show()

for i in range(0,N):
    plt.plot(time, x[i,:])
plt.xlabel("Time (s)")
plt.ylabel("Distance (m)")
plt.show()