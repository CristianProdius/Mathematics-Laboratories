import random
import matplotlib.pyplot as plt

def sum_9(a, b, c):
    if a + b + c == 9:
        return True
    else:
        return False

def sum_10(a, b, c):
    if a + b + c == 10:
        return True
    else:
        return False

count_9 = 0 
count_10 = 0 

for _ in range(1000000):
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    dice_3 = random.randint(1, 6)

    if sum_9(dice_1, dice_2, dice_3):
        count_9 += 1
    if sum_10(dice_1, dice_2, dice_3):
        count_10 += 1
    
print("Probability of a 9 sum: ", count_9 / 1000000 )
print("Probability of a 10 sum: ", count_10 / 1000000 )

names = ['sum_9', 'sum_10']
values = [count_9, count_10]

plt.figure(figsize=(9, 4))
plt.bar(names, values)
plt.title('Frequency of apperence of a sum of 9 or a sum of 10')
plt.show()