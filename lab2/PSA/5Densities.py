import random, math
def check_real(b, c):
    if b**2 - 4*c > 0:
        return True
    else: return False

def check_positive(b, c):
    if check_real(b, c):
        root_1 = (-b + math.sqrt(b**2 - 4*c)) / 2
        root_2 = (-b - math.sqrt(b**2 - 4*c)) / 2
        if root_1 > 0 and root_2 > 0:
            return True
    return False

total_real = 0
total_positive = 0
for _ in range(100000):
    B = random.uniform(-1, 1)
    C = random.uniform(-1, 1)
    if check_real(B,C):
        total_real += 1
    if check_positive(B, C):
        total_positive += 1

print("Prob. roots are real is: ",total_real / 100000)
print("Prob. roots are positive is: ",total_positive / 100000)