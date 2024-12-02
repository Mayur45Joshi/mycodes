# Classes in Pthon no New Keyword used here to create object


"""
class Calculator:
    num=100

    #default constructor

    def __init__(self):
        print("I am calling auto constructor")

    def getData(self):
        print("I am mayur")


obj = Calculator()

print(obj.num)
obj.getData()

"""

class Calculator:

    num=100

    #default constructor

    def __init__(self , a, b):
        self.firstnumber = a
        self.secondnumber = b

    def getData(self):
        print("I am mayur")

    def Summation(self):
        return  self.firstnumber + self.secondnumber + Calculator.num


obj = Calculator(2,3)

print(obj.num)
obj.getData()
print(obj.Summation())

obj1 = Calculator(100, 200)
print(obj1.Summation())