import matplotlib.pyplot as plt 
import numpy as np 

#variables
m = 6 #kg
t0 = 0  
x0 = 0
v0 = 0
dt = 0.1
t1 = 10

t = np.linspace(t0, t1, 1+ t1/dt)
t2 = np.linspace(t0, t1, 1+ t1/dt)

def acceleration(t):
    f = 3.5*t
    a = f/m 
    return a
def acceleration2(t2):
    f = -7.4*t2
    a = f/m
    return a

def verplaatsinganalystisch(t):
    x_an = np.zeros(len(t))
    v_an = np.zeros(len(t))
    x_an[0]=x0
    for n in range(len(t)):
        a_an = acceleration(t[n])
        v_an[n] = -np.cos(t[n])/6*t[n]+1/6
        x_an[n] = -np.sin(t[n])/6+t[n]/6
    return x_an, v_an

x_an, v_an = verplaatsinganalystisch(t)

x3 = x_an[100]
v3 = v_an[100]

def verplaatsinganalystisch2(t2):
    x2_an = np.zeros(len(t2))
    v2_an = np.zeros(len(t2))
    x2_an[0] = x3
    v2_an[0] = v3
    for k in range(len(t2)-1):
        a = acceleration2(t2[k])
        v2_an[k] = -np.cos(t[k])/6*t[k]+1/6
        x2_an[k] = -np.sin(t[k])/6+t[k]/6
    return v2_an, x2_an

x4, v4 = verplaatsinganalystisch2(t2)

def verplaatsing(t):
    x_num = np.zeros(len(t))
    v_num = np.zeros(len(t))
    x_num[0] = x0
    v_num[0] = v0
    for n in range(len(t)-1):
        a = acceleration(t[n])
        x_num[n+1] = x_num[n] + v_num[n]*dt
        v_num[n+1] = v_num[n] +  a  *dt
    return x_num, v_num, a

x,v,a = verplaatsing(t)
x_an = verplaatsinganalystisch(t)

x1 = x[100]
v1 = v[100]



#variables
a2 = 0

def verplaatsing2(t2):
    x2_num = np.zeros(len(t2))
    v2_num = np.zeros(len(t2))
    x2_num[0] = x1
    v2_num[0] = v1
    for m in range(len(t2)-1):
        a = acceleration2(t2[m])
        x2_num[m+1] = x2_num[m] + v2_num[m]*dt
        v2_num[m+1] = v2_num[m] +  a  *dt
    return x2_num, v2_num

x2, v2 = verplaatsing2(t2)

# print(x2[100], v2[100])

print(x4[100], v4[100])

plt.figure(1)
plt.plot(t, x2)