# List data type

values  = [1, 2.5, "Mayur", 10, 100]

print(values[0])

print(values[3])

print(values[1:3])

print(values[-1])
print(values[-2])

values.insert(3 , "Joshi")
print(values)

values.append("Supu")
print(values)

values[2] = "Mjj"
print(values)

del values[2]
print(values)


#tuple data type

tup = (1, 2.5, "Mayur")
print(tup[0])
print(tup[2])


# Dictionary data type work in Key:Value formate

dic={1:"First", "a": 4, 2:"Last2.5"}
print(dic[1])
print(dic["a"])
print(dic[2])


# we can define values in dictionary at run time also

dict={}

dict["Firstname"]= "Mayur"

dict["lastname"] = "Joshi"

dict["Gender"] = "Male"

print(dict)

print(dict["Firstname"])
