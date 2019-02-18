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

# def drag(v_num):
#     D = 10*v_num**3
#     return D

# D = drag(v_num)

# def acceleratie(v_num):
#     a=F/m
#     F= -D
#     return acceleratie(v_num)
    
def verplaatsingnumeriek(t):
    x_num = np.zeros(len(t))
    v_num = np.zeros(len(t))
    x_num[0] = x0
    v_num[0] = v0
    for n in range(len(t)-1):
        a = -10*v_num[n]**3
        x_num[n+1] = x_num[n] + v_num[n]*dt
        v_num[n+1] = v_num[n] + a*dt
    return a, x_num, v_num

a, x_num, v_num = verplaatsingnumeriek(t)

print(v_num[-1])