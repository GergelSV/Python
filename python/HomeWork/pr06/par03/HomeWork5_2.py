class Complex:
    def __init__(self,a,b) -> None:
        self.a = a
        self.b = b

    def __str__(self) -> str:
        if self.b < 0:
            znak = '-'
            self.b *=-1
        else:
             znak = '+'    
        return str(self.a)+znak+str(self.b)+'*i'

    def __add__(self,other):   
        a= self.a + other.a
        b = self.b + other.b
        return Complex(a,b)
        
       
    
    def __sub__(self,other):
        a = self.a - other.a
        b = self.b - other.b
        return Complex(a,b)
        

    # произведениe комплексных чисел a+bi и c+di  (ac+bd)+(bc-ad)*i

    def __mul__(self,other):
        ac= self.a * other.a
        bd = self.b * other.b
        bc = self.b * other.a
        ad = self.a * other.b
        a = ac - bd
        b = bc + ad

        return Complex(a,b)
        

    def __truediv__(self,other):
        ac= self.a * other.a
        bd = self.b * other.b
        bc = self.b * other.a
        ad = self.a * other.b
        c2PlusD2 = other.a * other.a + other.b *other.b 
        a = (ac + bd)/c2PlusD2
        b = (bc - ad)/c2PlusD2

        return Complex(a,b)
        


# z = a+b*i комплексное число

z1 = Complex(5,-6)
z2 = Complex(-3,2)

print('z1+z2 =',z1+z2)
print('z1-z2 =',z1 - z2)

z1 = Complex(2,3)
z2 = Complex(-1,1)
print('z1*z2 =',z1 * z2)

z1 = Complex(-2,1)
z2 = Complex(1,-1)
print('z1/z2 =',z1 / z2)