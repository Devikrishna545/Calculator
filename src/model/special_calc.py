import math

class SpecialCalculator:
    def __init__(self,mem=0):
        self.mem = mem

    def sqrt(self,a):
      
        return math.sqrt(a)

    def perct(self,a):
        x=int(input("enter the percentage"))
        output=(a*x)/100
        return output

    def memory_store(self,c):
        self.mem = c

    def mem_recall(self):
        return self.mem

    def mem_add(self,a):
        self.mem +=a
        return self.mem

    def mem_sub(self,a):
        self.mem -=a
        return self.mem