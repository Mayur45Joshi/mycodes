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



# import random
# import string
#
# users = [
#     {"username": "john_doe", "dob": "1990-05-10"},
#     {"username": "jane_smith", "dob": "1985-12-25"},
#     {"username": "alice", "dob": "2000-01-01"}
# ]
#
# def generate_password(length=8):
#     chars = string.ascii_letters + string.digits + "!@#$%^&*"
#     return ''.join(random.choice(chars) for _ in range(length))
#
# for user in users:
#     user["password"] = generate_password()
#
# # Output
# for user in users:
#     print(user)



# Str="12mayur4joshi15"
# Output=31
text = "12mayur4joshi15"
total = 0
number = ""
for char in text:
    if char.isdigit():
        number += char  # keep adding digit to number
    else:
        if number:
            total += int(number)  # convert and add to total
            number = ""  # reset number
#Add last number if string ends with digits
if number:
    total += int(number)
print(total)
