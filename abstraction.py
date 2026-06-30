class Car:
    def __init__(self):
        self.act = False
        self.brk = False
        self.clutch = False
        
        
    def start(self):
        self.clutch =True
        self.act =True
        # unneccesary details which are hiding 
        print("Car is started")
        
# car1 = Car()
# car1.start()



class Account:
    def __init__(self,balance:int,acc_no:int):
        self.balance = balance
        self.acc_no = acc_no
    def debit(self,amount:int):
        self.balance -= amount
        print(f"rs:{amount} was debit from your account {self.acc_no}")
        print(f"Your balance is :{self.balance}")
            
    def credit(self,amount:int):
        self.balance += amount
        print(f"rs:{amount} is credited to your account {self.acc_no}")
        print(f"Your balance is :{self.balance}")       
        
acc1  = Account(10000,1223)

acc1.credit(1000)

acc1.debit(500)