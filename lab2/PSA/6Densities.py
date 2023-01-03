import math, random
def position_coin():
    x = random.uniform(-2, 2)
    y = random.uniform(-2, 2)
    return x, y

def prob_player_won(x, y):
    return -1<=x<=1 and -1<=y<=1

player_frequency = 0
manager_frequency = 0

for _ in range(100000):
    x, y = position_coin()

    if prob_player_won(x, y):
        player_frequency += 1
    else:
        manager_frequency += 1

prob_player = player_frequency / 1000
prob_manager = manager_frequency / 1000
print("########################")
print("Here are the probabilities of the participants")
print("Prob. player to win is: ", prob_player)
print("Prob. manager to win is: ", prob_manager)
print("*************************")

player_won_money = 0
manager_won_money = 0
for _ in range(100000):
    if random.choices(["player", "manager"], [prob_player, prob_manager]) == ["player"]:
        player_won_money += 1
    else:
        manager_won_money += .25

print("Player won the sum of: ", player_won_money, " lei")
print("Manager won the sum of: ", manager_won_money, " lei")

fairnes = 1*prob_player + (-0.25)*prob_manager
if fairnes > 0:
    print("The game is in favor of the player")
elif fairnes < 0:
    print("The game is in favor of the manager")
else:
    print("Game is fair")

print("******************************")
x = (0.25*prob_manager) / prob_player
print("In order for the game to be fair the outcome for player should be ", x)
