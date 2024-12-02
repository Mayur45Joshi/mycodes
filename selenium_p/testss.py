
# string= mayur123

str=input("enter any string")
sum=0
for char in str:
    if char.isdigit():
        sum=sum+int(char)
    else:
        pass

print(sum)