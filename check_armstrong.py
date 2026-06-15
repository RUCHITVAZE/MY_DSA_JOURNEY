n =  153 
num = n
nod = len(str(num))
total = 0
while num>0:
    total = total + (num%10)** nod 
    num = num // 10 
    
print(total == n)
print(total)