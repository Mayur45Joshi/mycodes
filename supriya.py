"""s1 = {3,4}
s2 = {1,2}
s3 = set()
i = 0
j = 0
for i in s1:
    for j in s2:
        s3.add((i,j))
        i =i+1
        j = j+1
print(s3)
"""

a = 1+(2-3)*4**5//6
#b = 1+ (2028-3072)//6
#print(b)
"""print(a)

b = (22.0//5)
print(b)

list1 = [10,20,30]
list2 = [40,50,60]
list3 = list1+list2
print(list3)
list4 = list1.append(list2)
print(list4)
list5 = list1.extend(list2)
print(list5)


s = 'python languague python'
s1 = s.capitalize()
s2 = s.title()
print(s1,s2)
s3 = s.index('python')
print(s3)
print(s.find('A'))

t = ('1')
print(t*3)

TUP=([1,2],[3,4],[5,6])
TUP[2][1]=8
print(TUP)



a = -1024//6
print(a)


t = [1,2,4,3,8,9]
for i in range(0,len(t),2):
    print(t[i])

a = {1,2,3}
b = {4,5,6}
#print(a+b)

for x in range(4):
    print(x**2)


d = {1:2,2:3,3:4}
print(d.pop(4,9))
d1 = d.get(4,4)
print("value of d is ",d1)

d2 = {1:"A",2:"B",3:"C"}
d3 = d2.setdefault(4,"D")
print(d2.clear())"""

A = input("Enter Any string which want to reverse")

def reve(A):
    str = ""
    for i in A:
        str = i + str
        print(str)
        return str
print(str)
print(A)
print(reve(A))





