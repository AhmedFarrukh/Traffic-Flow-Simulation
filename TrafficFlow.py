## Parameters
# v_f = free-flow speed (m/s)
# tau = reaction time (s)
# d = minimum safety distance (m)
# N = number of vehicles in the system
# L = total length of the track (m)
# t = step-size
# T = horizon time
# d = the minimum safety distance between two car bumpers
# s = distance between the car and the one immediately in front

import numpy as np
import random

#defining the ranges of the speed variables
v_f_max = 80/3.6
v_f_min = 100/3.6
tau_min = 1
tau_max = 2
d_min = 5
d_max = 8

#set the parameter values
N = 5
L = 1000
T = 36 #increase later
t = 0.1

#Randomly selecting unique speed parameters for each driver
v_f = (v_f_max-v_f_min)*np.random.rand(N,1) + v_f_min
d = (d_max-d_min)*np.random.rand(N,1) + d_min
tau = (tau_max-tau_min)*np.random.rand(N,1) + tau_min

#'tau' should be in multiples of 't'
tau = (np.rint(tau/t))*t

#Initializing the problem
s = np.zeros([N,T], dtype=float)
v = np.zeros([N,T], dtype=float)

s[:,0] = L/N
v[:,0] = v_f[:,0]

#Simulate Speeding Dynamics