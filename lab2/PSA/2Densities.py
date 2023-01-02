import random

def triangel_posibility(side_a, side_b, side_c):
    if side_a + side_b > side_c and side_a + side_c > side_b and side_c + side_b > side_a:
        return True
    else:
        return False
    
triangel_count = 0

for _ in range(1000000):
    breakpoint_1 = random.randint(0, 100)
    breakpoint_2 = random.randint(0, 100)

    if breakpoint_1 > breakpoint_2:
        temp = breakpoint_1
        breakpoint_1 = breakpoint_2
        breakpoint_2 = temp

    a = breakpoint_1
    b = breakpoint_2 - breakpoint_1
    c = 100 - breakpoint_2

    if triangel_posibility(a, b, c):
        triangel_count += 1

print(triangel_count / 1000000)