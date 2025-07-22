# Parse JSON - Convert from JSON to Python
# If you have a JSON string, you can parse it by using the json.loads() method.

# import json
# # some JSON:
# x='{"name":"john","age":"50","city":"kgn"}'
# y=json.loads(x)
# print(y["age"])


# #Convert from Python to JSON
#
# import json
# # a Python object (dict):
# x = {"name": "John","age": 30,"city": "New York"}
# # convert into JSON:
# y = json.dumps(x)
# # the result is a JSON string:
# print(y)



# import json
#
# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }
# print(json.dumps(x))



#####regular expression

# import re
#
# txt="my name is mayur joshi"
# re.search("my name",txt)


x = -2

if x < 0:
  raise Exception("Sorry, no numbers below zero")