#>>>>1>>>>reverse string
from collections import Counter


# def rev_str(str):
#     reverc = ""
#     for char in str:
#         reverc = char+reverc
#     return reverc
# str="mayur"
# print(rev_str(str))


# def rev_str(str):
#     return str[::-1]
# print(rev_str("Mayur"))


# def rev_str(str):
#     return "".join(reversed(str))
# str="mayur"
# print(rev_str(str))


#>>>>>2>>>>>>>>>>palindrom

# def palindrom(word):
#     if word==word[::-1]:
#         print("palindrom")
#     else:
#         print("no palindrom")
#
# print(palindrom("mayur"))


# def is_palindrom_Str(str):
#     return str==str[::-1]
# def is_palindrom_num(num):
#     return str(num)==str(num)[::-1]
#
# print(is_palindrom_Str("josoj"))
# print(is_palindrom_num(12321))


# #>>>3>>>>count vowels and constants in string
# def vowels_const(str):
#     vowels="aeiou"
#     const="abcdfghjklmnpqrstvwxyz"
#     vo_count=0
#     cha_count=0
#     for char in str:
#         if char in vowels:
#             vo_count+=1
#         elif char in const:
#             cha_count+=1
#     return print(f"vowels:{vo_count} , consonants:{cha_count} , total:{vo_count+cha_count}")
#
# str="mayur sjohi"
# print(vowels_const(str))


# #>>>4>>>>frequency of each character
#
# def eachchar_count(str):
#     char_count={}
#     for char in str:
#         if char != " ":
#             if char in char_count:
#                 char_count[char]+=1
#             else:
#                 char_count[char]=1
#     #return char_count
#
#     for char,count in char_count.items():
#         print(f"char:{char} , count:{count}")
# str="gfgfgfghf"
# print(eachchar_count(str))


# #>>>>5 first non repeating char >>>>>>>>>>>>>>.
# def nonrepeat(str):
#     char_count={}
#     for char in str:
#         if char in char_count:
#             char_count[char]+=1
#         else:
#             char_count[char]=1
#     print(char_count)
#
#     for char in str:
#         if char_count[char]==1:
#             print(char)
#
# str="mmddffrggtt"
# print(nonrepeat(str))


#>>>6?????remove duplicate characters

# def remove_duplicate(strs):
#     set1=set(strs)
#     str1=str(set1)
#     print(str1)
# print(remove_duplicate("mmaahfr"))

# def remove_duplicate(strs):
#     result=""
#     seen=set()
#
#     for char in strs
#         if char not in seen:
#             seen.add(char)
#             result+=char
#
#     return result
#
# strs="mamaghrgh"
# print(remove_duplicate(strs))



# #print duplicates + results also in o/p
# def duplicates(strt):
#     seen = set()
#     duplicates = set()
#     result = ""
#     for char in strt:
#         if char in seen:
#             duplicates.add(char)
#         else:
#             seen.add(char)
#             result += char
#     print("duplicates", "".join(duplicates))
#     return result
# strt = "mayurbdfsdhd"
# print("non duplicates", duplicates(strt))



# #>>>>7>>>>>check if string are anagrams
# def anagrams(str1,str2):
#
#     str1 = str1.replace(" ","").lower()
#     str2 = str2.replace(" ","").lower()
#     if sorted(str1)==sorted(str2):
#         print("angrams ")
#     else:
#         print("no angrama")
#
# str1="ruyam"
# str2="mayur"
# (anagrams(str1,str2))




# #>>>>>>>8.>>>>>>combination of string
#
# import itertools
# def permutations(str):
#     perms=itertools.permutations(str)
#     for p in perms:
#         print("".join(p))
#
# permutations("mayur")


#>>>>9>>>>> capitalize first leter of each word

# def capitalize(sen):
#
#     words=sen.split(" ")
#     capt_word = [word.capitalize() for word in words]
#     return " ".join(capt_word)
# print(capitalize("mayur joshi"))


# def capitalize(sen):
#
#     words=sen.split(" ")
#     capt_word= [word[0].upper() + word[1:] for word in words]
#     return " ".join(capt_word)
#
# print(capitalize("mayur joshi"))


# #>>>>10>>>>count words in sentence>>>>>>...
# def count_words(sen):
#
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
#
# print(count_words("mayur joshi"))


# #convert upper into lower and lower into upper at same time
#
# def stringconvert(strt):
#     result=""
#     for char in strt:
#         askii_val= ord(char)
#         #lower convert
#         if 65<= askii_val <=90:
#             #result.append(chr(askii_val + 32))
#             result+=chr(askii_val + 32)
#         #upper convert
#         elif 97<= askii_val <=122:
#             #result.append(chr(askii_val - 32))
#             result+=chr(askii_val - 32)
#         else:
#             #result.append(char)
#             result+=char
#
#     return "".join(result)
#
# print(stringconvert("ZzAaXxWwPp"))


