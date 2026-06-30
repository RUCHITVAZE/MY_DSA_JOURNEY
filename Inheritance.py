# parent class
class Car:  
    @staticmethod
    def start():
        print("Car is started")
    
    @staticmethod
    def stop():
        print("Car is stopped")
#child class
class BmwCar(Car):
    def __init__(self,brand):
        self.brand = brand

class M3(BmwCar):
    def __init__(self,model):
        self.model = model

car1 = M3("diesel")
#multilevel Inheritance
car1.start()   

# car1 = BmwCar("M3") 
# car2 = BmwCar("M4") 
# single inheritance    
# print(car1.start())
# print(car2.stop())

# multiple imheritance 
class A:
    varA = "welcome to class A"
class B:
    varB = "welcome to class B"
class C(A,B):
    varC = "welcome to class c"

c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)