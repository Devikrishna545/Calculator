class SimpleCalculator:

    def __init__(self):
        pass

    def add(self,a,b):
        return a+b

    def sub(a,b):
        if a<b:
            return -(b-a)
        else:
            return a-b

    def mul(self,a,b):
        return a*b

    def div(self,a,b):
        return a/b if b!=0 else print("zero division error")
        