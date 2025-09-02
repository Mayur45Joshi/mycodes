
# #print even numbers with lambada and filter
# nums=[1, 2, 3, 4, 5, 6]
# eve_nums=list(filter(lambda x: x%2==0,nums))
# print(eve_nums)


# nums=[5]
# add=lambda x: x+15
# mulit=lambda x: x*15
# mul=lambda  x,y: x*y
# print(add(nums[0]))
# print(mulit(nums[0]))
# print(mul(5,6))


# def lambadatest(n):
#     return lambda x : x*n
# result=lambadatest(4)
# print(result(5))
#
#
# result1=lambda x, unknown_no:x * unknown_no
# print(result1(4,9))


# #tuple sorting lambada
#
# x=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# x.sort(key=lambda x:x[1])
# print(x)


# #Dictionary Sorting Lambda
# x=[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
# #x.sort(key=lambda x : int(x['model']))
# x.sort(key=lambda x : x['make'])
#
# print(x)


# #even odd filter
# x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even=list(filter(lambda x: x%2==0,x))
# odd=list(filter(lambda  x: x%2!=0 , x))
# print(even)
# print(odd)


# #square and cube of a list
# x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# square=list(map(lambda x: x**2,x))
# cube=list(map(lambda x: x**3, x))
# print(square)
# print(cube)



# #string start with check
#
# #string=lambda x: True if x.startswith("P") else False
# string=lambda x: x.startswith("P")
# print(string("mayur"))
# print(string("Python"))


# import datetime
# curr_t=datetime.datetime.now()
# year=lambda x: x.year
# month=lambda x: x.month
# day=lambda x: x.day
# t=lambda x: x.time
# print(year(curr_t))
# print(month(curr_t))
# print(day(curr_t))
# print(t(curr_t))






