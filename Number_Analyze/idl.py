import math

n = 4
a = [0] * n
b = [0] * n
alfa = 0
a0 = 0.1
b0 = 0.1
a[0] = a0
b[0] = b0

for i in range(n-1):
    a[i+1] = math.cos(a[i]) - 1 + a[i]
    b[i+1] = b[i] - ((math.cos(b[i]) - 1 + b[i]) / (-math.sin(b[i]) + 1))

print("n = 4")
print("Order of convergence n -> infinity will be = 1")
print("Linear convergence")
qa = math.log(abs((a[n-1]-a[n-2])/(a[n-2]-a[n-3]))) / math.log(abs((a[n-2]-a[n-3])/(a[n-3]-a[n-4])))
print("Order of convergence n -> infinity will be =", qa)
print("Quadratic convergence")
qb = math.log(abs((b[n-1]-b[n-2])/(b[n-2]-b[n-3]))) / math.log(abs((b[n-2]-b[n-3])/(b[n-3]-b[n-4])))
print("Order of convergence n -> infinity will be =", qb)
print("when n = 1, a = 0.9")
print("Bisection Method is 1/2")
rate_a = (a[n-1] - a[n-2]) / (a[n-2] - a[n-3])
print("Convergence of a:", rate_a)
print("Convergence of b:", end=' ')
rate_b = (b[n-1] - b[n-2]) / pow((b[n-2] - b[n-3]), 2)
print(rate_b)
print("[", end=' ')
for i in range(n):
    print(a[i], end=' ')
print("]")
print("[", end=' ')
for i in range(n):
    print(b[i], end=' ')
print("]")
print("the order e-10 appeared after 4 iterations")
