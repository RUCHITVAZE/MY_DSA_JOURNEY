
# class Car:
#     #default constructors 
#     def __init__(self):
#         pass
#     #parameterized Constructor 
#     def __init__(self,model:str,color:str):
#         print("constructor called")
#         self.model = model #obj atr
#         self.color = color #obj atr
#     brand = "BMW" # class atr 
#     # method
#     def get_model(self):
#         print(f"Your model is {self.model}")
# car1 = Car("m3","red")
# # print(car1.model)

# car2 = Car("m4","Blue")
# # print(car2.brand)

# car2.get_model()


class Student():
    @staticmethod # decorator
    def greet():
        print("Hello")
    greet()   
    def __init__(self,name,marks):
        self.name  =name
        self.marks = marks 
    def Avg_marks(self):
        avg = sum(self.marks)/len(self.marks)
        print(f"Hi {self.name} your average marks is {avg}")
s1 = Student("tony",[99,98,98])
s1.Avg_marks()
# del keyword to del atr or obj
s1 = Student("tony",[99,98,98])
print(s1.name)
del s1.name
print(s1.name)
del s1