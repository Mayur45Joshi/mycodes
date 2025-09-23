# def print_pascals_triangle(n):
#     for line in range(n):
#         # Add spaces for alignment
#         print(" " * (n - line), end=" ")
#
#         num = 1
#         for i in range(line + 1):
#             print(num, end=" ")
#             # Update number using formula: nCr+1 = nCr * (n-r)/(r+1)
#             num = num * (line - i) // (i + 1)
#         print()
#
# # Example: print 6 rows
# print_pascals_triangle(6)



# # pairs giving sum 10
# List = [2, 5, 4, 1, 12, -2, 8, 9]
#List="s,d,sds,ds,s,s"
# target = 10
# pairs = []
# for i in range(len(List)):
#     for j in range(i + 1, len(List)):
#         if List[i] + List[j] == target:
#             pairs.append((List[i], List[j]))
#
# print(pairs)


# Str="MAYUR"
# new=Str.replace("A","0").replace("Y","P")
# print(new)


# text = "a,b,c,d,e"
# parts = text.split(",", 2)   # split at most 2 times
# print(parts)


# Str="Mayur"
# new=",".join(list(Str))
# print(new)


# Str="Mayur Joshi is good boy and havin g funf"
# words=Str.lower().split()
# print(sorted(words))
# print(" ".join(sorted(words)))



# Str="Mayur333 Joshi is good boy and havin g funf"
# words=Str.split()
# max_len=max(len(word) for word in words)
# for word in words:
#     if len(word)==max_len:
#         print(word)



# def compare(s1,s2):
#     if len(s1)!=len(s2):
#         return False
#     for i in range(len(s1)):
#         if s1[i]!=s2[i]:
#             return False
#     return True

# print(compare("ma1yur","Ma1yur"))


# s1="mayur"
# s2="joshi"
# #if len(s1)==len(s2) and all(c1==c2 for c1,c2 in zip(s1,s2)):
# if len(s1)==len(s2) and all(c1.lower()==c2.lower() for c1,c2 in zip(s1,s2)):
#     print(True)
# else:
#     print(False)



# Str="Kalyani Lives in Pune"
# words=Str.split()
# first=""
# for word in range(2):
#     first+=words[word][0] + " "
# second=""
# for word in range(-2,0):
#     second+=words[word] + " "
#
# result=first + second
# print(result.strip())



# numbers = [5, 2, 9, 1, 7]
# words = ["banana", "apple", "cherry", "date"]
# # Ascending
# asc = sorted(words)
# print("Ascending:", asc)   # [1, 2, 5, 7, 9]
# # Descending
# desc = sorted(words, reverse=True)
# print("Descending:", desc)  # [9, 7, 5, 2, 1]
#
# # Ascending
# numbers.sort()
# print("Ascending:", numbers)   # [1, 2, 3, 4]
# # Descending
# numbers.sort(reverse=True)
# print("Descending:", numbers)  # [4, 3, 2, 1]
#
#
# text = "mayur"
# # Ascending
# asc = "".join(sorted(text))
# print("Ascending:", asc)   # 'amruy'
# # Descending
# desc = "".join(sorted(text, reverse=True))
# print("Descending:", desc)  # 'yurma'


# import string
# def StringChallenge(str_param):
#     # __define-ocg__: custom password validation rules
#
#     # filters for checking constraints
#     varFiltersCg = {
#         "has_upper": any(ch.isupper() for ch in str_param),
#         "has_digit": any(ch.isdigit() for ch in str_param),
#         "has_symbol": any(ch in string.punctuation for ch in str_param),
#         "no_password": "password" not in str_param.lower(),
#         "valid_length": 7 < len(str_param) < 31
#     }
#     # aggregate check
#     varOcg = all(varFiltersCg.values())
#
#     if varOcg:
#         return "true"
#     else:
#         return "false"
# # Example tests
# print(StringChallenge("apple!M7"))  # true
# print(StringChallenge("mypassword1!A"))  # false
# print(StringChallenge("Hello@123"))  # true
# print(StringChallenge("short1!"))  # false



# def leader(arr):
#     leader=[]
#     max_val=arr[-1]
#     leader.append(max_val)
#     for i in range(len(arr)-2,-1,-1):
#         if arr[i] > max_val:
#             leader.append(arr[i])
#             max_val=arr[i]
#     print(leader)
#     print(leader[::-1])
# arr=[16, 17, 4, 3, 5, 2]
# leader(arr)


