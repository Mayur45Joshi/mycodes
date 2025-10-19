# a = "abcd"
# b = "defg"
# result=""
# for char in a+b:
#     if char not in "d":
#         result+=char
# print(result)



# Str="Python is good"
#
# lst=Str.split()
# for char in lst:
#     print(char[::-1])


# L = [(9, 'a', 5), (3, 'x', 8), (7, 'g', 2)]
# sorted_ind=sorted(L, key=lambda x : x[-1])
# print(sorted_ind)



# #swapping first and last items in list
# arr1="mayur joshi"
# arr=list(arr1)
# def swap_str(arr):
#     arr[0],arr[-1] = arr[-1],arr[0]
#     return "".join(arr)
# print(swap_str(arr))


# #swapping first and last items in list
# arr1="mayur joshi"
# arr=arr1.split()
# def swap_str(arr):
#     arr[0],arr[-1] = arr[-1],arr[0]
#     return "".join(arr)
# print(swap_str(arr))


# arr1="mayur joshi"
# arr=arr1.split()
# result=[]
# def swap_str(arr):
#     for char in arr:
#         if len(arr)>1:
#             swapped= char[-1] + char[1:-1] + char[0]
#         else:
#             swapped=char
#         result.append(swapped)
#     return result
#
# print(swap_str(arr))