#author Tom Ruijgrok

import matplotlib.pyplot as plt 
import numpy as np 

#variables
x0 =  0 #m
v0 = 5 #m/s
P = 10 #N
m = 100 #kg
dt = 0.1
t0 = 0
t1 = 400



#timestamp
t = np.linspace(t0, t1, 1 + t1/dt)

acc = P/m

print(acc)

def verplaatsingnumeriek(t):
    x_num = np.zeros(len(t))
    v_num = np.zeros(len(t))
    x_num[0] = x0
    v_num[0] = v0
    for n in range(len(t)-1):
        a = acc
        x_num[n+1] = x_num[n] + v_num[n]*dt
        v_num[n+1] = v_num[n] + a*dt
    return x_num, v_num, a

x_num, v_num, a = verplaatsingnumeriek(t)


print(v_num[-1])