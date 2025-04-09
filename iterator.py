#iterator

# mytuple=("apple","banana","cherry")
# it=iter(mytuple)
# print(it)
# print(next(it))
# print(next(it))
# print(next(it))


class munumber():
    def __iter__(self):
        self.a=1
        return self

    # def __next__(self):
    #     x=self.a
    #     self.a=self.a+1
    #     return x

    def __next__(self):
        if self.a<=15:
            x=self.a
            self.a=self.a+1
            return x
        else:
            raise StopIteration
mynm=munumber()
it=iter(mynm)

# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

for x in it:
    print(x)


