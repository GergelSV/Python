class Complex:
    def __init__(self,a,b) -> None:
        self.a = a
        self.b = b

    def __add__(self,other):
        aPlusC= self.a + other.a
        bPlusD = self.b + other.b
        return str(aPlusC) +str(bPlusD) +'*i'
    
    def __sub__(self,other):
        aSubC= self.a - other.a
        bSubD = self.b - other.b
        return str(aSubC) +str(bSubD) +'*i'

    # произведениe комплексных чисел a+bi и c+di  (ac+bd)+(bc-ad)*i

    def __mul__(self,other):
        ac= self.a * other.a
        bd = self.b * other.b
        bc = self.b * other.a
        ad = self.a * other.b
        skobka1 = ac - bd
        skobka2 = bc + ad

        return str(skobka1) +str(skobka2) +'*i'

    def __truediv__(self,other):
        ac= self.a * other.a
        bd = self.b * other.b
        bc = self.b * other.a
        ad = self.a * other.b
        c2PlusD2 = other.a * other.a + other.b *other.b 
        drob1 = (ac + bd)/c2PlusD2
        drob2 = (bc - ad)/c2PlusD2

        return str(drob1) +str(drob2) +'*i'


# z = a+bi комплексное число

z1 = Complex(5,-6)
z2 = Complex(-3,2)

print('z1+z2 =',z1 + z2)
print('z1-z2 =',z1 - z2)

z1 = Complex(2,3)
z2 = Complex(-1,1)
print('z1*z2 =',z1 * z2)

z1 = Complex(-2,1)
z2 = Complex(1,-1)
print('z1/z2 =',z1 / z2)