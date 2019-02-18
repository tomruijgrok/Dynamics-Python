#author Tom Ruijgrok

import matplotlib.pyplot as plt 
import numpy as np 

#variables:

v0 = 10 #m/s
x0 = 0 #m
m = 200 #kg
dt = 0.1
t0 = 0 
t1 = 100

#timestamp
t = np.linspace(t0, t1, 1 + t1/dt)

def drag(v)
    D = 10*v**3
    return D

D = drag(v)