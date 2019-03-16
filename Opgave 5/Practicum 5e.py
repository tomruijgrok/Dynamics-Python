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
r1 = 0.25
m =1.6

Theta_hoek0 = -np.pi/2
Xeno0 = 0
alpha_hoek0 = 0

Theta_hoek = np.zeros(len(t))
Theta_hoekL = np.zeros(len(t))
Xeno = np.zeros(len(t))
XenoL = np.zeros(len(t))
alpha_hoek = np.zeros(len(t))
alpha_hoekl = np.zeros(len(t))
moment = np.zeros(len(t))
momentL = np.zeros(len(t))

Theta_hoek[0] = Theta_hoek0
Theta_hoekL[0] = Theta_hoek0
Xeno[0] = Xeno0
Zeros = []
ZerosL = []
Traagheidsmoments = 1/12*m*(0.5+0.5)
Traagheidsmoment = Traagheidsmoments+m*r**2
for n in range(len(t)-1):
    
    moment[n] = -m*g*r*np.sin(Theta_hoek[n])
    momentL[n] = -m*g*r*(Theta_hoekL[n])
    alpha_hoek[n] = moment[n]/Traagheidsmoment
    alpha_hoekl[n] = momentL[n]/Traagheidsmoment
    Theta_hoek[n+1] = Theta_hoek[n]+Xeno[n]*dt
    Theta_hoekL[n+1] = Theta_hoekL[n]+XenoL[n]*dt
    Xeno[n+1] = Xeno[n]+alpha_hoek[n]*dt
    XenoL[n+1] = XenoL[n]+alpha_hoekl[n]*dt
    if Theta_hoek[n]*Theta_hoek[n+1] <0: 
        Zeros.append(t[n])
    if Theta_hoekL[n]*Theta_hoekL[n+1] <0:
        ZerosL.append(t[n])

tijd = Zeros[2]-Zeros[0]
tijdL = ZerosL[2]-ZerosL[0]
print("Python 5e")
print("I= ",np.round(Traagheidsmoments,3)," kg*m^2")
print("T=",tijd,"s")
print("Tlin=",tijdL,"s")        

plt.plot(t,Theta_hoek,"r-")
plt.plot(t,Theta_hoekL,"y--")
plt.show