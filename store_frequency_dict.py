#method 1 tc O(n) sc=O(n)
nums =[3,4,5,6,4,5,3,6,8,6,7,9,6,4,7,6,4]
freq = {}
for i in range(0,len(nums)):
    if nums[i] in freq:
        freq[nums[i]] += 1
    else:
        freq[nums[i]] = 1
print(freq)

# methods 2 tc O(n) sc=O(n)
nums =[3,4,5,6,4,5,3,6,8,6,7,9,6,4,7,6,4]
n = len(nums)
freq = {}
for i in range(0,n):
    freq[nums[i]] = freq.get(nums[i],0)+1
    
print(freq)