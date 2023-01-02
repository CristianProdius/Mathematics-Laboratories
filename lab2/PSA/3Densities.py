import random

def triangel_posibility(side_a, side_b, side_c):
    if side_a + side_b > side_c and side_a + side_c > side_b and side_c + side_b > side_a:
        return True
    else:
        return False

triangal_count = 0

for _ in range(1000000):
    breakpoint_1 = random.randint(1, 99)

    length_a = breakpoint_1
    length_b = 100 - length_a

    if length_a > length_b:
        max = length_a
        min = length_b
    else:
        max = length_b
        min = length_a

    breakpoint_2 = random.randint(1, max)

    length_a_from_max = breakpoint_2
    length_b_from_max = max - breakpoint_2

    if triangel_posibility(min, length_a_from_max, length_b_from_max):
        triangal_count += 1

print(triangal_count / 1000000)