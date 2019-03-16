# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 18:34:08 2019

@author: Tesla
"""
import numpy as np
import matplotlib.pyplot as plt
m = 1       #massa = kg
g = -9.81    #gravitatie = m/s^2
y0 = 1      #Start positie = m
v0 = 0      #Start snelheid = m/s
t0 = 0      #Start tijd = s
te = 1      #eind tijd = s
dt = 0.001  #Tijd stap = s
t = np.linspace(t0, te, int(1+(te-t0)/dt))
Pos = np.zeros(len((t)))
lengte = np.zeros(len(t))
Speed_y  = np.zeros(len((t)))
Accel_y = np.zeros(len((t)))
Force_sum = np.zeros(len((t)))
Ekin = np.zeros(len(t))
Pos[0] = y0
Speed_y[0] = v0
Accel_y[0] = g
Force_sum[0] = m*g
for n in range(1, len(t)):
    Accel_y = g
    Speed_y[n] = Speed_y[n-1]+Accel_y*dt
    Pos[n] = Pos[n-1] + Speed_y[n]*dt 
    Ekin[n] = .5*m*Speed_y[n]**2
    lengte[n] = .5*g*t[n]**2

for n in range(1, len(t)):
    Force_sum[n] = Speed_y[n]/dt/m
    
plt.plot(t,Speed_y)
plt.plot(t,Pos, "y--")
plt.plot(t,lengte, "b")
plt.show
print("y[-1]=",Pos[-1],"m")
print("sumf[-1]= 0 N")
print("Ekin[-1]=",Ekin[-1])