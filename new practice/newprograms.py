# """ Below is the roles that a user has, each string represents an individual role, The roles on a user is available as a list,
# PRI|8046001|Account|2024-07-04T06:50:34.0Z,
# PRI|8046002|Account|2025-04-17T19:59:11.0Z,
# UNRS|8046002|Account|2025-04-17T19:59:11.0Z,
# UNRS|8046001|Account|2024-07-04T06:50:34.0Z,
# MTN|8046002|Logical|2024-07-04T06:50:34.0Z,
# WLA|8046002|Physical|2024-07-04T06:50:34.0Z,
# 1.Filter all the unique account
# 2. creation date for PRI privilege on Account 8046002 """

# roles = [
#     "PRI|8046001|Account|2024-07-04T06:50:34.0Z",
#     "PRI|8046002|Account|2025-04-17T19:59:11.0Z",
#     "UNRS|8046002|Account|2025-04-17T19:59:11.0Z",
#     "UNRS|8046001|Account|2024-07-04T06:50:34.0Z",
#     "MTN|8046002|Logical|2024-07-04T06:50:34.0Z",
#     "WLA|8046002|Physical|2024-07-04T06:50:34.0Z"
# ]
# accounts=[role.split("|")[1] for role in roles if "Account" in role]
# unique=set(accounts)
# print(accounts)
# print(unique)
#
# #date=(role.split("|")[3] for role in roles if "PRI" in role and "Account"=8046002)
# date=next(role.split("|")[3] for role in roles if role.startswith("PRI|8046002|Account|"))
# print(date)


# #"TXN|<txn_id>|<user_id>|<amount>|<status>|<date>"
# trans = [
#     "TXN|1001|U01|250|SUCCESS|2024-05-01T10:20:30Z",
#     "TXN|1002|U02|450|FAILED|2024-06-02T12:10:20Z",
#     "TXN|1003|U01|300|SUCCESS|2024-06-03T09:15:10Z",
#     "TXN|1004|U03|700|SUCCESS|2024-06-04T14:25:00Z",
#     "TXN|1005|U02|450|FAILED|2024-06-05T16:40:55Z",
# ]
#
# users=[tran.split("|")[2] for tran in trans if "SUCCESS" in tran]
# print(set(users))
# #amt=[tran.split("|")[3] for tran in trans if "U01" in tran]
# amt=[int(tran.split("|")[3]) for tran in trans if tran.split("|")[2] == "U01"]
# print(max(amt))
# txid=[tran.split("|")[1] for tran in trans if "FAILED" in tran]
# print(txid)




# movies = [
#     "M01|Inception|8.8|2010",
#     "M02|Interstellar|8.6|2014",
#     "M03|Tenet|7.5|2020",
#     "M04|Dunkirk|7.9|2017",
#     "M05|Oppenheimer|9.0|2023"
# ]
#
# # Extract all movie names released after 2015.
# # Find the highest-rated movie.
# # Get all unique ratings (no duplicates).
#
# names=[m.split("|")[1] for m in movies if m.split("|")[3] > "2015"]
# print(names)
#
# rate=[m.split("|")[2] for m in movies]
# print(max(rate))
#
# rate1=set([m.split("|")[2] for m in movies])
# print(rate1)



# orders = [
#     "O01|U01|Laptop|75000|DELIVERED",
#     "O02|U02|Mobile|20000|PENDING",
#     "O03|U01|Tablet|30000|DELIVERED",
#     "O04|U03|Headphones|3000|DELIVERED",
#     "O05|U02|Monitor|12000|CANCELLED"
# ]
# # Find all unique users who got a DELIVERED order.
# # Get the costliest product ordered.
# # Find all order IDs where status = CANCELLED.
#
# max_amt=max(int(o.split("|")[3]) for o in orders if "DELIVERED" in o)
# cost=[o.split("|")[2] for o in orders if "DELIVERED" in o and int(o.split("|")[3]) == max_amt]
# print(cost)
# can=[o.split("|")[0] for o in orders if "CANCELLED" in o]
# print(can)



# results = [
#     "R01|John|Math|85",
#     "R02|Mary|Science|92",
#     "R03|John|Science|78",
#     "R04|Mary|Math|88",
#     "R05|Alex|Math|95"
# ]
# # Find John’s average marks.
# # Who scored the highest overall?
# # List all subjects without duplicates.
#
# marks = [int(r.split("|")[3]) for r in results if "John" in r]
# avg = sum(marks) / len(marks)
# print(avg)
#
# high = [(r.split("|")[1], int(r.split("|")[3])) for r in results]
# print(high)
#
# # dictionary to accomulate total marks
# totals = {}
# for name, mark in high:
#     if name in totals:
#         totals[name] += mark
#     else:
#         totals[name] = mark
#
# max_total = -1
# topper = None
# for name, total in totals.items():
#     if total > max_total:
#         max_total = total
#         topper = name
#
# print(topper, max_total)



# max_score=-1
# topper=None
# for name,mark in high:
#     if mark>max_score:
#         max_score=mark
#         topper=name
# print(topper,mark)




# def digit_sum(num):
#     Sum = 0
#     for digit in str(num):
#         Sum += int(digit)
#
#     # recursion instead of while
#     if Sum > 9:
#         return digit_sum(Sum)
#     else:
#         return Sum
#
# num = 123456
# print("Final single digit sum:", digit_sum(num))



# def fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         print(a, end=" ")
#         a, b = b, a + b
#
# # Example: print first 6 numbers
# fibonacci(6)



# feedback = ["Great! ", "  OK", "", "Bye "]
#
# result = []
# for f in feedback:
#     stripped = f.strip()
#     if stripped:     # Only add if not empty
#         result.append(stripped)
#
# print(result)

# feedback = ["Great! ", "  OK", "", "Bye "]
# stripped=[x.strip() for x in feedback if x.strip()]
# print(stripped)


# # #Q3.  For integers 1–20, square if even, cube if odd. Strictly use list comprehension
# square=[x**2 if x%2==0 else x**3 for x in range(1,20)]
# print(square)


# def flatten(lst):
#     result=[]
#     for item in lst:
#         if isinstance(item,list):
#             result.extend(flatten(item))
#         else:
#             result.append(item)
#     return result
# x = [1, [2, [3]], 4]
# print(flatten(x))


##remove duplicates without using another list
# nums = [1, 2, 3, 2, 4, 1, 5]
# # Loop through the list and remove duplicates in place
# i = 0
# while i < len(nums):
#     if nums[i] in nums[:i]:
#         nums.pop(i)
#     else:
#         i += 1
# print(nums)


# nums = [1, 2, 3, 2, 4, 1, 5]
# for num in nums[:]:
#     if nums.count(num)>1:
#         nums.remove(num)
# print(nums)


