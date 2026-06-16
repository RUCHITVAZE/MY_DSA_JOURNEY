#Instead of checking every number up to $N$, we only check up to $\sqrt{N}$. Factors always occur in pairs. 
# For example, if $N = 36$ and we find $4$, we instantly know $36 / 4 = 9$ is also a factor.
# This is a brute force attempt to find all factors of a number, but it is more efficient than checking every number up to $N$.
n = 20
num = n
result =[]
for i in range (1,num+1):
    if num%i==0:
        result.append(i)
print(result)

#better optimised Approach 
n = 10 
num = n
result =[]
for i in range (1,(num//2)+1):
    if num%i==0:
        result.append(i)
result.append(num)
print(result)

# most optimised approach
# aprroach 36 divisible by 1 result is 36 which is also factor 
#36 divisible by 2 result is 18 which is also factor
#36 divisible by 3 result is 12 which is also factor
#36 divisible by 6 result is 6 which is also factor this goes on till root of num 
result = []
n=36
num = n
from math import sqrt 
for i in range (1,int(sqrt(num))+1):
    if num%i==0:
        result.append(i)
        if num//i !=i:
            result.append(num//i)
    
print(result)  
