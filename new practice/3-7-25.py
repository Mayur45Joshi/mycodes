#sum of array

# arr={4,5,0,10}
# sum=0
# for n in arr:
#     sum=n+sum
#
# print(sum)


#largest value in array

# arr={-714,25,85,96,-1040}
# larg=0
# for n in arr:
#     if n>larg:
#         larg=n
#
# print(larg)


# # #array rotate (Left Rotation by 1):
# arr=[1,2,3,4,5,6,7]
# def rotate_arr(arr):
#     return arr[1:] + arr[:1]
#
# print(rotate_arr(arr))

# def rotate_right(arr, k):
#     k = k % len(arr)
#     return arr[-k:] + arr[:-k]
# print(rotate_right([1, 2, 3, 4, 5], 2))  # Output: [4, 5, 1, 2, 3]



#array rotate alogorithm

# arr=[1,2,3,4,5,6,7]
# def roate_array(arr,d):
#     return arr[d:] + arr[:d]
#
# print(roate_array(arr,2))


# arr=[1,2,3,4,5,6,7]
# mul=1
# n=10
# for i in arr:
#     mul=mul*i
#     rem=mul%n
#     print(rem)


# #monotonic array check increasing or decresing
# arr=input("enter any array")
# def is_monotonic(arr):
#     incresing=decreasing=True
#     for i in range(len(arr)-1):
#         if arr[i]> arr[i+1]:
#             incresing=False
#         if arr[i]< arr[i+1]:
#             decreasing=False
#
#     return incresing or decreasing
# print(is_monotonic(arr))


# #swapping first and last items in list
# arr=[1,2,3,4,5,6]
# def swap_str(arr):
#     arr[0],arr[-1] = arr[-1],arr[0]
#     return arr
# print(swap_str(arr))
#
# def swap_first_last(s):
#     if len(s) <= 1:   # if string is empty or 1 char, return same
#         return s
#     return s[-1] + s[1:-1] + s[0]   # last + middle + first
# s = "mayur"
# print(swap_first_last(s))


# #Python | Find elements of a list by indices
# lst1=[12,14,45,48,48,71]
# lst2=[0,2,1,3]
#
# def indices(lst1,lst2):
#     return [lst1[i] for i in lst2]
#
# print(indices(lst1,lst2))

# #Python - Ways to find indices of value in list
# a=[1,2,7,8,7,8,9,7]
# indices=[]
# for i in range(len(a)):
#     if a[i]==7:
#         indices.append(i)
#
# print(indices)


#Find most frequent repeate element in a list
# def most_fre(List):
#     counter=0
#     #num=List[0]
#     for i in List :
#         curr_freq=List.count(i)
#         if curr_freq > counter:
#             counter=curr_freq
#             num=i
#     return num
#
# # List=[1,2,2,4,2,2,2,2,8,5,9]
# List="55788888888961212121111111111111111111"
# print(most_fre(List))


# #Finding All Elements with Their Frequencies:
# from collections import Counter
# def find_frequencies(arr):
#     freq=Counter(arr)
#     return dict(freq)
#
# arr=[1,1,1,2,2,3,3,8,8,9,9,6,6,4,4]
# print(find_frequencies(arr))


# #Given string like "abc38gh89" separate number from this string without converting into character array
# str = "afa353hg353"
# lst1 = ""
# #lst2 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# lst2="0123456789"
# for char in str:
#     if char not in lst2:
#         lst1 += char
# print(lst1)


# #Move all the zeroes to one side of array and ones to right side of array
# def zeroonefun(arr):
#     zeros=[x for x in arr if x==0]
#     ones=[x for x in arr if x==1]
#     others=[x for x in arr if x not in [1,0]]
#     return zeros + others + ones
# arr = [1, 0, 1, 2, 0, 3, 0, 4, 1]
# print(zeroonefun(arr))


# #convert string into lower without using inbuld function
# def to_lower(s):
#     result=""
#     for char in s:
#         #ord = gives askii value for charter
#         #chr = giver charte for any askii value
#         aski_val=ord(char)
#         if 65<= aski_val <=90:
#             result+= chr(aski_val+32)
#         else:
#             result += char
#     return result
# print(to_lower("MAYUR"))


# # to convert in upper cases
# def to_upper(s):
#     result = ""
#     for char in s:
#         aski_val = ord(char)
#         if 97 <= aski_val <= 122:
#             result += chr(aski_val - 32)
#         else:
#             result += char
#     return result
#
# print(to_upper("mayur"))





#
# def reverse_alterword(sentence):
#
#     words=sentence.split()
#     trasform_w=[]
#
#     for i, word in enumerate(words):
#         if i%2 != 0:
#             trasform_w.append(word[::-1])
#
#         else:
#             trasform_w.append(word)
#
#     return " ".join(trasform_w)
# print(reverse_alterword("mayur joshi is good boy"))

##another way of above
# def reversealtnum(sen):
#     trans_word = []
#     words = sen.split()
#     for i in range(len(words)):
#         if i % 2 == 0:
#             trans_word.append(words[i][::-1])
#
#         else:
#             trans_word.append(words[i])
#
#     return " ".join(trans_word)
#
#
# sen = "Mayur joshi is good boy"
# print(reversealtnum(sen))



# def nonrepeate(str):
#
#     char_count = {}
#     for char in str:
#         if char in char_count:
#             char_count[char]+=1
#
#         else:
#             char_count[char]=1
#     print(char_count)
#     for char in str:
#         if char_count[char]==1:
#             return char
# str="aaabbfddhh"
# print(nonrepeate(str))


# def nonrepeate(str):
#
#     char_count = {}
#     for char in str:
#         if char in char_count:
#             char_count[char]+=1
#
#         else:
#             char_count[char]=1
#     max_count=max(char_count.values())
#     for char,count in char_count.items():
#         if count==max_count:
#             print(char,count)
# nonrepeate("fgdgdgddd")



# import oracledb
# conn = oracledb.connect(user="C##mayur", password="joshi", dsn="localhost:1521/orcl")
# print("Connected successfully.")


# def charcount(strt):
#     char_count = {}
#     result = ""
#     for char in strt:
#         if char in char_count:
#             char_count[char] += 1
#
#         else:
#             char_count[char] = 1
#
#     for char, count in char_count.items():
#         result += char + str(count)
#
#     return result
# strt = "aabbbccccddddd"
# print(charcount(strt))