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

# for y in range(2,10,3):
#     print(y)

# for x in range(6):
#     if x == 3:
#         break
#     print(x)
#     else:
#         print("final end")


# def my_function(Child1, Child2, Child3):
#     print("the youngest child is " + Child2)
#
# my_function(Child1 = "MJ" ,Child2 = "pt", Child3 = "kt")



# def my_function(fisrtname):
#     print(fisrtname + "lastname")
#
# my_function("mayur")
# my_function("Puja ")


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



# #Input is Mayur Joshi And I want to reverse only mayur and full string in output
# input_string = input("Enter a string: ")
# first_name = input_string.split()[0][::-1]
# print(first_name + " "+ input_string.split()[1])


# #Program to reverse only first and last character of the word and same login works for List also
# def reverse_first_last(word):
#   if len(word) > 1:
#     return word[-1] + word[1:-1] + word[0]
#   else:
#     return word
# input_word = input("Enter a word: ")
# print("Word with first and last characters reversed: ", reverse_first_last(input_word))


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


#?????????????????????????????????????????????????????????????

# #Given a string, reverse each word in the string and replace spaces with the % character. The order of the words should be maintained, but the characters within each word should be reversed..
#
# str=input("enter any sentense").split(" ")
# new_str=[]
# for char in str:
#
#     new_str.append(char[::-1])
#     res="%".join(new_str)
#
# print(res)