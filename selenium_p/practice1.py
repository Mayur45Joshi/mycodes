from http import client

# Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.
# #dat = input("enter data")
# def test_distinct(dat):
#     if len(dat) == len(set(dat)):
#         return True
#         #print(len(dat))
#     else:
#         return False
#
# print(test_distinct([1, 5, 7, 9]))
# print(test_distinct([1, 5,5,7,7, 9]))


# #program that creates all possible strings using the letters 'a', 'e', 'i', 'o', and 'I'. Ensure that each character is used only once.
# import random
# list_data = ['a','e','i','o','u']
# #list_data = ['1','2','3','4','5']
# for dt in list_data:
#
#     random.shuffle(list_data)
#     print(''.join(list_data))



# # Remove and print every third number from a list of numbers until the list becomes empty
# def num_list(num):
#     index=0
#     while num:
#         index = (index + 2)%len(num)
#         print("removed no :", num.pop(index))
#         print(num)
# number=[1,2,3,4,5,6,7,8,9,10]
# print("oroginal list : " , number)
# num_list(number)


# #Write a Python program to make combinations of 3 digits.
# number=[]
# for num in range(56):
#     num=str(num).zfill(10)
#
# print(num)
# number.append(num)



# #Convert the string to a list and print all the words and their frequencies
# string_word="""The U.S. Declaration of Independence inspired many other similar documents in other countries, the first
# being the 1789 Declaration of Flanders issued during the Brabant Revolution in the Austrian Netherlands
# (modern-day Belgium). It also served as the primary model for numerous declarations of independence across
# Europe and Latin America, as well as Africa (Liberia) and Oceania (New Zealand) during the first half of the
# 19th century."""
# word_list = string_word.split()
# word_freq = [word_list.count(n) for n in word_list]
#
# # print(word_list)
# # print(word_freq)
# # print(word_list,word_freq)
# print("String:\n {} \n".format(string_word))
# print("List:\n {} \n".format(str(word_list)))
# print("Pairs (Words and Frequencies:\n {}".format(str(list(zip(word_list, word_freq)))))



## Get the top stories from Google news
# import bs4
# from urllib.request import urlopen
# from bs4 import BeautifulSoup as soup
#
# news_url = "https://news.google.com/news/rss"
#
# try:
#     with urlopen(news_url) as client:
#     #Client=urlopen(news_url)
#         xml_page=client.read()
#
# except Exception as e:
#     print(f"Failed to retrieve the news feed: {e}")
#     exit()
#
# #Client.close()
# soup_page=soup(xml_page,"xml")
# news_list=soup_page.findAll("item")
#
# for news in news_list:
#     # print(news.title.text)
#     # print(news.link.text)
#     # print(news.pubDate.text)
#     # print(" " * 60)
#     title = news.title.text if news.title else "No Title"
#     link = news.link.text if news.link else "No Link"
#     pub_date = news.pubDate.text if news.pubDate else "No Date"
#
#     print(title)
#     print(link)
#     print(pub_date)
#     print("-" * 60)



# #Print out a set containing all the colors from a list which are not present in other list
# color_list1= {"White","Black","Red"}
# color_list2 = {"Red","Green"}
# print("Original sets")
# print(color_list1)
# print(color_list2)
# print("difference of two lists")
# print(color_list1.difference(color_list2))
# print(color_list2.difference(color_list1))



#add all integer digits from string

# def add_integers_in_string(s):
#     # Initialize sum to 0
#     total_sum = 0
#
#     # Initialize an empty string to build numbers
#     num_str = ""
#
#     # Iterate over each character in the string
#     for char in s:
#         # Check if the character is a digit
#         if char.isdigit():
#             # Append the digit to the num_str
#             num_str=num_str+char
#         else:
#             # If num_str is not empty, add its integer value to total_sum
#             if num_str:
#                 total_sum=total_sum+int(num_str)
#                 num_str = ""
#
#     # Add the last number's integer value to total_sum (if any)
#     if num_str:
#         total_sum=total_sum+int(num_str)
#
#     return total_sum
#
#
# # Test the function
# s = "123abc45ds565"
# result = add_integers_in_string(s)
# print("Sum of integers in the string:", result)



# # easier way of above
# #
# str=input("Enter any string")
# values=list(str)
# sum=0
# letters=""
# for v in values:
#     if v.isdigit():
#         sum=sum+int(v)
#
#     else:
#         letters=letters+v
# print(sum)
# print(letters)


# n = int(input("Enter any Number"))
# if n % 2 != 0 or n in range (6,21):
#     print("Weird")
# # elif n==2 or 4:
# #     print("Not Weird")
# # elif n in (6, 20):
# #     print("Weird")
#
# else:
#     print("Not Weird")




# def are_anagrams(str1, str2):
#   return sorted(str1) == sorted(str2)
#
# string1 = input("Enter the first string: ")
# string2 = input("Enter the second string: ")
# if are_anagrams(string1, string2):
#   print("Anagrams")
# else:
#   print("Not anagrams")



def char_count(input_string):
    string="my name is mayur"
    char_count = {}
    for char in input_string:
        char_count[char] = char_count.get(char,0)+1

    return char_count

char_count()




