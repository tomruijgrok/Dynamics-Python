# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 18:34:08 2019

@author: Tesla
"""
import numpy as np
import matplotlib.pyplot as plt

k = 1000
m = 1       #massa = kg
g = 9.81    #gravitatie = m/s^2
y0 = 1      #Start positie = m
v0 = 0      #Start snelheid = m/s
t0 = 0      #Start tijd = s
te = 1       #eind tijd = s
dt = 0.001  #Tijd stap = s
t = np.linspace(t0, te, round(1+(te-t0)/dt))
Pos = np.zeros(len((t)))
lengte = np.zeros(len(t))
Speed_y  = np.zeros(len((t)))
Accel_y = np.zeros(len((t)))
Force_sum = np.zeros(len((t)))
Ekin = np.zeros(len(t))
Etot = np.zeros(len(t))
Epot = np.zeros(len(t))
Force_g = np.zeros(len(t))
Fres = np.zeros(len(t))
Pos[0] = y0
Speed_y[0] = v0


for n in range(len(t)-1):
    Force_g[n] = -k*Pos[n]
    Fres[n] = Force_g[n]-m*g
    if Pos[n] < 0:
        Accel_y[n] = Fres[n]/m
    else:
        Accel_y[n] = -g
    
    Pos[n+1] = Pos[n] + Speed_y[n]*dt
    Speed_y[n+1] = Speed_y[n]+Accel_y[n]*dt
    
for n in range(len(t)):
    Ekin[n] = .5*m*Speed_y[n]**2
    Epot[n] = m*g*Pos[n]

Etot = Ekin+Epot
print("Approximately 100 milliseconds")
print("Ymin=",min(Pos),"m")
plt.figure(2)
plt.plot(t,Pos)
print("Etot[-1]-Etot[0]=",Etot[-1]-Etot[0],"Joule")

