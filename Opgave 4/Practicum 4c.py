# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 09:40:15 2019

@author: Tesla
"""


import matplotlib.pyplot as plt
import numpy as np

    # defining variables constant
g  = -9.81  # or 0 to turn off gravity. (note: y is positive downward)
dt = 0.001 #size of integration time step
t0 = 0     #start time
t1 = 1   #end time
v0 = 0   #initial velocity, downward is positive

    # defining variables open for change
k = 800
m  = 1.4
y0 = 0.8  #initial position, downward is positive

    #Vectors
t  = np.linspace(t0,t1,int(1 +(t1-t0)/(dt)))
Pos_y = np.zeros(len(t))
Speed_y = np.zeros(len(t))
Accel_y = np.zeros(len(t))
Sum_Force = np.zeros(len(t))
Fground = np.zeros(len(t))
Frem = np.zeros(len(t))
Impulse = np.zeros(len(t))
ImpulseD = np.zeros(len(t))
Epot = np.zeros(len(t))
Ekin = np.zeros(len(t))
Etot = np.zeros(len(t))

    #Defined Xeno
Pos_y[0] = y0
Speed_y[0] = v0
Accel_y[0] = g
for n in range(len(t)-1):
    
    Fground[n] = -k*Pos_y[n]
    Frem[n] = g*m+Fground[n]
    
    if Pos_y[n] > 0 or n==0:
        Accel_y[n] = g
    else:
        Accel_y[n] = Frem[n]/m
        
    Pos_y[n+1] = Pos_y[n] + Speed_y[n]*dt
    Speed_y[n+1] = Speed_y[n] + Accel_y[n]*dt
    

for n in range(len(t)):
    #Impulse
    Fground[n] = Pos_y[n]*-k
    if Pos_y[n] > 0:
        Fground[n] = 0
    
    Impulse[n] = Impulse[n-1]+Fground[n]*dt
    #Puls
    ImpulseD[n] = m*Speed_y[n]
    #Energie
    Epot[n] = m*g*Pos_y[n]
    Ekin[n] = 0.5*m*Speed_y[n]**2
    Etot[n] = Epot[n]+Ekin[n]

index = np.array(np.where(Fground>0))[0]
n1 = index[0]
n2 = index[-1]

fig5 = plt.figure(3)
plt.plot(t[n1:n2],Fground[n1:n2])
plt.fill_between(t[n1:n2],Fground[n1:n2],color=[0.7,0.7,1] )
plt.xlabel('time (s)')
plt.ylabel('Fground (N)')
fig5.savefig('Python2019-4b-fig5.png', dpi = 300, format = 'png' )

    #Printen
print("4c")
print("n1 =" ,  n1)
print("n2 = " , n2)
print("p[n2]-p[n1]=",ImpulseD[n2]-ImpulseD[n1], "N*s")
print("int. fg*dt =", m*g*t[n2]-m*g*t[n1],"Ns")
print("int. Fground =", Impulse[-1], "Ns")
print("Antwoord 3")


