import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return np.exp(x) / np.exp(np.pi) + np.cos(x) - x + np.pi

def dfdx(x):
    return np.exp(x) / np.exp(np.pi) - np.sin(x) - 1

def newton_method(x_0, epsilon):
    tol = epsilon  
    i = 0  
    xi_1 = x_0  

    while abs(f(xi_1)) > tol:
        i += 1
        xi = xi_1 - f(xi_1) / dfdx(xi_1) 
        xi_1 = xi

    print(f"Iteration {i}: x = {xi}, f(x) = {f(xi)}")

xlist = np.linspace(0, 6, num=10000)
ylist = f(xlist)

plt.figure(num=0, dpi=120)
plt.plot(xlist, ylist)

newton_method(3, 1e-06)

plt.show()
