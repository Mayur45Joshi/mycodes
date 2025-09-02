# #reverse string
# def rev_string(s):
#     rev_str=""
#     for char in s:
#         rev_str=char+rev_str
#
#     return rev_str
#
# print(rev_string("mayur"))



# str=input("enter any string")
# def rev_string(str):
#     return str[::-1]
#
# print(rev_string(str))

# def rev_string(s):
#     return "".join(reversed(s))
#
# print(rev_string("mayur"))


# #second largest number
#
# s=[10,25,36,78,96,70]
# max1=max2=(float('-inf'))
# min1=min2=float('inf')
# for num in s:
#     if num>max1:
#         max2=max1
#         max1=num
#     elif num>max2 and num != max1:
#         max2=num
#
# print(max2)
#
# for num in s:
#     if num<min1:
#         min2=min1
#         min1=num
#     elif num <min2 and num != min1:
#         min2=num
# print(min2)


#squring numbers using MAp function

# def square_num(x):
#     return x**2
# numbers=[1,2,3,4,5]
#
# squred_num=list(map(square_num,numbers))
# print(squred_num)


# def remove_duplicates(s):
#     seen = set()
#     result = []
#     for char in s:
#         if char not in seen:
#             result.append(char)
#             seen.add(char)
#     return ''.join(result)
#
# print(remove_duplicates("mahhmawr"))


# #squaring only even numbers
# inp = [1, 4, 3, 6, 8]
# def sqare(inp):
#     result = []
#     for char in inp:
#         if char % 2 == 0:
#             char = char * char
#             result.append(char)
#         else:
#             result.append(char)
#     return result
# print(sqare(inp))


# def squarelistcompr(inp):
#    # return [num * num if num % 2 == 0 else num for num in inp]
#     return [num**2 if num%2==0 else num for num in inp]
# inp=[1, 4, 3, 6, 8]
# print(squarelistcompr(inp))


# str="Hello World"
# print(str.replace("l","*"))
#
# s="".join(c for c in str if c !="o")
# print(s)


# #update dictionary from new dictionary
# d1 = {'x': 1, 'y': 2}
# d2 = {'x': 3, 'z': 4}
# d1.update(d2)
# print(d1)
# print(d2)
#
# #| operator introduced in Python 3.9 can be used to merge dictionaries. It creates a
# # new dictionary without modifying the original dictionary.
# d1 = {'x': 1, 'y': 2}
# d2 = {'y': 3, 'z': 4}
# d3 = d1 | d2
# print(d3)
# print(d1)
# print(d2)


# #reading data in txt file
# with open (r"D:\STUDY AUTO\files\aim.txt","r") as file:
#     content=file.read()
#     print(content)


# #reading data line in a file one at a time
# with open (r"D:\STUDY AUTO\files\aim.txt","r") as file:
#     line=file.readline()
#     while line:
#         print(line,end='')
#         line=file.readline()


# #reading data lines in a file all at a time
# with open (r"D:\STUDY AUTO\files\python.txt","r") as file:
#     lines=file.readlines()
#     for line in lines:
#         print(line,end='')




# with open("new 2"
#           ".txt", "w") as file:
#    file.write("Hello, World!")
#    print ("Content added Successfully!!")