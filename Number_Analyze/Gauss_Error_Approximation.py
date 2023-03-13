import math
import matplotlib.pyplot as plt

def erf(x, n):
    result = 0
    for i in range(n+1):
        numerator = ((-1)**i * x**(2*i+1))
        denominator = math.factorial(i) * (2*i+1)
        result += numerator / denominator
    result *= 2 / math.sqrt(math.pi)
    return result

print(erf(3,30))

x_values = list(range(-3,4))
y_approx = [erf(x,30) for x in x_values]
plt.plot(x_values, y_approx, label='Approximation')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Approximation')
plt.legend()

plt.show()