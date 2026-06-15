n = 12345
num = n 
count = 0
# brute force attempt tc: O(n) 
while num >0:
    count+=1 
    num = num//10 
print(count)
# optimised approach tc O(LOG10(n))
from math import * 
def count_num(nb):
    return int(log10(nb)+1)
print(count_num(123456))
    