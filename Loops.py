# # if else stattement
#
# Value = "Mayur Great"
#
# a = -1
# if a>=0:
#
#     print("Positive Value")
# else:
#     print("Negative Value")
#
#
#
# if Value == "Mayur Great":
#     print("Condition  matches")
#
# else:
#     print("Condition not Match")

##############################################################################
# For loop

# obj = [1, 2, 3, 4, 5]
#
# for i in obj:
#     print(i)
#     print(i*2)
#
# # adding first 5 natural nos
#
# Summation = 0
# for i in range(1, 6):
#     Summation = Summation+i
# print(Summation)
#
# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
#
# for k in range(1, 20, 5):
#     print(k)
#
# print("****************************************************************")
#
# for m in range(10):
#     print(m)


#########################################################################################

# While loop

# #
# mj = 10
# while mj>1:
#     if mj == 9:
#         mj = mj - 1
#         continue
#
#     if mj == 3:
#         break
#     print(mj)
#
#     mj= mj-1

#########################################################

# TUPLE LOOP

# thistuple = ("apple", "banana", "cherry")
# for x in thistuple:
#   print(x)


# thistuple = ("apple", "banana" , "cherry")
# for i in range(len(thistuple)):
#     print(thistuple[i])


# thistuple= ("apple", "banana" , "cherry")
# i=0
# while i<len(thistuple):
#     print(thistuple[i])
#     i=i+1



#join tuples

# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)
#
# tuple3 = tuple1 + tuple2
# print(tuple3)


# #multiply tuple
# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 2
#
# print(mytuple)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#set loops

# thisset = {"apple", "banana", "cherry"}
#
# for x in thisset:
#   print(x)


#JOIN SETS

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
#
# #set3 = set1.union(set2)
# set3 = set1 | set2
# print(set3)



# #Join multiple sets with the union() method:
#
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}
#
# #myset = set1.union(set2, set3, set4)
# myset = set1 | set2 | set3 |set4
# print(myset)



# #Join a set with a tuple:
#
# x = {"a", "b", "c"}
# y = (1, 2, 3)
#
# z = x.union(y)
# print(z)


# #INTERSECTION
#
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
#
# set3 = set1.intersection(set2)
# print(set3)


#INTERSECTION UPDATE
#The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
#
# set1.intersection_update(set2)
#
# print(set1)



#The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.

#Keep all items from set1 that are not in set2:
#You can use the - operator instead of the difference() method, and you will get the same result.

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
#
# set3 = set1.difference(set2)
#
# print(set3)




#The symmetric_difference() method will keep only the elements that are NOT present in both sets.
#You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
#
# set3 = set1.symmetric_difference(set2)
#
# print(set3)



#The keys() method will return a list of all the keys in the dictionary.
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
#
# x = thisdict.keys()
# #The values() method will return a list of all the values in the dictionary.
# y=thisdict.values()
# print(x)
# print(y)
#
# z=thisdict.items()
# print(z)



# # #adding items into list
# thisdict={"key1":"value1" , "key2" : "value2" , "key3":"value3"}
# thisdict["key4"] = "value4"
# print(thisdict)
#
# thisdict.update({"key4":"mj"})
# print(thisdict)



# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# #mydict = thisdict.copy()
# mydict = dict(thisdict)
# print(mydict)



# #Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
#
# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }
#
# myfamily = {
#   "mj1" : child1,
#   "mj2" : child2,
#   "mj3" : child3
# }
# print(myfamily)



# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }
# print(myfamily)
#
# #To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary:
#
# print(myfamily["child2"]["name"])




# #Loop through the keys and values of all nested dictionaries:
#
# for x, obj in myfamily.items():
#   print(x)
#
#   for y in obj:
#     print(y + ':', obj[y])



def fruits(fruit):
    for x in fruit:
        print(x)

fruit1=["apple","banana","cherry"]
fruits(fruit1)