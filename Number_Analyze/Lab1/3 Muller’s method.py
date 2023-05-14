import math

def muller(f, x0, x1, x2, tol=1e-8, max_iter=100):
    h1 = x1 - x0
    h2 = x2 - x1
    d1 = (f(x1) - f(x0)) / h1
    d2 = (f(x2) - f(x1)) / h2
    d12 = (d2 - d1) / (h2 + h1)
    i = 2
    while i <= max_iter:
        b = d2 + h2 * d12
        D = math.sqrt(b**2 - 4*f(x2)*d12)
        if abs(b - D) < abs(b + D):
            E = b + D
        else:
            E = b - D
        h = -2*f(x2) / E
        p = x2 + h
        if abs(h) < tol:
            return p
        x0 = x1
        x1 = x2
        x2 = p
        h1 = x1 - x0
        h2 = x2 - x1
        d1 = (f(x1) - f(x0)) / h1
        d2 = (f(x2) - f(x1)) / h2
        d12 = (d2 - d1) / (h2 + h1)
        i += 1
    raise Exception("Muller's method failed to converge")
    
f = lambda x: x**3 + 2*x**2 + 10*x - 20
x0 = 0
x1 = 1
x2 = 2
root = muller(f, x0, x1, x2)
print("Root:", root)
print("f(root):", f(root))
