def hybrid_secant_bisection(f, a, b, epsilon, max_iterations):
    if f(a) * f(b) > 0:
        raise ValueError("The function has the same sign at both endpoints of the interval.")

    x0, x1 = a, b
    y0, y1 = f(a), f(b)

    for i in range(max_iterations):
        x2 = x1 - y1 * (x1 - x0) / (y1 - y0)
        y2 = f(x2)

        if abs(y2) < epsilon:
            return x2
        elif abs(x2 - x1) < epsilon:
            return x2
        elif abs(y1) < abs(y0):
            x0, y0 = x1, y1
            x1, y1 = x2, y2
        else:
            c = (a + b) / 2
            if f(c) == 0:
                return c
            elif f(c) * f(a) < 0:
                b = c
            else:
                a = c

    return x2

def f(x):
    return x ** 3 - 5 * x + 1

root = hybrid_secant_bisection(f, 0, 1, 1e-8, 100)
print(root)
