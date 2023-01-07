import random

all_games_winning = []
for _ in range(100000):
    total_wining = 0
    x = random.uniform(0, 1)
    y_sequence = []
    for _ in range(100000):
        y = random.uniform(0, 1)
        if y > x:
            y_sequence.append(y)
            break
        else:
            y_sequence.append(y)
    get_paid = len(y_sequence) - 1
    all_games_winning.append(get_paid)

total = 0
for i in all_games_winning:
    total += i

print(total / 100000)