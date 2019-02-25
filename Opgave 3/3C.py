# importing relevant libraries

import matplotlib.pyplot as plt
import numpy as np

# defining variables

m  = 12
k  = 100
g  = 9.81  # or 0 to turn off gravity. (note: y is positive downward)
dt = 0.001 #size of integration time step
t0 = 0     #start time
t1 = 10    #end time
y0 = 0.2   #initial position, downward is positive
v0 = 0.1   #initial velocity, downward is positive

# creating result vectors

t        = np.linspace(t0, t1, round(1 + (t1-t0)/(dt))) #notice the "round" command to prevent warnings
y_num    = np.zeros(len(t))  #vector with zeros, same length as t
v_num    = np.zeros(len(t))  #vector with zeros, same length as t
y_num[0] = y0  #put initial position into first element of result vector 
v_num[0] = v0  #put initial velocity into first element of result vector

def derivatives(state, t): #function name is free to choose, but it must take exactly these two inputs
    y = state[0] #this will seem useless for now, but it is best to always unpack your states here
    v = state[1] #same as above, but a little less useless because we will provide v as a return value
    a = (-k*state[0])/m      #you will modify this line several times during this assignment. For now: constant a
    return [v, a]

for n in range(len(t)-1):
    afgeleiden = derivatives([y_num[n], v_num[n]], t[n])  #calculate derivatives based on previous state
    # calculate new states based on old states and old derivatives
    # notice how the two states (y and v) are treated exactly the same
    y_num[n+1] = y_num[n] + afgeleiden[0]*dt
    v_num[n+1] = v_num[n] + afgeleiden[1]*dt
    if y_num[n]*y_num[n+1] <= 0.00000001:
        print('t(y=0)', t[n], 's')
        
     
plt.figure(1)
plt.plot(t, y_num)
print('y_num', y_num[-1], 'm')
