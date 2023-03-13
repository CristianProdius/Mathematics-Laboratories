from scipy.interpolate import lagrange
import numpy as np
import math
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 8)
y1 = np.sqrt(x + 1)

i = np.arange(7)
xk = np.cos((2 * i + 1) * math.pi / (2 * 7))
y = np.sqrt(xk + 1)
x_new = np.linspace(-1, 1, 100)
y_final = np.sqrt(x_new + 1)

f = lagrange(xk, y)
f1 = lagrange(x, y1)

fig = plt.figure(figsize=(10, 8))
plt.plot(x_new, y_final, 'purple', label='F(x)')
plt.plot(x_new, f(x_new), 'b', label='m7(x)')
plt.plot(x_new, f1(x_new), 'r', x, y1, 'yo', label='P7(x)')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()