import random

average_won_money = 0
head_got_on_throw = 1
faice_of_coin = ["Tails", "Heads"]
for i in range(100000):
    choice = random.choice(faice_of_coin)
    head_got_on_throw = 1
    while choice != "Heads":
        head_got_on_throw += 1
        choice = random.choice(faice_of_coin)
    average_won_money += pow(2, head_got_on_throw)

print(average_won_money / 100000)