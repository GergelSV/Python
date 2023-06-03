import math
class Figure:                           
    def __init__(self) -> None:
        pass

    def square(self):
        pass

        
class Rectangle(Figure):                
    def __init__(self, a,b) -> None:
        super().__init__()
        self.a = a
        self.b = b

    def square(self):
        return self.a * self.b
    
    def __int__ (self):
        return self.square()
    
    def __str__(self) -> str:
        print('figure Rectangle with sides',self.a,' and ',self.b,' has an square = ',self.__int__())

class Circle(Figure):   
    def __init__(self,a) -> None:
        super().__init__()
        self.a = a
        
    def square(self):
        return math.pi*self.a*self.a
    
    def __int__ (self):
        return self.square()
    
    def __str__(self) -> str:
        print('figure Circle with radius',self.a,' has an square = ',self.__int__())

    

class RightTriangle(Figure):
    def __init__(self, a, c) -> None:
        super().__init__()
        self.a = a
        self.c = c
       
    def square(self):
        return 0.5*self.a*self.c
    
    def __int__ (self):
        return self.square()
    
    def __str__(self) -> str:
        print('figure RightTriangle with sides',self.a,',and ',self.c,' has an square = ',self.__int__())
    
class Trapezoid(Figure):
    def __init__(self, a, b,h) -> None:
        super().__init__()
        self.a = a
        self.b = b
        self.h = h

    def square(self):
        return (self.a+self.b)*self.h/2                     
    
    def __int__ (self):
        return self.square()
    
    def __str__(self) -> str:
        print('figure Trapezoid with sides',self.a,' and ',self.b,' with higth',self.h,' has an square = ',self.__int__())


figur1 = Trapezoid(2,5,3)
figur1.__str__()

figur2 = RightTriangle(5,7)
figur2.__str__()

figur3 = Circle(5)
figur3.__str__()

figur4 = Rectangle(5,4)
figur4.__str__()




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