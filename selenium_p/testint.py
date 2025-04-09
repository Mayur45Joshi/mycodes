# # def compress_string(input_str):
# #     result = ""
# #     count = 1
# #     for i in range(1, len(input_str)):
# #         if input_str[i] == input_str[i-1]:
# #             count += 1
# #         else:
# #             result += input_str[i-1] + str(count)
# #             count = 1
# #     result += input_str[-1] + str(count)
# #     return result
# #
# # input_str = "abacbcbccca"
# # print(compress_string(input_str))
#
#
# def count_characters(input_str):
#     char_count = {}
#     for char in input_str:
#         if char in char_count:
#             char_count[char] += 1
#         else:
#             char_count[char] = 1
#     result = ""
#     for char, count in char_count.items():
#         result += char + str(count)
#     return result
#
# input_str = "abacbcbccca"
# print(count_characters(input_str))


# input= aaabbbacfwww
# output= a3b3acfw3


# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[-4:-1])



















