
import math

ratio = (1 + math.sqrt(5))/2

n1 = 0
n2 = 1
count = 1
terms = 51

while count < terms:
    n_th = n1 + n2
    n1 = n2
    n2 = n_th
    r_n = n2/n1
    error = abs(ratio - r_n)
    print("Iteration number:", count, " Rn =", r_n, " Error =", error)
    count += 1