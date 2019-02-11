#author Tom Ruijgrok
import matplotlib.pyplot as plt 
import numpy as np

#variables
dt = 0.1
t0 = 0
t1 = 10
x0 = 0
v0= 4

t = np.linspace(t0, t1, 1 + t1/dt)

def verplaatsinganalytisch(t):
    x_an = np.zeros(len(t)) 
    x_an[0] = x0
    for n in range(len(t)):
        x_an[n] = x0 + v0*t[n]
    return x_an

def verplaatsing(t):
    x_num = np.zeros(len(t))  
    v_num = np.zeros(len(t))   
    x_num[0] = x0  #initial position 
    v_num[0] = v0  #initial velocity
    for n in range(len(t)-1):
        a = 0   
        x_num[n+1] = x_num[n] + v_num[n]*dt
        v_num[n+1] = v_num[n] +  a  *dt
    return x_num,v_num

x_num,v = verplaatsing(t)
x_an = verplaatsinganalytisch(t)


plt.figure(1)
plt.plot(t, x_num)

plt.plot(t, x_an, 'y--')  #make a yellow dashed line


plt.figure(2)
plt.plot(t, x_num-x_an)   
