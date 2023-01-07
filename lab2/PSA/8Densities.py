import random

def the_alone_one():
    lunch = random.sample(range(10), 10)
    dinner = random.sample(range(10), 10)

    neighbors_lunch = []
    neighbors_dinner = []
    for i in range(10):
        neighbors_lunch.append([lunch[(i-1)%10], lunch[i], lunch[(i+1)%10]])
    for i in range(10):
        neighbors_dinner.append([dinner[(i-1)%10], dinner[i], dinner[(i+1)%10]])

    for i in range(10):
        if neighbors_lunch[i] in neighbors_dinner or neighbors_dinner[i] in neighbors_lunch:
            return False
    return True



arent_seting_at_both_lunch_and_dinner = 0
for _ in range(100000):
    if the_alone_one():
        arent_seting_at_both_lunch_and_dinner  += 1

print(arent_seting_at_both_lunch_and_dinner  / 100000)
