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
    def kvadrat(a):
        Square.count+=1
        return a*a
    
    @staticmethod
    def rightTriangle(a,b):
        Square.count+=1
        return (a*b)/2
    
    @staticmethod
    def circumferential_area_of_triangle(a,b,c,r):
        Square.count+=1
        return (a*b*c)/4*r
    
    @staticmethod
    def Side3_R_Triangle(a,b,c,r):
        Square.count+=1
        return (a+b+c)/2*r
    
    
    @staticmethod
    def get_count():
        return Square.count
        
romb1 = Square.romb(2,3)
print('S romb =',romb1)

triangle1 = Square.circumferential_area_of_triangle(1,2,5,8)
print('S1 triangle = ',triangle1)

triangle2 = Square.Side3_R_Triangle(2,5,7,10)
print('S2 triangle = ',triangle2)

figure = Square.kvadrat(2)
print('S kvadrat = ',figure)

count = Square.get_count()
print("Count call function in class Squer = ",count)


