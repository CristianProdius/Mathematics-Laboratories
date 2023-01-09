import random

def the_alone_one():
    coutnt_repeat = 0
    lunch = random.sample(range(10), 10)
    dinner = random.sample(range(10), 10)

    neighbors_lunch = []
    neighbors_dinner = []
    for i in range(10):
        neighbors_lunch.append([lunch[(i-1)%10], lunch[i], lunch[(i+1)%10]])
    for i in range(10):
        neighbors_dinner.append([dinner[(i-1)%10], dinner[i], dinner[(i+1)%10]])

    for i in range(10):
        if neighbors_lunch[i] in neighbors_dinner:
            coutnt_repeat += 1
    return coutnt_repeat

arent_seting_at_both_lunch_and_dinner = 0
for _ in range(100000):
    arent_seting_at_both_lunch_and_dinner += the_alone_one()

print(arent_seting_at_both_lunch_and_dinner)
print(arent_seting_at_both_lunch_and_dinner  / 100000)
