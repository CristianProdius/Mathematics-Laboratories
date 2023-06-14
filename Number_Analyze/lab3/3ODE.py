import numpy as np
import matplotlib.pyplot as plt

def resource_utilization(t, U, A, D):
    return A - D

def resource_allocation(t, R, A, D):
    return A - D

t0 = 0  
tf = 10  
dt = 0.1 
num_steps = int((tf - t0) / dt)  

A = np.random.rand(num_steps)  
D = np.random.rand(num_steps)  
R = np.zeros(num_steps)  
U = np.zeros(num_steps)  

#Euler's method
for i in range(num_steps - 1):
    t = t0 + i * dt
    U[i+1] = U[i] + dt * resource_utilization(t, U[i], A[i], D[i])
    R[i+1] = R[i] + dt * resource_allocation(t, R[i], A[i], D[i])

plt.plot(np.arange(t0, tf, dt), U)
plt.xlabel('Time')
plt.ylabel('Resource Utilization')
plt.title('Resource Utilization over Time')
plt.show()
