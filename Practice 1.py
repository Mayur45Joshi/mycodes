# amount=1200
# discount=0
#
# if amount>1000:
#     discount=amount*10/100
#
# print("amount ",amount-discount)



# # amount=1000
# input("Enter amount")
# print("Amount ",amount)
#
# if amount>50000:
#     discount=amount*50/100
# elif amount>30000:
#     discount=amount*30/100
# elif amount>10000:
#     discount=amount*5.27/100
# else:
#     discount=0
# print("Final amount", amount-discount)


# # amount=1000
# amount=float(input("Enter amount"))
# print("Amount ",amount)
#
# if amount>50000:
#     discount=amount*50/100
# elif amount>30000:
#     discount=amount*30/100
# elif amount>10000:
#     discount=amount*10/100
# else:
#     discount=0
# print("Final amount", amount-discount)



# num=2
# print("Num ",num)
# if num % 2==0:
#     if num %3==0:
#         print("divisible by both")
#     print("divisible by 2")
# print("no divisble")



# num=8
#
# if num %2 == 0:
#     if num %3 == 0:
#         print("Divisble by 3")
#     else:
#         print("Divisble by 2 but not with 3")
#
# else:
#     if num %3 == 0 :
#         print("divisible by 3")
#     else:
#         print("divisble by 3 but not with 2")


#match case statement
#The last case statement in the function has "_" as the value to compare. It serves as the
# wildcard case, and will be executed if all other cases are not true.
# def weekdays(n):
#     match n:
#         case 0: return "Monaday"
#         case 1: return  "Tuesday"
#         case 2: return  "Wednesday"
#         case 3: return  "Thursday"
#         case 4: return  "Friday"
#         case 5: return  "Saturday"
#         case 6: return  "Sunday"
#         case _: return  "Invalid case"
#
# print(weekdays(0))
# print(weekdays(3))
# print(weekdays(7))



# def access (user):
#     match user:
#         case "admin" | "manager" : return "Full access"
#         case "Guest" : return "limited"
#         case _ : return  "No access"
# print(access("admin"))
# print(access("manager"))
# print(access("chi"))



# def intr(details):
#     match details:
#         case [amt,duration] if amt<10000:
#             return amt*10*duration/100
#         case [amt,duration] if amt>=1000:
#             return amt*10*duration/100
# print("Interest = ",intr([5000,5]))
# print("Interest = ",intr([15000,3]))



# numbers=(12,25,65,85,96,74,56,66,45,55,2,22,228,6,58)
# total=0
# for num in numbers:
#     total=total+num
#
# print(total)



# numbers=[10,45,78,41,52,48,63,45,74,88,220,20,62,585,47,87]
# for num in numbers:
#     if num%2 == 0:
#         print(num)



# #loop with range object
# for num in range(5):
#     print(num, end=' ')
# print()
# for num in range(10,20):
#     print(num,end=' ')
# print()
# for num in range(1,10,5):
#     print(num,end=' ')


# numbers={10:"ten",20:"twenty",30:"thirty",40:"fourty"}
# for x in numbers:
#     print(x,":",numbers[x])
#
# for x in numbers.items():
#     print(x)



# for count in range(6):
#     print("interator number {}".format(count))
# else:
#     print("for loop exists and currently in else block")
# print("end of loop")


# def positive_negative():
#     for i in [5,-1,7]:
#         if i>=0:
#             print("positive value")
#         else:
#             print("negative value")
#             break
#     else:
#         print("for loop else")
# positive_negative()


#while loop

# count=0
# while count<5:
#     count=count+1
#     print("No of iteration {}".format(count))
# print("while end")


# var=10
# while var>0:
#     print("Variable ",var)
#     var=var-1
#     if var==5:
#         break
#
# print("loop end")


# nom=33
# numbers=[10,22,44,88,33,44,77,15,89,74]
# for num in numbers:
#     if num==nom:
#         print(num)
#         print("no found")
#         #print(num)
#         break
# else:
#     print("no nt found")



# num=25
# numbers=[12,25,78,89,56,36,45,74,77,82,34]
# for n in numbers:
#     if n == num:
#         continue
#
#     print(n)



# num=20
# print("Prime factor for num", num)
# d=2
# while num>1:
#     if num%d==0:
#         print(d)
#         num=num/d
#         continue
#     d=d+1


# month=["Jan", "Feb","Mar","APR"]
# days=["Mon","Tue","Wed"]
#
# for x in month:
#     for y in days:
#         print(x,y)



# def yourfunction():
#    a = 5
#    b = 6
#    # nested function
#    def myfunction():
#       # nonlocal function
#       nonlocal a
#       nonlocal b
#       a = 10
#       b = 20
#       print("variable a:", a)
#       print("variable b:", b)
#       return a+b
#    print (myfunction())
# yourfunction()


# name = 'TutorialsPoint'
# marks = 50
# result = True
# def myfunction():
#    a = 10
#    b = 20
#    c = a+b
#    print ("globals():", globals())
#    print ("locals():", locals())
#    return c
# myfunction()



#Annotations

# def myfunction(a:int , b:int) -> int:
#     c=a+b
#     return c
# print(myfunction(56,88))
# print(myfunction.__annotations__)
#
#
# def total(x:"marks in pyh",y:"marks in chm"):
#     return x+y
# print(total(25,69))
# print(total.__annotations__)



#<<<<<<<<<<<<<<<<<Encapsulation?>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# class Desktop:
#     def __init__(self):
#         self.__max_price=25000
#     def sell(self):
#         return f"selling price: {self.__max_price}"
#     def set_max_price(self,price):
#         if price>self.__max_price:
#             self.__max_price=price
#
# destopobj=Desktop()
# print(destopobj.sell())
#
# destopobj.__max_price=35000
# print(destopobj.sell())
#
# destopobj.set_max_price(35000)
# print(destopobj.sell())


# #find duplicatss in array
# def find_duplicates(arr):
#     seen=set()
#     duplicates=set()
#
#     for num in arr:
#         if num in seen:
#             duplicates.add(num)
#         seen.add(num)
#     print(list(duplicates))
#
# find_duplicates([1,2,2,6,3,5,5,8,9,6,5,6,4,8,8,1])


#reverse string  method 1 with sring slicing
#method 1
# def reverse_str(s):
#     return s[::-1]
#
# print(reverse_str("Mayur"))

#method 2
#
# def reverse_string(s):
#     return "".join(reversed(s))
#
# print(reverse_string("Mayur"))


# #method 3 by loop
# def reverse_str(s):
#     reversed_str=""
#     for char in s:
#         reversed_str=char+reversed_str
#     return reversed_str
#
# print(reverse_str("joshi"))


#second largest number in list find out

# a=[10,25,68,74,99,40]
# max1=max2=(float('-inf'))
#
# for n in a:
#     if n>max1:
#         max2=max1
#         max1=n
#
#     elif n>max2 and n!= max1:
#         max2=n
# print(max2)



#   MAP IN python Example
# def square(x):
#     return x ** 2
#
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = list(map(square, numbers))
# print(squared_numbers)
# # Output: [1, 4, 9, 16, 25]


# num1=int(input("enter 1 no "))
# num2=int(input("enter 2 no "))
# num3=int(input("enter 3 no "))
#
# if num1 > num2 and num1 > num3:
#     print(f"num1 is large , {num1}")
# elif num2 > num1 and num2>num3:
#     print(f"num2 is large , {num2}")
# elif num3 > num1 and num3> num2:
#     print(f"num3 is large , {num3}")


# num= int(input("enter any number"))
# s = num %10
# m = num/10
# print (s)
# print(m)


# if num %2 ==0:
#     print("e")
# elif num%2 !=0:
#     print("0")



#Sort a List in Ascending Order Without using an Extra Variable

# l1=[76,25,69,63,47,60]
# print("Originnal list",l1)
#
# for i in range(0,len(l1)):
#     for j in range(i+1,len(l1)):
#         if l1[i] > l1[j]:
#             l1[i],l1[j]=l1[j],l1[i]
#
# print("sorted list",l1)



# #to count the number of occurence in string
# def countfun(s,c):
#
#     count=0
#     for char in s:
#         if char==c:
#             count=count+1
#     return count
# print(countfun("MAyurjoshihfgjshgfjsh","M"))


# #to swap numbers
# a=int(input("entrer any numbers "))
# b=int(input("entrer any numbers "))
#
# a=a+b
# b=a-b
# a=a-b
#
# print(a)
# print(b)


# #reverse the numbers
# n = 123
# rev = 0
# while n > 0:
#     rem = n % 10
#     rev = rev * 10 + rem
#     n = n // 10
# print("Reversed number:", rev)


