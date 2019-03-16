# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 09:40:15 2019

@author: Tesla
"""


import matplotlib.pyplot as plt
import numpy as np

"""
Hier je waardes voor: k,m,y0 invullen
"""
Factor = 100
    # defining variables constant
g  = 9.81  # or 0 to turn off gravity. (note: y is positive downward)
dt = 0.001 #size of integration time step
t0 = 0     #start time
t1 = 1   #end time
v0 = 0   #initial velocity, downward is positive

    # defining variables open for change
m  = 1
y0 = 1  
e = 0.8


    #Vectors
t  = np.linspace(t0,t1,int(1 +(t1-t0)/(dt)))
Pos_y = np.zeros(len(t))
Speed_y = np.zeros(len(t))
Accel_y = np.zeros(len(t))
Sum_Force = np.zeros(len(t))
#Fground = np.zeros(len(t))
Frem = np.zeros(len(t))
Impulse = np.zeros(len(t))
ImpulseD = np.zeros(len(t))
Epot = np.zeros(len(t))
Ekin = np.zeros(len(t))
Etot = np.zeros(len(t))

    #Defined Xeno
Pos_y[0] = y0
Speed_y[0] = v0
Accel_y[0] = -g


for n in range(len(t)-1):
    Accel_y[n] = -g
    Pos_y[n+1] = Pos_y[n]+Speed_y[n]*dt
    Speed_y[n+1] = Speed_y[n]+Accel_y[n]*dt
    if Pos_y[n+1]<0:
        Pos_y[n+1] = 0
        store = -Speed_y[n+1]
        Speed_y[n+1] = store

    #Energie
for n in range(len(t)):
    Epot[n] = m*g*Pos_y[n]
    Ekin[n] = 0.5*m*Speed_y[n]**2
    
Etot = Ekin+Epot


    #Printen
"""
plt.figure(1)
plt.plot(t, Pos_y)
plt.figure(2)
plt.plot(t, Etot)
"""
print("4e")
print("Etot[-1]-Etot[0]=",Etot[-1]-Etot[0],"Joule")

    # defining variables open for change
t1 = 2
m  = 1
y0 = 1  
e = 0.8

    #Vectors
t  = np.linspace(t0,t1,int(1 +(t1-t0)/(dt)))
Pos_y = np.zeros(len(t))
Speed_y = np.zeros(len(t))
Accel_y = np.zeros(len(t))
Sum_Force = np.zeros(len(t))
#Fground = np.zeros(len(t))
Frem = np.zeros(len(t))
Impulse = np.zeros(len(t))
ImpulseD = np.zeros(len(t))
Epot = np.zeros(len(t))
Ekin = np.zeros(len(t))
Etot = np.zeros(len(t))
index = []

    #Defined Xeno
Pos_y[0] = y0
Speed_y[0] = v0
Accel_y[0] = -g


for n in range(len(t)-1):
    Accel_y[n] = -g
    Pos_y[n+1] = Pos_y[n]+Speed_y[n]*dt
    Speed_y[n+1] = Speed_y[n]+Accel_y[n]*dt
    
    if Pos_y[n+1]<0:
        index.append(n)
        Pos_y[n+1] = 0
        store = -Speed_y[n+1]
        Speed_y[n+1] = store*e

    #Energie
for n in range(len(t)):
    Epot[n] = m*g*Pos_y[n]
    Ekin[n] = 0.5*m*Speed_y[n]**2
    
Etot = Ekin+Epot
index = np.asarray(np.where(Pos_y==0))[0]
n0 = index[0]

"""
    #Printen
plt.figure(3)
plt.plot(t, Pos_y)
plt.figure(4)
plt.plot(t, Etot)
"""
print("Etot[-1]-Etot[0]=",Etot[-1]-Etot[0],"Joule")
print("Antwoord = optie 1 en 2")
print("Fground =", (max(Speed_y)*m-min(Speed_y)*m))
print("Antwoord = True")


