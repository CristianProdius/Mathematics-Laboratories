import random
import matplotlib.pyplot as plt


num_heads_in_each_experiment = []
experiment_posibiliti = ["head", "tail"]
for i in range(1000):
  heads = 0
  for j in range(100):
    if random.choice(experiment_posibiliti) == "head":
      heads += 1
  num_heads_in_each_experiment.append(heads)


head_counts_frequency = {}
for heads in num_heads_in_each_experiment:
  if heads not in head_counts_frequency:
    head_counts_frequency[heads] = 1
  else:
    head_counts_frequency[heads] += 1

proportions = []
for n in range(35, 66):
  if n in head_counts_frequency:
    proportions.append(head_counts_frequency[n])
  else:
    proportions.append(0)


plt.figure(figsize=(9, 4))
plt.title("Mexican head of tosing a coin 100 times for 1000 experiment and leanding on head")
plt.bar(range(35, 66), proportions)
plt.show()

