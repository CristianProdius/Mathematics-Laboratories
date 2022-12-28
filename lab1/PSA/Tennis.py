import random

def dan():
    return random.choice([0, 1])


def ana():
    return random.choice([0, 0, 0, 1, 1, 1, 1, 1, 1, 1])

ana_won = 0
for i in range(1, 10000):
    count_ana = 0
    count_dan = 0
    while(count_ana < 25):
        ana()
        if ana() == 1:
            count_ana += 1
        else:
            count_dan += 1
            dan()
            if dan() == 1:
                count_dan += 1
            else:
                count_ana+= 1
    if count_ana == 25 and count_dan < 25:
        ana_won += 1

print("prob: ", ana_won/10000)