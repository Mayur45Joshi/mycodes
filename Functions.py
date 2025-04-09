# Functions  in python

#
# def desiganation():
#     print("My name is Mayur")
#
#
# def desig(name):
#     print("Hello " + name)
#
#
# def sum(a, b):
#     return (a+b)
#
#
# desiganation()
# desig('mayur')
# print(sum(2, 3))



# def my_function(value):
#     return value*5
#
# print(my_function(3))
# print(my_function(5))
# print(my_function(8))


# The __str__() Function
# The __str__() function controls what should be returned when the class object is represented as a string.
# If the __str__() function is not set, the string representation of the object is returned:


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
#   def __str__(self):
#     return f"{self.name}({self.age})"
#
# p1 = Person("John", 36)
#
# print(p1)



# # Object Methods
# # Objects can also contain methods. Methods in objects are functions that belong to the object.
# # Let us create a method in the Person class:
# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def my_func(self):
#         print("my name is "+self.name, self.age)
#
# p1=person("john",36)
# p1.my_func()
# #You can modify properties on objects like this:
# p1.age=40
# print(p1.age)



#Note: The self parameter is a reference to the current instance of the class, and is used to access variables
# that belong to the class.




#The self parameter is a reference to the current instance of the class, and is used to access variables
# that belong to the class. It does not have to be named self,
# you can call it whatever you like, but it has to be the first parameter of any function in the class:
# class Person:
#   def __init__(mysillyobject, name, age):
#     mysillyobject.name = name
#     mysillyobject.age = age
#
#   def myfunc(abc):
#     print("Hello my name is " + abc.name)
#
# p1 = Person("John", 36)
# p1.myfunc()



