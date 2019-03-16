# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 11:45:54 2019

@author: olafc
"""

import matplotlib.pyplot as plt
import numpy as np
g = 0                    #Gravitatie in m/s^2
m = 12                      #Massa in Kg
t0 = 0                      #Start tijd in s
t1 = 10                     #Eind tijd in s
dt = 0.001                #Tijd stap in s
#ZELF INVULLEN
k = 230                     #Veerstijfheid in N/m
y0 = 0.4                    #Start positie in m
v0 = 0.5                    #Start snelheid in m/s

z = np.sqrt(k/m)
t = np.linspace(t0,t1,int(1+(t1-t0)/dt))
Pos_num = np.zeros(len(t))
Speed_num = np.zeros(len(t))
Pos_num[0] = y0
Speed_num[0] = v0

def derivatives(state, t): #function name is free to choose, but it must take exactly these two inputs
    y = state[0] #this will seem useless for now, but it is best to always unpack your states here
    v = state[1] #same as above, but a little less useless because we will provide v as a return value
    a = g-y*k/m      #you will modify this line several times during this assignment. For now: constant a
    return [v, a]

for n in range(len(t)-1):
    afgeleiden = derivatives([Pos_num[n], Speed_num[n]], t[n])  #calculate derivatives based on previous state
    # calculate new states based on old states and old derivatives

    # notice how the two states (y and v) are treated exactly the same

    Pos_num[n+1] = Pos_num[n] + afgeleiden[0]*dt
    Speed_num[n+1] = Speed_num[n] + afgeleiden[1]*dt 
    

Pos_an = np.zeros(len(t))
Speed_an = np.zeros(len(t))
Pos_an[0] = y0
Speed_an[0] = v0
A = v0/z
Sin = np.zeros(len(t))
for n in range(len(t)):
    Sin[n] = A*np.sin(z*t[n])+y0*np.cos(z*t[n])

plt.figure(1)
plt.plot(t, Pos_num)
plt.plot(t, np.zeros(len(t)), "y--")

plt.plot(t,Sin, "g--")
print("3b1")
print("de waardes v0 y0 en k veranderen vul deze bovenaan opnieuw in")
print("acceleratie =    -y*k/m")
print("Frequency =",z,"rad/s")
print("A =",A,"m")
print("B =",y0,"m")

