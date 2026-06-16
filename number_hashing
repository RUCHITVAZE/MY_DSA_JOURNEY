#1. Problem Statement
# Title: Count Frequencies of Elements from One Array in Another.

# Description: Given two integer arrays, n and m, find the number of times each element of array m appears in array n.
n = [5,3,5,3,6,7,8,0,3,7,2]
m =[2,4,6,42,4,6,75,4,24,2,5,2,3]

for i in m :
    count= 0
    for j in n:
        if j == i:
            count+=1
            
print(count)

#optimised approach
n = [5,3,5,3,6,7,8,0,3,7,2]
m =[2,4,6,42,4,6,75,4,24,2,5,2,3]
hash_list = [0]* 11
for num in n:
    hash_list[num]+=1

for nums in m:
    if nums <1 or nums > 10:
        print(0)
    else:
        print(hash_list[nums])


# method 3 using a dict 
freq = {}
for i in n:
    freq[i] = freq.get(i,0)+1
for j in m:
    if j in freq:
        count = freq[j]  # Get the actual frequency count from the map
    else:
        count = 0        # Element doesn't exist in 'n'
        
    print(f"Element {j} appears: {count} times")       