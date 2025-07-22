#class and object concept
# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def display_info(self):
#         print(f"person: {self.name} , age: {self.age}")
#
# p1=person("mayur",34)
# p1.display_info()



# #encapsulation
# class bankaccount:
#     def __init__(self,balance):
#         self.__balance=balance
#
#     def deposit(self,amount):
#         self.__balance+= amount
#
#     def get_balance(self):
#         return self.__balance
#
# s1=bankaccount(2000)
# s1.deposit(200)
# print(s1.get_balance())


# #inheritance
# class Animal:
#     def sound(self):
#         print("Animal makes sound")
# class Dog(Animal):
#     def bark(self):
#         print("dog barks")
# d=Dog()
# d.sound()
# d.bark()


# #polymorphism
# class bird:
#     def speak(self):
#         print("bird speak")
# class human:
#     def speak(self):
#         print("human speak")
# def make_sound(mj):
#     mj.speak()
#
# make_sound(bird())
# make_sound(human())


# #abstraction
# from abc import ABC,abstractmethod
# class shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class square(shape):
#     def __init__(self,side):
#         self.side=side
#     def area(self):
#         return self.side * self.side
# s1=square(4)
# print(s1.area())


# #combo of all
# from abc import ABC,abstractmethod
# class person(ABC):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     @abstractmethod
#     def showinfo(self):
#         pass
#
#
# class student(person):
#     def __init__(self,name,age,studentid):
#         super.__init__(name,age)
#         self.studentid=studentid
#         self.__marks={}
#
#     def addmarks(self,subject,mark):
#         self.__marks[subject]=mark
#
#     def get_marks(self):
#         return self.__marks
#
#     def showinfo(self):
#         print(f"Student name:{self.name},age:{self.age},id:{self.studentid}")
#         print("marks:",self.__marks)
#
# class teacher(person):
#     def __init__(self,name,age,subject):
#         super().__init__(name,age)
#         self.subject=subject
#
#     def showinfo(self):
#         print(f"Teacher name : {self.name},age:{self.age},subject:{self.subject}")
#
# def main():
#     s1=student("mayur",25,455)
#     s1.addmarks("math",25)
#
#     t1=teacher("joshi",25,"maths")
#
#     peoples=[s1,t1]
#     for person in peoples:
#         person.showinfo()
#         print("-",* 30)
#
#     print(s1.get_marks())
#
# main()