import random 
 
nr = 100000 
 
def spin_6(): 
    li = [1,2,3,4,"DEAD","DEAD"]     
    counter = 0 
    for _ in range(nr): 
        chance = random.choice(li)  
        if chance != "DEAD": 
            counter += 1 
    return print(counter/nr,"spin_6") 
 
 
def no_spin_6(): 
    li = [1,2,3,"DEAD"] 
    counter = 0 
    for _ in range(nr): 
        chance = random.choice(li)  
        if chance != "DEAD": 
            counter += 1 
    return print(counter/nr,"no_spin_6") 
 
 
def spin_6_na(): 
    li = [1,2,"DEAD1",4,5,"DEAD2"] 
    counter = 0 
    for _ in range(nr): 
        chance = random.choice(li)  
        if chance not in ["DEAD1","DEAD2"]: 
            counter += 1 
    return print(counter/nr,"spin_6_na") 
 
def no_spin_6_na(): 
    li = ["DEAD1",2,3,"DEAD2"]  
    counter = 0 
    for _ in range(nr): 
        chance = random.choice(li)  
        if chance not in ["DEAD1","DEAD2"]: 
                counter += 1 
    return print(counter/nr,"no_spin_6_na") 
 
 
def spin_5(): 
    li = [1,2,3,"DEAD1","DEAD2"] 
    counter = 0 
    for _ in range(nr): 
        chance = random.choice(li)  
        if chance not in ["DEAD1","DEAD2"]: 
            counter += 1 
    return print(counter/nr,"spin_5") 
 
 
def no_spin_5(): 
    li = [1,2,"DEAD"] 
    counter = 0 
    for _ in range(nr): 
        chance = random.choice(li)  
        if chance != "DEAD": 
            counter += 1 
    return print(counter/nr,"no_spin_5") 
 
 
def spin_5_na(): 
    li = [1,2,"DEAD1",4,"DEAD2"] 
    counter = 0 
    for _ in range(nr): 
        chance = random.choice(li)  
        if chance not in ["DEAD1","DEAD2"]: 
            counter += 1 
    return print(counter/nr,"spin_5_na") 
 
def no_spin_5_na(): 
    li = ["DEAD1",2,"DEAD2"] 
    counter = 0 
    for _ in range(nr): 
        chance = random.choice(li)  
        if chance not in ["DEAD1","DEAD2"]: 
                counter += 1 
    return print(counter/nr,"no_spin_5_na") 
 
 
 
spin_6() 
no_spin_6() 
spin_6_na() 
no_spin_6_na() 
print("-"*40) 
spin_5() 
no_spin_5() 
spin_5_na() 
no_spin_5_na()