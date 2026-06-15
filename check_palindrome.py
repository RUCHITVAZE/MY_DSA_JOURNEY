n =  1234
num = n 
result = 0
def check_palindrome():
    global num ,result
    while num >0:
        result = result*10 + num%10
        num  = num //10    
    return result == n
print(check_palindrome())