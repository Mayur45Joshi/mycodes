# #1>Find most frequent repeate element in a list>
# def most_fre(List):
#     counter=0
#     #num=List[0]
#     for i in List :
#         curr_freq=List.count(i)
#         if curr_freq > counter:
#             counter=curr_freq
#             num=i
#     return num,counter
#
# # List=[1,2,2,4,2,2,2,2,8,5,9]
# List="55788888888961212121111111111111111111"
# print(most_fre(List))


# #2>>Finding All Elements with Their Frequencies:
# from collections import Counter
# def find_frequencies(arr):
#     freq=Counter(arr)
#     return dict(freq)
#
# arr=[1,1,1,2,2,3,3,8,8,9,9,6,6,4,4]
# print(find_frequencies(arr))



# #3>>>alternate word reverse
# def reversealtnum(sen):
#     trans_word = []
#     words = sen.split()
#     for i in range(len(words)):
#         if i % 2 == 0:
#             trans_word.append(words[i][::-1])
#         else:
#             trans_word.append(words[i])
#     return " ".join(trans_word)
# sen = "Mayur joshi is good boy"
# print(reversealtnum(sen))


#4>>> first non repeating charcter
# def nonrepeate(str):
#     char_count = {}
#     for char in str:
#         if char in char_count:
#             char_count[char]+=1
#         else:
#             char_count[char]=1
#     print(char_count)
#     for char in str:
#         if char_count[char]==1:
#             return char
# str="aaabbfddhh"
# print(nonrepeate(str))



##all repeting char and count
# my_list = [1, 2, 7, 8, 7, 8, 9, 7]
# frequency_map = {}
#
# for element in my_list:
#     if element in frequency_map:
#         frequency_map[element] += 1
#     else:
#         frequency_map[element] = 1
#
# print("Repeating elements and their frequencies:")
# for element, count in frequency_map.items():
#     if count > 1:
#         print(f"Element: {element}, Frequency: {count}")



#5>>>>o/p=a2b3c4d5
# def charcount(strt):
#     char_count = {}
#     result = ""
#     for char in strt:
#         if char in char_count:
#             char_count[char] += 1
#         else:
#             char_count[char] = 1
#     for char, count in char_count.items():
#         result += char + str(count)
#
#     return result
# strt = "aabbbccccddddd"
# print(charcount(strt))



# #6>>>occurancy of each nmber
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


# #7>>>>count words in sentence>>>>>>...
# def count_words(sen):
#     word_count={}
#     words=sen.split(" ")
#     print("total words :",len(words))
#     #print(Counter(words))
#     for word in words:
#         if word not in word_count:
#             word_count[word]=1
#         else:
#             word_count[word]+=1
#     return word_count
# print(count_words("mayur joshi"))


#8>>>>Input: "Automation"
# Output: "2u22m22i2n"
# def char_count(strt):
#     result=""
#     low_c=strt.lower()
#     for char in low_c:
#         counts=low_c.count(char)
#         if counts>1:
#             result+=str(counts)
#         else:
#             result+=char
#     return result
# print(char_count("Automation"))



#a = "123abc345def435ghi"
#output = 123cba345fed45ihg
import re

a = "123abc345def435ghi"
# Find all sequences of letters (non-digits) and numbers
matches = re.findall(r'(\d+|\D+)', a)
result = ""
for group in matches:
    if group.isalpha():
        result += group[::-1]
    else:
        result += group
print(result)


#another way
a = "123abc345def435ghi"
result = ""
temp = ""
for ch in a:
    if ch.isdigit():
        # flush the temp letters (if any) reversed
        if temp:
            result += temp[::-1]
            temp = ""
        result += ch   # keep number as is
    else:
        temp += ch     # collect letters
# handle last letters block
if temp:
    result += temp[::-1]
print(result)


import re
a = "123abc345def435ghi"
result = "".join(map(lambda x: x if x.isdigit() else x[::-1], re.split(r'(\d+)', a)))
print(result)



