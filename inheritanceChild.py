from oppsconcept import Calculator


class FinalSum(Calculator):

    num2= 100

    def __init__(self):
        Calculator.__init__(self, 3,4,)

    def FinalTotal(self):

        return self.Summation() + self.num2

obj= FinalSum()

print(obj.FinalTotal())

