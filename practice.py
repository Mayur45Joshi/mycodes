# fruits = ["Apple","Carrat","Banana"]
# for x in fruits:
#     #print(x)
#     if x == "Banana":
#         break
#     print(x)


# fruits = ["Apple","Banana","Cherry"]
# for x in fruits:
#     if x == "Banana":
#         continue
#     print(x)


# for x in range(6):
#     print(x)
#
# for y in range(2,10,3):
#     print(y)

# for x in range(6):
#     if x == 3:
#         break
#     print(x)
# else:
#     print("final end")


# def my_function(Child1, Child2, Child3):
#     print("the youngest child is " + Child2)
#
# my_function(Child1 = "MJ" ,Child2 = "pt", Child3 = "kt")


# def my_function(fisrtname):
#     print(fisrtname + "lastname")
#
# my_function("mayur")
# my_function("Supu ")


# def my_function(*Kids):
#     print("The Youngest child is : " + Kids[0])
#
# my_function("may","june","july")


# def my_function(child3, child2, child1):
#     print("The youngest child is " + child1)
#
# my_function(child1="mj", child2="kh", child3="ty")


# def my_function(**Kids):
#     print("the last name " + Kids["lname"])
# my_function(lname= " joshi ")


# def my_function(country = "India"):
#     print("I am from " + country)
#
# my_function("Norway")
# my_function()


# def my_function(food):
#     for x in food:
#         print(x)
#
# fruits=["apple", "mango", "banana"]
#
# my_function(fruits)


# def my_function(x):
#     return 5 * x
#
# print(my_function(3))



# def are_anagrams(str1, str2):
#   return sorted(str1) == sorted(str2)
#
# string1 = input("Enter the first string: ")
# string2 = input("Enter the second string: ")
# if are_anagrams(string1, string2):
#   print("Anagrams")
# else:
#   print("Not anagrams")


# lst = [1]
# if not lst:
#   print("List is empty")
# else:
#   print("List is not empty")


# base = float(input("Enter the base: "))
# exponent = float(input("Enter the exponent: "))
# power_result = base ** exponent
# print("Result:", power_result)


# Find the length of the longest word in a given sentence.
# # Explanation
# sentence = input("Enter a sentence: ")
# words = sentence.split()
# max_length = max(len(word) for word in words)
# print("Length of the longest word:", max_length)


# def is_perfect_square(num):
#   return int(num**0.5)**2 == num
#
# num = int(input("Enter a number: "))
# if is_perfect_square(num):
#   print("Perfect square")
# else:
#   print("Not a perfect square")


#Find the common elements between two lists.

# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# common_elements = list(set(list1) & set(list2))
# print("Common elements:", common_elements)


# # Fiboncci series
# def fibonacci(n):
#   fib_seq = [0, 1]
#   while len(fib_seq) < n:
#     fib_seq.append(fib_seq[-1] + fib_seq[-2])
#   return fib_seq
#
# num_terms = int(input("Enter the number of terms: "))
# fibonacci_seq = fibonacci(num_terms)
# print("Fibonacci sequence:", fibonacci_seq)


#print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

# import sys
# print(sys.version_info)

# from math import pi
# r=float(input("entere radius "))
# area = pi * r ** 2
# print(area)


# fn=input("Enter the first name:")
# sn=input("Enter second name:")
# print(sn + " " + fn )


# values=input("Enter numbers:")
# list=values.split(",")
# print(list)
# print(tuple(list))


# nm=input("Enter file name:")
# slit_file=nm.split(".")
# print(slit_file[1])


# color_list=["Red","Green","White" ,"Black"]
# print(color_list[0], color_list[-1])


# n=input("Emter any value for n")
# print(n+(n*n)+(n*n*n))


# def calculate_n_value(n):
#     str_n= str(n)
#     nn = int(str_n*2)
#     nnn = int(str_n*3)
#     total=n+nn+nnn
#     return total
#
# n=int(input("Enter n value :"))
# result=calculate_n_value(n)
# print(result)


# print(len.__doc__)
# print(sorted.__doc__)
# print(abs.__doc__)


# #calander o/p
# import calendar
# y=int(input("Enter Year"))
# m=int(input("Enter Month"))
#
# print(calendar.month(y,m))


# #use 3 commas for multiline comment
# print("""
# a string that you "don't" have to escape
# This
# is a  ....... multi-line
# heredoc string --------> example
# """)


# #no of days between 2 dates
# from datetime import date
#
# f_date=date(1,1,1)
# l_date=date(9999,12,31)
#
# delta=l_date-f_date
# print(delta.days)


# #Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.
#
# n=int(input("Enter any number:"))
# def comparison():
#     if n > 17:
#         print(2*(n-17))
#     else:
#         print(n-17)
# comparison()


##Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.
# a=int(input("Enter first value"))
# b=int(input("Entere second no"))
# c=int(input("Entere third no"))
#
# def compare():
#     if a==b==c:
#         print(3*(a+b+c))
#
#     else:
#         print(a+b+c)
#
# compare()


# # #Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is"
# string_1=(input("Enter any string"))
#
# def stringmatch(text):
#     if len(text)>=2 and text[:2]== "Is":
#         return text
#
#     else:
#         return "Is" + text
#
# print(stringmatch(string_1))


#Write a Python program that returns a string that is n (non-negative integer) copies of a given string.
# def string_repeat(text,n):
#     result=""
#
#     for i in range(n):
#
#         result=result + text
#
#     return result
#
# print(string_repeat("abc",2))
# print(string_repeat("Mayur",10))


# #22. Write a Python program to count the number 4 in a given list.
# num = input("Enter the list of values")
# nums = list(map(int,num))
# #nums = list(map(int, num.split(",")))
# def countno_4(nums):
#     count = 0
#
#     for n in nums:
#         #print(n)
#         if n == 4:
#             count = count + 1
#     return count
#
# print(countno_4(nums))



# #Prompt the user to enter a number and convert the input to an integer
# n=int(input("enter any number"))
# mod=n%2
# if mod>0:
#     print("Odd no")
#
# else:
#     print("even no")


# char = input("enter any character")
# def is_vowel(char):
#     vowels = ("aeiouAEIOU")
#     if char in vowels:
#         print("It is vowel")
#     else:
#         print("Not vowel")
#
# is_vowel(char)


# char = input("enter any character")
# def is_vowel():
#     vowels = ("aeiouAEIOU")
#     for ch in char:
#         if ch in vowels:
#             print("It is vowel")
#         else:
#             print("Not vowel")
#
# is_vowel()


# #pattern print
# def patter_len():
#     pattern_type = [1,2,3,4,5,4,3,2,1]
#     for pattern in pattern_type:
#         print('$' * pattern)
#
# patter_len()



# #pattern print
# n= int(input("enter any no"))
# for i in range(1,n+1):
#     print("()" * i)



# #program to print all even numbers from a given list of numbers in the same order and stop printing any after 237 in the sequence
# data= input("enter the list of values")
# nums = list(map(int,data.split()))
# for d in nums:
#
#     if d == 4:
#         break
#     elif d % 2 == 0:
#        print(d)


# #    interview question    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# driver=webdriver.Chrome()
#
# driver.get("https://designli.co/blog/5-great-web-application-examples/")
# driver.maximize_window()
# # ele=driver.find_element(By.XPATH,"//div[@class='logo-standard']//img[@title='Designli']")
# #
# # driver.implicitly_wait(10)
#
# actions=ActionChains(driver)
# #actions.move_to_element(ele).perform()
# # txt=ele.text
# # print(txt)
# # print(ele.get_attribute("title"))
# # print(ele.get_attribute("text-content"))
# # time.sleep(10)
#
#
# arrow=driver.find_element(By.XPATH,"//a[@id='return-to-top']//i")
# # actions.scroll_to_element(arrow)
# #time.sleep(10)
# # actions=ActionChains(driver).move_to_element(arrow)
# # time.sleep(10)
# actions.scroll_to_element(arrow).click()
# time.sleep(10)


##interation
# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self
#
#   def __next__(self):
#     x = self.a
#     self.a += 1
#     return x
#
# myclass = MyNumbers()
# myiter = iter(myclass)
#
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))


# #stop iteration
# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#
#     def __next__(self):
#         if self.a <= 20:
#             x = self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration
#
#
# myclass = MyNumbers()
# myiter = iter(myclass)
#
# for x in myiter:
#     print(x)



# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)


# #List Comprehension
# #List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
#
# for x in fruits:
#   if "a" in x:
#     newlist.append(x)
#
# print(newlist)



# #looping string
# thislist = ["apple" , "banana" ,"cherry"]
# i=0
# while i<len(thislist):
#     print(thislist[i])
#     i=i+1

#
# #The replace() method replaces a string with another string:
# a = "Hello, World!"
# print(a.replace("H", "J"))



# #print random no
# import random
# print(random.randrange(1, 10))



