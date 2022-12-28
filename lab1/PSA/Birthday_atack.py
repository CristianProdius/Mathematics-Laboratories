import hashlib 
import os 
 
def md5_prime(a): 
   hash = hashlib.md5(a).hexdigest() 
   return hash 
 
collisions = 0 
dic = {} 
for _ in range(2500000): 
   ran_s = os.urandom(40) 
   hash = md5_prime(ran_s) 
   if hash[:10] in dic: 
      print(hash) 
      print(hash[:10]) 
      print(ran_s) 
      collisions += 1 
   else: 
      dic[hash[:10]] = "0" #li.append(hash) 
 
print("Nr of collisions:", collisions)