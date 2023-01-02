import random, math
import numpy as np

def pol_to_cartisian(degree):
    x = 10 * np.cos(degree)
    y = 10 * np.sin(degree)
    return(x, y)

def acute_triangel(a, b, c):
    cos_c = (c**2 - a**2 - b**2) / (-2*a*b)
    cos_b = (b**2 - c**2 - a**2) / (-2*a*c)
    cos_a = (a**2 - b**2 - c**2) / (-2*c*b)

    angle_c = math.acos(cos_c) * (180 / math.pi)
    angle_b = math.acos(cos_b) * (180 / math.pi)
    angle_a = math.acos(cos_a) * (180 / math.pi)

    if angle_a < 90 and angle_b < 90 and angle_c < 90:
        return True
    else:
        return False

total_acute_triangel = 0

for _ in range(100000):
    degree_a = random.randint(1, 360)
    degree_b = random.randint(1, 360)
    while degree_b == degree_a:
        degree_b = random.randint(1, 360)
    degree_c = random.randint(1, 360)
    while degree_c == degree_b or degree_c == degree_a:
        degree_c = random.randint(1, 360)

    #asume that circel is center at (0,0) and has radius 10
    cartisian_a = pol_to_cartisian(degree_a)
    cartisian_b = pol_to_cartisian(degree_b)
    cartisian_c = pol_to_cartisian(degree_c)

    #side c which lies betwen points a and b
    side_c = math.sqrt((cartisian_b[0] - cartisian_a[0])**2 + (cartisian_b[1] - cartisian_a[1])**2)
    #side b which lies betwenn points a and c
    side_b = math.sqrt((cartisian_c[0] - cartisian_a[0])**2 + (cartisian_c[1] - cartisian_a[1])**2)
    #side a which lies between point b and c
    side_a = math.sqrt((cartisian_c[0] - cartisian_b[0])**2 + (cartisian_c[1] - cartisian_b[1])**2)

    if acute_triangel(side_a, side_b, side_c):
        total_acute_triangel += 1

print(total_acute_triangel / 100000)
