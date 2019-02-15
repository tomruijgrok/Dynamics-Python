#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 11:58:45 2019

@author: tomruijgrok
"""

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


def verplaatsingnumeriek(t):
    x_num = np.zeros(len(t))
    v_num = np.zeros(len(t))
    x_num[0] = x0
    v_num[0] = v0
    for n in range(len(t)-1):
        a = acc
        x_num[n+1] = x_num[n] + v_num[n]*dt
        v_num[n+1] = v_num[n] + a*dt
    return a, x_num, v_num

a, x_num,v_num  = verplaatsingnumeriek(t)

def verplaatsinganalytisch(t):
    x_an = np.zeros(len(t))
    v_an = np.zeros(len(t))
    x_num[0] = x0
    v_num[0] = v0
    for n in range(len(t)):
        v_an[n] = v0 + 0.1*t[n]
        x_an[n] = x0 + 0.5*0.1*t[n]**2 +v0*t[n]
    return v_an, x_an

v_an, x_an = verplaatsinganalytisch(t)


xint = np.interp(7000, t , x_num)
print(xint)

print(v_an[-1])
print(x_an[-1])

print(v_num[-1])
print(x_num[-1])

plt.plot(t, x_an)

