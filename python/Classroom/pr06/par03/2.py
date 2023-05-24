# class My_math:
    
#     __count=0

#     @staticmethod
#     def  middle_arithmetic(n1,n2,n3,n4):
#         My_math.__count+=1
#         return (n1+n2+n3+n4)/4
    
#     @staticmethod
#     def max(n1,n2,n3,n4):
#         mas=[n1,n2,n3,n4]
#         My_math.__count+=1
#         return max(mas)
    
#     @staticmethod
#     def min(n1,n2,n3,n4):
#         mas=[n1,n2,n3,n4]
#         My_math.__count+=1
#         return min(mas)
    
#     @staticmethod
#     def factorial(n):
#         factor=1
#         for i in range(1,n+1):
#             factor*=i
#         My_math.__count+=1
#         return factor
#     @staticmethod
#     def get_count():
#         return My_math.__count



# print('max=',My_math.max(1,2,5,7))
# print('min=',My_math.min(1,2,5,7))
# print('Middle arithmetic =',My_math.middle_arithmetic(5,8,7,1))
# print ('Factorial =',My_math.factorial(4))
# print('Count =',My_math.get_count())

from math import pi
class Square:
    
    count = 0
    
    @staticmethod
    def circle(r):
        Square.count+=1
        return pi*r*r

    @staticmethod
    def romb(d1,d2):
        Square.count+=1
        return d1*d2/2

    @staticmethod
    def kvadrat(a,b):
        Square.count+=1
        return a*b

    @staticmethod
    def get_count():
        return Square.count
        





