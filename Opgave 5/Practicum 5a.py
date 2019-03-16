# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 12:58:10 2019

@author: Tesla
"""
print("Jezus wat was dit een gedoe een biertje zou fijn zijn ;-)")
import matplotlib.pyplot as plt
import numpy as np


t0 = 0
t1 = 20
dt = 0.001
t = np.linspace(t0,t1,int(1+(t1-t0)/dt))
g = 2
l = 0
r = 0.5
m =1.6

Theta_hoek0 = -np.pi/2
Xeno0 = 0
alpha_hoek0 = 0

Theta_hoek = np.zeros(len(t))
Xeno = np.zeros(len(t))
alpha_hoek = np.zeros(len(t))
moment = np.zeros(len(t))

Theta_hoek[0] = Theta_hoek0
Xeno[0] = Xeno0
Zeros = []
Traagheidsmoment = 1/12*m*l**2+m*r**2

for n in range(len(t)-1):
    moment[n] = -m*g*r*np.sin(Theta_hoek[n])
    alpha_hoek[n] = moment[n]/Traagheidsmoment
    Theta_hoek[n+1] = Theta_hoek[n]+Xeno[n]*dt
    Xeno[n+1] = Xeno[n]+alpha_hoek[n]*dt
    if Theta_hoek[n]*Theta_hoek[n+1] <0:
        Zeros.append(t[n])

tijd = Zeros[2]-Zeros[0]
print("Python 5a")
print("I= 0 kg*m^2")
print("T=",tijd,"s")
print("T=",np.round(np.pi,5),"s")        

plt.plot(t,Theta_hoek,"r-")
plt.show