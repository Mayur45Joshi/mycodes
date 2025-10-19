# from array import array
#
# arr=array('i',[10,20,30])
# arr.append(40)
# print(arr)


#duplicate print and count
# def duplicate_c(arr):
#     char_count={}
#     duplicate={}
#     for char in arr:
#         if char in char_count:
#             char_count[char]+=1
#             duplicate[char] = char_count[char]
#         else:
#             char_count[char]=1
#     return duplicate
# print(duplicate_c("ghyrtyrtyryr"))


# #leap yesar check
# def leap_y(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         print("leap year")
#     else:
#         print("no leap")
# leap_y(2001)


# ##identify missing no in sequensce
# def missing_num(arr):
#     arr.sort()
#     for i in range(len(arr)-1):
#         if arr[i+1] - arr[i] != 1:
#             return arr[i]+1
#
#     return none
# #print(missing_num([1,2,3,5]))
# print(missing_num([11,12,14,16]))


# #missing multiple nubers
# def missing_mul(arr):
#     missing=[]
#     arr.sort()
#     for i in range(len(arr)-1):
#         gap=arr[i+1]-arr[i]
#         if gap > 1:
#             missing.extend(range(arr[i]+1,arr[i+1]))
#     return missing
#
# print(missing_mul([10,11,14,19]))


# #numbers reverse
# arr=[12,23,45,89]
# for num in arr:
#     print(str(num)[::-1])



# #armstrong number check
# def is_armstrong(num):
#     digits = str(num)
#     power = len(digits)
#     total = sum(int(digit) ** power for digit in digits)
#     return total == num
#
#
# num = int(input("Enter any number: "))
# if is_armstrong(num):
#     print(f"{num} is an Armstrong number.")
# else:
#     print(f"{num} is not an Armstrong number.")



# #count no of digtis in number
# num="564645545gfhfhf46531"
# count=0
# for char in num:
#     count=count+1
# print(count)


# #print double word from each char
# Str="Mayur"
# double=[]
# for char in Str:
#     double.append(char + char)
# print(double)
#
# double1="".join(char + char for char in Str)
# print(double1)

# Str="Mayur"
# double=[]
# for char in Str:
#     double.append(char*10)
# print(double)


# str1="mayur"
# str2="joshi"
# str1 ,str2= str2 ,str1
# print("after swapping str1 =",str1)
# print("after swapping str2 =",str2)


# Str="aBACbcEDed"
# small=[]
# big=[]
# for char in Str:
#     if char.islower():
#         small.append(char)
#     else:
#         big.append(char)
# small_str="".join(small)
# s_count=len(small_str)
# big_str="".join(big)
# b_count=len(big_str)
# print(small_str,s_count,big_str,b_count)



#
# Str="Subbu123raj"
# digits=[]
# letters=[]
# for char in Str:
#     if char.isalpha():
#         letters.append(char)
#     elif char.isdigit():
#         digits.append(char)
# dig="".join(digits)
# let="".join(letters)
# print("digits",dig)
# print("letters",let)
# print(let+dig)


# ##prime numbers between 1 to 1000
# def is_prime(n):
#     if n<=1:
#         return False
#     if n==2:
#         return True
#     if n%2==0:
#         return False
#
#     for i in range(3, int(n**0.5)+1,2):
#         if n%i==0:
#             return False
#     return True
#
# primes=[num for num in range(1,1001) if is_prime(num)]
# print(primes)


# #sorting without inbuld method
# temp = [10, 22, 432, 23, 56, 76, 0, 1]
# # Bubble Sort
# for i in range(len(temp)):
#     for j in range(0, len(temp) - i - 1):
#         if temp[j] > temp[j + 1]:
#             temp[j], temp[j + 1] = temp[j + 1], temp[j]
#
# print("Sorted Array in Ascending Order:", temp)
#
#
# temp = [10, 22, 432, 23, 56, 76, 0, 1]
#
# n = len(temp)
# for i in range(n):
#     min_index = i
#     for j in range(i+1, n):
#         if temp[j] < temp[min_index]:
#             min_index = j
#     # swap the found minimum with element at i
#     temp[i], temp[min_index] = temp[min_index], temp[i]
#
# print("Sorted:", temp)



# input_str = "aaaabbbaabcccccd"
# #out =4a3b2a1b5c1d
# result = ""
# count = 1
# for char in range(1, len(input_str)):
#     if input_str[char] == input_str[char - 1]:
#         count += 1
#
#     else:
#         result += str(count) + input_str[char - 1]
#         count = 1
#
# result += str(count) + input_str[-1]
# print(result)


# sen = "Ravi had been saying that he had been there"
# words=sen.split()
# count={}
# for word in words:
#     if word in count:
#         count[word]+=1
#     else:
#         count[word]=1
# for word,count in count.items():
#     if count > 1:
#         print(word,count)


# inpu = "4a3b2a1b5c1d"
# result = ""
# for i in range(0, len(inpu), 2):
#     result += inpu[i+1] * int(inpu[i])
#
# print(result)


# #another way
# inpu = "4a3b2a1b5c1d"
# result = ""
# i = 0
# while i < len(inpu):
#     count = int(inpu[i])          # number part
#     char = inpu[i + 1]            # character part
#     result += char * count
#     i += 2                       # move to next number-char pair
# print(result)



# # pairs giving sum 10
# List = [2, 5, 4, 1, 12, -2, 8, 9]
# target = 10
# pairs = []
# for i in range(len(List)):
#     for j in range(i + 1, len(List)):
#         if List[i] + List[j] == target:
#             pairs.append((List[i], List[j]))
#
# print(pairs)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>Patterns>>>>>>>>>>>>>>>>>>>>>>>
# rows=5
# for i in range(rows,0,-1):
#     print(" "* (rows-i),end="")
#     print("* " * i)
# * * * * *
#  * * * *
#   * * *
#    * *
#     *

# rows=5
# for i in range(1,rows+1,1):
#     print(" " * (rows-i),end="")
#     print("* " * i)
#
#     *
#    * *
#   * * *
#  * * * *
# * * * * *

#
# rows=5
# for i in range(1,rows+1):
#     print(" " * (rows-i) + "* "*i)
#
# #another way
# rows=5
# for i in range(1,rows+1):
#     for j in range(rows-i):
#         print(" ",end="")
#     for k in range(i):
#         print("*",end="")
#     print()

#     *
#    **
#   ***
#  ****
# *****


# rows = 5
# for i in range(1, rows + 1):
#     for j in range(rows - i):
#         print(" ", end="")
#     for k in range(i):
#         print("* ", end="")
#     print()  # move to next line
#
# rows = 5
# for i in range(rows, 0, -1):
#     for j in range(rows - i):
#         print(" ", end="")
#     for k in range(i):
#         print("* ", end="")
#     print()

#     *
#    * *
#   * * *
#  * * * *
# * * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *


#
# rows=5
# for i in range(1,rows+1,1):
#     print(" " * (rows-i),end="")
#     print("* " * i)
# for i in range(rows-1,0,-1):
#     print(" "*(rows-i),end="")
#     print("* "*i)

# #another way of above
# rows = 5
# for i in range(1, rows+1):
#     for j in range(rows-i):
#         print(" ", end="")
#     for k in range(i):
#         print("* ", end="")
#     print()   # move to next line
#
# rows=5
# for i in range(rows-1,0,-1):
#     for j in range(rows-i):
#         print(" ",end="")
#     for k in range(i):
#         print("* ",end="")
#     print()


#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *



# rows=5
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


# rows=5
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print(i*j,end=" ")
#     print()
# 1
# 2 4
# 3 6 9
# 4 8 12 16
# 5 10 15 20 25



rows=5
for i in range(1,rows+1):
    for j in range(1,i+1):
        print("*",end="")
    print()

# *
# **
# ***
# ****
# *****


# rows=5
# for i in range(1,rows+1):
#     for j in  range(i-1,rows):
#         print("*",end="")
#     print()
# *****
# ****
# ***
# **
# *

# rows=5
# for i in range(1,rows+1):
#     for j in range(i,rows+1):
#         print(j,end="")
#     print()
#
# 12345
# 2345
# 345
# 45
# 5


# rows=5
# for i in range(1,rows+1):
#     for j in range(i,rows+1):
#         print(i,end="")
#     print()
#
# 11111
# 2222
# 333
# 44
# 5


# rows=5
# for i in range(1,rows+1):
#     for j in range(i):
#         print(i,end="")
#     print()
#
# 1
# 22
# 333
# 4444
# 55555


# rows = 4
# for i in range(1, rows+1):
#     for j in range(1, i+1):
#         print(str(j) * j, end="")
#     print()

# 1
# 122
# 122333
# 1223334444


# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# matrix = []
# for i in list1:
#     rows = []
#     for j in list2:
#         rows.append(i * j)
#     matrix.append(rows)
# for row in matrix:
#     print(row)