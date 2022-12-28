import random 
import matplotlib.pyplot as plt 
 
sums = [] 
tries = [] 
def red(): 
    n = int(input()) 
    sum = 0 
    for i in range(500): 
        if random.randrange(1,39) in range(1,19):  
            sum += n 
        else: 
            sum -= n 
        sums.append(sum) 
        tries.append(i) 
    plt.plot(tries, sums) 
    plt.xlabel('Nr. of bets') 
    plt.ylabel('Money') 
    plt.title(f"Roulette Wins Overtime When Betting On Red| Total Wins:{sum}") 
    plt.show() 
 
 
 
sums2 = [] 
tries2 = [] 
def num(): 
    n = int(input()) 
    sum = 0 
    for i in range(500): 
        if random.randrange(1,39) == 18:  
            sum += 35 
        else: 
            sum -= n 
        sums2.append(sum) 
        tries2.append(i) 
    plt.plot(tries2, sums2) 
    plt.xlabel('Nr. of bets') 
    plt.ylabel('Money') 
    plt.title(f"Roulette Wins Overtime When Betting On One Number| Total Wins:{sum}") 
    plt.show() 
 
red() 
 
num()