import math

def f(x, a):
    return -1 / (a+273.15) + 1.129241e-3 + 2.341077e-4 * math.log(x) + 8.775468e-8 * (math.log(x)) ** 3

def df(x):
    return 2.341077e-4/x + 3*8.775468e-8*math.log(x)**2/x

def newton(x,a):
    tol=1e-6
    while True:
        h=f(x,a)/df(x)
        if abs(h) < tol:
            break
        x -= h
    print("root is ",x)

print("Equation 1: ")
newton(15000, 18.99)
print("Equation 2: ")
newton(15000, 19.01)

