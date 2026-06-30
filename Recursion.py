# print ruchit 4 times 

count =0 
def print_ruchit():
    global count
    if count<4:
        count+=1
        print_ruchit()
        print("ruchit")
    
print_ruchit()

