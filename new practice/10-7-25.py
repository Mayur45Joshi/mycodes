# shift zeros
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



# #occurancy of each nmber
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


