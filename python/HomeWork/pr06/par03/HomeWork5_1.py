import random
class Circle:
    def __init__(self,r,circumference) -> None:
        self.r = r
        self.circumference = circumference
    
    def show_info(self):
        print('r =',self.r, 'длина  = ',self.circumference)
         

    def __eq__(self, __value: object) -> bool:
        if type(__value) == Circle:
            if self.r == __value.r:
                return True
            else:
                return False
    def __lt__(self,other):
        if type(other) == Circle:
            if self.circumference < other.circumference:
                return True
            else:
                return False

    def __gt__(self,other):
        if type(other) == Circle:
            if self.circumference > other.circumference:
                return True
            else:
                return False    

    def __le__(self,other):
            if type(other) == Circle:
                if self.circumference <= other.circumference:
                    return True
                else:
                    return False    

    def __ge__(self,other):
            if type(other) == Circle:
                if self.circumference >= other.circumference:
                    return True
                else:
                    return False  
                            
    def __add__(self,other):
            return self.r + other
                
    def __sub__(self,other):
            return self.r-other
                    
    def __iadd__(self,other):
            self.r += other 
            return self.r
                    
    def __isub__(self,other):
            self.r -= other
            return self.r
            


a1 = Circle(105,25)
a2 = Circle(10,20)
a3 = Circle(23,45)
a4 = Circle(1,2)
number = random.randint(1,100)

print('expression a1 == a2 is',a1 == a2)
print('expression a1 > a2 is',a1 > a2)
print('expression a1 < a2 is',a1 < a2)
print('expression a1 >= a2 is',a1 >= a2)
print('expression a1 <= a2 is',a1 <= a2)

a1.r = a1.r - number
print('after decreasing by ',number,' radius object  a1= ',a1.r)       
a2.r = a2.r + number
print('after increaseing by ', number,' radius object a2=',a2.r)        

number = random.randint(1,100)
a4.r += number
print('expression a4 += ',number,' is ',a4.r)                           

number = random.randint(1,10)
a3.r -= number
print('expression a3 -= ',number,' is ',a3.r)                           

