# def my_generator():
#     yield 1
#     yield 2
#     yield 3
#
# gen = my_generator()
# print(next(gen))  # Output: 1
# print(next(gen))  # Output: 2
# print(next(gen))  # Output: 3


#generator with loop


# def count_up_to(n):
#     count = 1
#     while count <= n:
#         yield count
#         count += 1
#
# for num in count_up_to(5):
#     print(num)


# def fibonacci(limit):
#     a, b = 0, 1
#     while a < limit:
#         yield a
#         a, b = b, a + b
#
# for val in fibonacci(10):
#     print(val)


