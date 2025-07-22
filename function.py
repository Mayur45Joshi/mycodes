#local scope of variable
# def myfunc():
#   x = 300
#   print(x)
#
# myfunc()


# #function inside function
#
# def myfunc():
#     x=300
#     def myinnerfunc():
#         print(x)
#     myinnerfunc()
# myfunc()



# #global scope
#
# x=300
# def myfunc():
#     print(x)
#
# myfunc()
# print(x)



#naming variable

# x=300
# def myfunc():
#     x=200
#     print(x)
#
# myfunc()
# print(x)


# #global variable
#
# x=200
# def myfunc():
#     global x
#     x=300
#
# myfunc()
# print(x)



# #nonlocal variable
#
# def myfunc1():
#     x="june"
#     def myfunc2():
#         nonlocal x
#         x="hello"
#     myfunc2()
#     return x
# print(myfunc1())


import datetime
x=datetime.datetime.now()
print(x)
print(x.year)
print(x.month)
#The date contains year, month, day, hour, minute, second, and microsecond.



