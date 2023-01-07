import random

def the_alone_one():
    lunch = random.sample(range(10), 10)
    dinner = random.sample(range(10), 10)

    for i in range(10):
        if dinner[(i + 1) % 10] == lunch[(i + 1) % 10] or dinner[(i - 1) % 10] == lunch[i]:
            return False
    return True

the_loners = 0
for _ in range(100000):
    if the_alone_one():
        the_loners += 1

print(the_loners / 100000)
