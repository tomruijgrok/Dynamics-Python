#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 15:18:31 2019

@author: tomruijgrok
"""

#author Tom Ruijgrok

import matplotlib.pyplot as plt 
import numpy as np

#variables
dt = 0.1
t0 = 0
t1 = 10
y0 = 0
v0 = 0
g = 9.81
m = 6 #kg

t = np.linspace(t0, t1, 1 + t1/dt)

def acceleration(t):
    f = np.sin(t)
    a = f/m
    return a

def verplaatsinganalytisch(t):
    y_an = np.zeros(len(t)) 
    v_an = np.zeros(len(t))
    y_an[0] = y0
    for n in range(len(t)):
        a_an = acceleration(t[n])
        v_an[n] = v_an[n] + a_an*t[n]
        y_an[n] = y_an[n] + v_an[n]*t[n]
    return y_an

def verplaatsing(t):
    y_num = np.zeros(len(t))  
    v_num = np.zeros(len(t))   
    y_num[0] = y0  #initial position 
    v_num[0] = v0  #initial velocity
    for n in range(len(t)-1):
        a = acceleration(t[n])
        y_num[n+1] = y_num[n] + v_num[n]*dt
        v_num[n+1] = v_num[n] +  a  *dt
    return y_num,v_num, a


y_num,v,a = verplaatsing(t)
y_an = verplaatsinganalytisch(t)


plt.figure(1)
plt.plot(t, y_num)

plt.plot(t, y_an, 'y--')  #make a yellow dashed line


plt.figure(2)
plt.plot(t, y_num-y_an)   


print(y_an[100])
print(y_num[100])
print(y_num[100]-y_an[100])
