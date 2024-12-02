# class person:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
#
# p1 = person("John" , 45)
# print(p1)
# print(p1.name)
# print(p1.age)


import self


# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname
#
#   def printname(self):
#     print(self.firstname, self.lastname)
#
# #Use the Person class to create an object, and then execute the printname method:
#
# x = Person("John", "Doe")
# x.printname()

#>>>>>>>>>>>>>>>>>>or >>>>>>>>>>>>>>>>>

# class Person:
#     def printname(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
#         print(self.firstname, self.lastname)
#
# # Create an object and call the printname method
# x = Person()
# x.printname("John", "Doe")
#
# class Student(Person):
#     def __init__(self, fname, lname):
#         Person.__init__(self, fname, lname)
#
# y=Student()
# y.printname("Mayur" , "Joshi")


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.



# class Person:
#     def __init__(self, fname , lname):
#         self.firstname=fname
#         self.lastname=lname
#
#     def printname(self):
#         print(self.firstname, self.lastname)
#
# class Student(Person):
#     def __init__(self, fname, lname, year):
#         super().__init__(fname, lname)
#         self.graduationyear= year
#
#     def welcome(self):
#         print("Hi" , self.firstname , self.lastname , "Welcome to the class of year " , self.graduationyear)
# x = Student("MAyur", "Joshi", 2019)
#
# print(x.graduationyear)
# x.welcome()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#iterations and stop iteration

# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self
#
#   def __next__(self):
#     if self.a <= 20:
#       x = self.a
#       self.a += 1
#       #self.a = self.a + 1
#       return x
#     else:
#       raise StopIteration
#
# myclass = MyNumbers()
# myiter = iter(myclass)
#
# for x in myiter:
#   print(x)


#3333333333333333333333333333333333333
#Inheritance Class Polymorphism

# class vechicle:
#   def __init__(self, company, model):
#     self.company = company
#     self.model = model
#
#   def move(self):
#     print("move")
#
# class car(vechicle):
#   pass
#
# class boat(vechicle):
#   def move(self):
#     print("sail")
#
#
# class plan(vechicle):
#   def move(self):
#     print("fly")
#
#
# car1 = car("tata", "altroz")
# boat1 = boat("ship", "shipmodel")
# plan1 = plan("plan", "planmodel")
#
# for x in (car1, boat1, plan1):
#   print(x.company)
#   print(x.model)
#   x.move()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#function inside function
#local variable
# def fun():
#     x=100
#     def innerfun():
#         print("inner" ,x)
#     innerfun()
# fun()

#local variable

# x = 300
# def fun():
#     print(x)
# fun()
# print(x)



# x = 300
# def fun():
#     x=200
#     print(x)
# fun()
# print(x)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>inbuilding math functions

# x = min(10,100,50)
# y = max(100,89,87)
# print(x)
# print(y)
#
# #The abs() function returns the absolute (positive) value of the specified number:
#
# x= abs(-7.25)
# print(x)



# x=200
# def myfun():
#     global x
#     x=300
#
# myfun()
# print(x)


# def myfunc1():
#   x = "Jane"
#   def myfunc2():
#     nonlocal x
#     x = "hello"
#   myfunc2()
#   return x
#
# print(myfunc1())


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Date and time

# import datetime
#
# x = datetime.datetime.now()
# print(x)
# print(x.year)
# print(x.day)
# print(x.month)

# #To create a date, we can use the datetime() class (constructor) of the datetime module.
# import datetime
# x=datetime.datetime(2024,10,24)
# print(x)



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# import datetime
#
# x = datetime.datetime(2018, 6, 1)
#
# print(x.strftime("%B"))

#>>>>>>>>>>>>>>>>>>>>>>>>>>>inbuilding math functions

# x = min(10,100,50)
# y = max(100,89,87)
# print(x)
# print(y)
#
# #The abs() function returns the absolute (positive) value of the specified number:
#
# x= abs(-1.02225)
# print(x)
#
# #The pow(x, y) function returns the value of x to the power of y (xy).
#
# x = pow(4, 3)
#
# print(x)