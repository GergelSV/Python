import math
class Figure:                           #  * arg
    def __init__(self,a,b,) -> None:
            self.a = a
            self.b = b

    def square(self):
        pass

    
class Rectangle(Figure):                
    def __init__(self, a, b) -> None:
        super().__init__(a, b)

    def square(self):
        return self.a * self.b

class Circle(Figure):                   #a - радиус b - длина окружности
    def __init__(self, a, b) -> None:
        super().__init__(a, b)

    def square(self):
        return math.pi*self.a*self.a

class RightTriangle(Figure):
    def __init__(self, a, b) -> None:
        super().__init__(a, b)
       
    def square(self):
        return 0.5*super().square()

class Trapezoid(Figure):
    def __init__(self, a, b,h) -> None:
        super().__init__(a, b)
        self.h = h

    def square(self):
        return (self.a+self.b)*self.h/2                     
    


figur1 = Trapezoid(2,5,3)
print (figur1.square())

figur2 = RightTriangle(5,7)
print (figur2.square())

figur3 = Circle(5,12)
print (figur3.square())
# class Circle:
#     def __init__(self,r) -> None:
#         self.r = r
    
#     def len(self):
#         return 2*math.pi*self.r


# class Square:
#     def __init__(self,a) -> None:
#         self.a = a
#     def len(self):
#         return 4*self.a

# class CircleInSquare(Circle, Square):
#     def __init__(self,r,a) -> None:
#         if (r < a/2):
#             Circle.__init__(self,r)
#             Square.__init__(self,a)
#         else:
#             del(self)

#     def len(self):
#         return Circle.len(self)+ Square.len(self)

# item = CircleInSquare(40,6)
# print(item)
# print(item.len())
# item2 = Circle(4)
# print(CircleInSquare.len(item2))