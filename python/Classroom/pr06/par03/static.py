import random
from math import pi

class Square:
    count = 0
   
    @staticmethod
    def circle(r):
        Square.count += 1
        return pi*r*r
    
    @staticmethod
    def romb(d1,d2):
        Square.count += 1
        return d1*d2/2

    @staticmethod
    def get_count():
        return Square.count

# a = random.randint(0,10)

# s = Square()
# print(type(s))
# print(s)
# c = Square().circle(3)
# romb1 = Square.romb(2,3)
# print(type(romb1))
# print(Square.get_count())

s7 = Square()
s = [1,2]
s2 = 5
s3 = s + [s]
print(len(s7))
