t=input("Insert the string: ")
res="no substring found"
for i in range(2,len(t)):
       for j in range(0,len(t)-i+1):
              for k in range(j+1,len(t)-i+1):
                     if t[j:j+i]==t[k:k+i]:
                            res=t[j:j+i]
print("Longest substring is: ",res)