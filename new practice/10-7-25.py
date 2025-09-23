# # shift zeros
# arr=[1,3,0,6,0,7,0,8,9]
# def shiftzero(arr):
#     zeros=[]
#     others=[]
#     for char in arr:
#         if char==0:
#             zeros.append(char)
#         else:
#             others.append(char)
#     return zeros + others
#     #return char
# print(shiftzero(arr))



# #removing white spaces
# strt="This is java program"
# new=strt.split(" ")
#
# print("".join(new))


# str=" ma yur js ohi "
# def reverse(str):
#     print(str[::-1])
#
# reverse(str)


# a=10
# b=25
# a,b=b,a
# print(a)
# print(b)

# a=10
# b=25
# a=a+b
# b=a-b
# a=a-b
# print("a:",a)
# print("b:",b)



# # reverse only first nummber
# str="Honesty is best policy"
# lst=str.split(" ")
# #print(lst[0])
# lst[0]=lst[0][::-1]
# print(" ".join(lst))


# #alternate word reverse
# sen="Honesty is best Policy"
# lst=sen.split(" ")
# #lst[0]=lst[0][::-1]
# for word in range(len(lst)):
#     if word %2==0:
#         lst[word]=lst[word][::-1]
# #print(lst0)
# print(" ".join(lst))



# # sorted string + on sorted finding second max and second min
# arr=[7,8,2,9,4,6,3]
# arr.sort()
# print(arr)
# min1=min2=float('inf')
# for num in arr:
#     if num < min1 :
#         min2=min1
#         min1=num
#     elif num < min2  and num != min1:
#         min2 = num
#
# print(min2)
#
# max1=max2=float('-inf')
# for num in arr:
#     if num > max1:
#         max2 = max1
#         max1=num
#
#     elif num > max2 and num != max1:
#         max2=num
# print(max2)



#occurancy of each nmber
# def countoccurance(str):
#
#     str="Mayur Joshi"
#     char_count={}
#     for char in str:
#         if char in char_count:
#             char_count[char]+=1
#
#         else:
#             char_count[char]=1
#     return  char_count
# print(countoccurance(str))


# # Remove negative numbers from string or list
# a=[2,-3,-2,3,5,-6,1,0,-6,1,4,6]
# def remove_neg(a):
#
#     for num in a[:]:
#         if num < 0:
#             a.remove(num)
#         elif num >= 0:
#             print(num)
#
#     return num
# remove_neg(a)

#another way of above program
# a=[2,-3,-2,3,5,-6,1,0,-6,1,4,6]
# def remove_neg(a):
#     for num in a:
#         if num >= 0:
#             pass
#     return [num for num in a if num >=0]
#
# print(remove_neg(a))


# a=[2,-3,-2,3,5,-6,1,0,-6,1,4,6]
# def remove_neg(a):
#     result=[]
#     for num in a:
#         if num >=0:
#             result.append(num)
#     return result
#
# print(remove_neg(a))


#a = "123abc345def435ghi"
#output = 123cba345fed45ihg
# import re
# a = "123abc345def435ghi"
# # Find all sequences of letters (non-digits) and numbers
# matches = re.findall(r'(\d+|\D+)', a)
# result = ""
# for group in matches:
#     if group.isalpha():
#         result += group[::-1]
#     else:
#         result += group
# print(result)


# #another way
# a = "123abc345def435ghi"
# result = ""
# temp = ""
# for ch in a:
#     if ch.isdigit():
#         # flush the temp letters (if any) reversed
#         if temp:
#             result += temp[::-1]
#             temp = ""
#         result += ch   # keep number as is
#     else:
#         temp += ch     # collect letters
# # handle last letters block
# if temp:
#     result += temp[::-1]
# print(result)
#
#
#
# a="123abc345def435ghi789"
# result=""
# temp=""
# for char in a:
#     if char.isalpha():
#         if temp:
#             result+=temp[::-1]
#             temp=""
#         result+=char
#     else:
#         temp+=char
# if temp:
#     result+=temp[::-1]
# print(result)
#
#
#
# import re
# a = "123abc345def435ghi"
# result = "".join(map(lambda x: x if x.isdigit() else x[::-1], re.split(r'(\d+)', a)))
# print(result)

