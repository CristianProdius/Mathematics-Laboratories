import numpy as np

def newton_raphson_system(f, J, x0, tol):
    x = x0
    fx = f(x)

    while np.linalg.norm(fx) > tol:
        J_inv = np.linalg.inv(J(x))
        delta_x = -J_inv.dot(fx)
        x = x + delta_x
        fx = f(x)

    return x

def f(x):
    return np.array([x[0]**2 + x[1]**2 - 1, x[0] - x[1]**2])

def J(x):
    return np.array([[2*x[0], 2*x[1]], [1, -2*x[1]]])

x0 = np.array([1, 1])
tol = 1e-6

roots = newton_raphson_system(f, J, x0, tol)

print(f"The roots of the system of equations are: {roots}")
