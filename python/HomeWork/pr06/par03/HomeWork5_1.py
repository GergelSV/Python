import math
import random
class Circle:
    def __init__(self,r) -> None:
        self.r = r
            
    def show_info(self):
        print('r =',self.r)
         

    def __eq__(self, __value: object) -> bool:
        if type(__value) == Circle:
            if self.r == __value.r:
                return True
            else:
                return False
    def __lt__(self,other):
        if type(other) == Circle:
            if 2*math.pi*self.r < 2*math.pi*other.r:
                return True
            else:
                return False

    def __gt__(self,other):
        if type(other) == Circle:
            if 2*math.pi*self.r > 2*math.pi*other.r:
                return True
            else:
                return False    

    def __le__(self,other):
            if type(other) == Circle:
                if 2*math.pi*self.r <= 2*math.pi*other.r:
                    return True
                else:
                    return False    

    def __ge__(self,other):
            if type(other) == Circle:
                if 2*math.pi*self.r >= 2*math.pi*other.r:
                    return True
                else:
                    return False  
                            
    def __add__(self,other):
            return Circle(self.r + other)
                
    def __sub__(self,other):
            return Circle(self.r-other)
                    
    def __iadd__(self,other):
            self.r += other 
            return Circle(self.r)
                    
    def __isub__(self,other):
            self.r -= other
            return Circle(self.r)
            


a1 = Circle(105)
a2 = Circle(10)
a3 = Circle(23)
a4 = Circle(1)
number = random.randint(1,100)

print('circle a1 = circle a2 is',a1 == a2)
print('circle a1 > circle a2 is',a1 > a2)
print('circle a1 < circle a2 is',a1 < a2)
print('circle a1 >= circle a2 is',a1 >= a2)
print('circle a1 <= circle a2 is',a1 <= a2)

a1 = a1 - number
print('after decreasing by ',number,' radius object  a1= ',a1.r)       
a2 = a2 + number
print('after increaseing by ', number,' radius object a2=',a2.r)        

number = random.randint(1,100)
a4 += number
print('expression a4 += ',number,' is ',a4.r)                           

number = random.randint(1,10)
a3 -= number
print('expression a3 -= ',number,' is ',a3.r)                           

