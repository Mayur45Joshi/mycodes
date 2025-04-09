# from oppsconcept import Calculator
#
#
# class FinalSum(Calculator):
#
#     num2= 100
#
#     def __init__(self):
#         Calculator.__init__(self, 3,4,)
#
#     def FinalTotal(self):
#
#         return self.Summation() + self.num2
#
# obj= FinalSum()
#
# print(obj.FinalTotal())



from oppsconcept import person

#child class
class student(person):
    #def __init__(self,firstname,lastname):
    def __init__(self,firstname,lastname,year):
        super().__init__(firstname,lastname)
        self.year=year

    def welcome(self):
        print("Welcome " , self.firstname, self.lastname, "to the class " , self.year)


s1=student("mayur","joshi",2019)
# print(s1.my_fun())
# print(s1.year)
s1.welcome()

