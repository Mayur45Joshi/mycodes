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


# def duplicatesfind(s):
#     seen=set()
#     result=[]
#     for char in s:
#         if char not in seen:
#             result.append(char)
#             seen.add(char)
#     return result
# s=['a','d','r','r','t','y','a','u']
# print(duplicatesfind(s))


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
#     return [num * num if num % 2 == 0 else num for num in inp]
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

# #| operator introduced in Python 3.9 can be used to merge dictionaries. It creates a
# # new dictionary without modifying the original dictionary.
# d1 = {'x': 1, 'y': 2}
# d2 = {'y': 3, 'z': 4}
# d3 = d1 | d2
# print(d3)


# #reading data in txt file
# with open (r"D:\STUDY AUTO\files\aim.txt","r") as file:
#     content=file.read()
#     print(content)


#reading data line in a file one at a time
# with open (r"D:\STUDY AUTO\files\aim.txt","r") as file:
#     line=file.readline()
#     while line:
#         print(line,end='')
#         line=file.readline()


# #array rotate (Left Rotation by 1):
# arr=[1,2,3,4,5,6,7]
# def rotate_arr(arr):
#     return arr[1:] + arr[:1]
#
# print(rotate_arr(arr))


# #monotonic array check increasing or decresing
# arr=input("enter any array")
# def is_monotonic(arr):
#     incresing=decreasing=True
#     for i in range(len(arr)-1):
#         if arr[i]> arr[i+1]:
#             incresing=False
#         if arr[i]< arr[i+1]:
#             decreasing=False
#
#     return incresing or decreasing
# print(is_monotonic(arr))


# #swapping first and last items in list
# arr=[1,2,3,4,5,6]
# def swap_str(arr):
#     arr[0],arr[-1] = arr[-1],arr[0]
#     return arr
# print(swap_str(arr))


# #Python | Find elements of a list by indices
# lst1=[12,14,45,48,48,71]
# lst2=[0,2,1,3]
#
# def indices(lst1,lst2):
#     return [lst1[i] for i in lst2]
#
# print(indices(lst1,lst2))

# #Python - Ways to find indices of value in list
# a=[1,2,7,8,7,8,9,7]
# indices=[]
# for i in range(len(a)):
#     if a[i]==7:
#         indices.append(i)
#
# print(indices)


#Find most frequent repeate element in a list
# def most_fre(List):
#     counter=0
#     #num=List[0]
#     for i in List :
#         curr_freq=List.count(i)
#         if curr_freq > counter:
#             counter=curr_freq
#             num=i
#     return num
#
# # List=[1,2,2,4,2,2,2,2,8,5,9]
# List="55788888888961212121111111111111111111"
# print(most_fre(List))


# from collections import Counter
# def repeate(Str):
#     counts = Counter(Str)
#     print(dict(counts))
#     print(max(counts))
#
# repeate("ccdhddhhhhhhd")

#

# #Finding All Elements with Their Frequencies:
# from collections import Counter
# def find_frequencies(arr):
#     freq=Counter(arr)
#     return dict(freq)
#
# arr=[1,1,1,2,2,3,3,8,8,9,9,6,6,4,4]
# print(find_frequencies(arr))


# #Given string like "abc38gh89" separate number from this string without converting into character array
# str = "afa353hg353"
# lst1 = ""
# #lst2 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# lst2="0123456789"
# for char in str:
#     if char not in lst2:
#         lst1 += char
# print(lst1)


# #Move all the zeroes to one side of array and ones to right side of array
# def zeroonefun(arr):
#     zeros=[x for x in arr if x==0]
#     ones=[x for x in arr if x==1]
#     others=[x for x in arr if x not in [1,0]]
#     return zeros + others + ones
# arr = [1, 0, 1, 2, 0, 3, 0, 4, 1]
# print(zeroonefun(arr))


# #convert string into lower without using inbuld function
# def to_lower(s):
#     result=""
#     for char in s:
#         #ord = gives askii value for charter
#         #chr = giver charte for any askii value
#         aski_val=ord(char)
#         if 65<= aski_val <=90:
#             result+= chr(aski_val+32)
#         else:
#             result += char
#     return result
# print(to_lower("MAYUR"))


# # to convert in upper cases
# def to_upper(s):
#     result = ""
#     for char in s:
#         aski_val = ord(char)
#         if 97 <= aski_val <= 122:
#             result += chr(aski_val - 32)
#         else:
#             result += char
#     return result
#
# print(to_upper("mayur"))



# def reverse_alterword(sentence):
#
#     words=sentence.split()
#     trasform_w=[]
#
#     for i, word in enumerate(words):
#         if i%2 != 0:
#             trasform_w.append(word[::-1])
#
#         else:
#             trasform_w.append(word)
#
#     return " ".join(trasform_w)
# print(reverse_alterword("mayur joshi is good boy"))



##another way of above
# def reversealtnum(sen):
#     trans_word = []
#     words = sen.split()
#     for i in range(len(words)):
#         if i % 2 == 0:
#             trans_word.append(words[i][::-1])
#
#         else:
#             trans_word.append(words[i])
#
#     return " ".join(trans_word)
#
#
# sen = "Mayur joshi is good boy"
# print(reversealtnum(sen))



# def nonrepeate(str):
#
#     char_count = {}
#     for char in str:
#         if char in char_count:
#             char_count[char]+=1
#
#         else:
#             char_count[char]=1
#     print(char_count)
#     for char in str:
#         if char_count[char]==1:
#             return char
# str="aaabbfddhh"
# print(nonrepeate(str))


# import oracledb
# conn = oracledb.connect(user="C##mayur", password="joshi", dsn="localhost:1521/orcl")
# print("Connected successfully.")


# def charcount(strt):
#     char_count = {}
#     result = ""
#     for char in strt:
#         if char in char_count:
#             char_count[char] += 1
#
#         else:
#             char_count[char] = 1
#
#     for char, count in char_count.items():
#         result += char + str(count)
#
#     return result
# strt = "aabbbccccddddd"
# print(charcount(strt))


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


# #another way
# def alt_rev(sen):
#     words=sen.split()
#     result=[]
#     for word in range(len(words)):
#         if word%2==0:
#             result.append(words[word][::-1])
#         else:
#             result.append(words[word])
#     return " ".join(result)
# sen="mayur joshi is good"
# print(alt_rev(sen))



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



#>>>>1>>>>reverse string
# from collections import Counter


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


# def countwords(arr):
#     vowels="aeiou"
#     vowels_lst=[]
#     const=[]
#     others=[]
#     for char in arr:
#         if char in vowels:
#             vowels_lst.append(char)
#         elif char.isalpha() and char.lower() not in vowels:
#             const.append(char)
#         else:
#             others.append(char)
#
#     print(vowels_lst,"count:", len(vowels_lst))
#     print(const,"count:" ,len(const))
#     print(others, "count:" , len(others))
# countwords("54545hgfdtytuymuiu")



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
#     for char in strs:
#         if char not in seen:
#             seen.add(char)
#             result+=char
#
#     return result
#
# strs="mamaghrgh"
# print(remove_duplicate(strs))


# #only work for even no of characters
# def removedupl(arr):
#     result=[]
#     for char in arr:
#         if char not in result:
#             result.append(char)
#         else:
#             result.remove(char)
#     return result
# print(removedupl("mmmmgfgg6756"))


# def removerep(arr):
#     result=[]
#     for char in arr:
#         if arr.count(char)==1:
#             result.append(char)
#     return result
#
# print(removerep("mmmmgfgg6756"))


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
#       #str1="12345".replace(" ","").lower()
#       #str2="54321".replace(" ","").lower()
#     if sorted(str1)==sorted(str2):
#         print("angrams ")
#     else:
#         print("no angrama")
#
# str1="fjsh"
# str2="mayur"
# print(anagrams(str1,str2))




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


# Input: "Automation"
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


# # Str="12mayur4joshi15"
# # Output=31
# text = "12mayur4joshi15"
# total = 0
# number = ""
# for char in text:
#     if char.isdigit():
#         number += char  # keep adding digit to number
#     else:
#         if number:
#             total += int(number)  # convert and add to total
#             number = ""  # reset number
# #Add last number if string ends with digits
# if number:
#     total += int(number)
# print(total)


# def stringtotal(Str):
#     total=0
#     number=""
#     alpha=""
#     for char in Str:
#         if char.isdigit():
#             number+=char
#         elif char.isalpha():
#             alpha+=char
#             if number:
#                 total+=int(number)
#                 number=""
#         else:
#             if number:
#                 total+=int(number)
#                 number=""
#     if number:
#         total+=int(number)
#     print(total)
#     print(alpha)
# stringtotal("12mayur4joshi15")