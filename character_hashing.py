s ='asdfghjklsdfghjasdfasdfghasd'
q =["a","d","h","f"]
hash_list = [0]*25
for char in s:
    ascii_value = ord(char)
    index = ascii_value - 97
    hash_list[index]+=1
    
for cr in q:
    ascii_value = ord(cr)
    index = ascii_value -97
    print(F"the char '{cr}'appeared {hash_list[index]} many time in the list s")


# tc :O(N+M)  sc :O(1) since we are using a fixed size hash list of 26 characters.