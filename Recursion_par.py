def func(x:int,n:int):
    if n==0:
        return
    print(x)
    func(x,n-1)
    
# func(15,5)

# print 1 to n using recursion
def fun(i,n):
    if i>n:
        return
    print(i)
    fun(i+1,n)
# fun(1,4)

# print 1 to n using backtracking 
def funct(i,n):
    if i>n:
        return
    funct(i+1,n)
    print(i)
# funct(1,4)

# sum n natural number 
def summer(sum,i,n):
    if i>n:
        print(sum)
        return
    summer(sum+i,i+1,n)
    
summer(0,1,4)
    

