import random
class Airplane:
    def __init__(self,typeAirplane,Passengers,maxCountPassenger) -> None:
        self.typeAirplane = typeAirplane
        self.Passengers = Passengers
        self.maxCountPassenger = maxCountPassenger
    
    def __eq__(self, __value: object) -> bool:
        if type(__value) == Airplane:
            if self.typeAirplane == __value.typeAirplane:
                return True
            else:
                return False
            


    def __lt__(self,other):
        if type(other) == Airplane:
            if self.maxCountPassenger < other.maxCountPassenger:
                return True
            else:
                return False

    def __gt__(self,other):
        if type(other) == Airplane:
            if self.maxCountPassenger > other.maxCountPassenger:
                return True
            else:
                return False    

    def __le__(self,other):
            if type(other) == Airplane:
                if self.maxCountPassenger <= other.maxCountPassenger:
                    return True
                else:
                    return False    

    def __ge__(self,other):
            if type(other) == Airplane:
                if self.maxCountPassenger >= other.maxCountPassenger:
                    return True
                else:
                    return False  
                            
    def __add__(self,other):
            return Airplane(self.Passengers + other)
            
    def __sub__(self,other):
            if (self.Passengers - other) >= 0:
                return Airplane(self.Passengers - other)
                    
    def __iadd__(self,other):
            self.Passengers += other 
            return Airplane(self.Passengers) 
                    
    def __isub__(self,other):
            if (self.Passengers - other) >= 0:
                    self.Passengers -= other
                    return Airplane(self.Passengers)

a1 = Airplane('Boyng',25,525)
a2 = Airplane('Boyng',20,260)
a3 = Airplane('Airbus',103,750)
a4 = Airplane('Airbus',501,750)
print('type airplane a1 == type airplane a2 is',a1 == a2)

print('**** Comparison according to the maximum number of passengers on board ****')
print('the airplane a1 > airplane a2 is',a1 > a2)
print('the airplane a1 < the airplane a2 is',a1 < a2)
print('the airplane a1 >= the airplane a2 is',a1 >= a2)
print('the airplane a1 <= the airplane a2 is',a1 <= a2)
print (' ****************************************************************************')
number = random.randint(1,10)
a1.Passengers = a1.Passengers - number
print('after decreasing passengers by',number,' in the  airplane a1  =',a1.Passengers)

number = random.randint(1,25)
a2.Passengers = a2.Passengers + number
print('after increaseing passengers by',number,' in the  airplane a2  =',a2.Passengers)

number= random.randint(1,100)
a4.Passengers += number
print('expression (a4 += ',number,') is',a4.Passengers)

number= random.randint(1,100)
a3.Passengers -= number
print('expression (a3 -= ',number,') is',a3.Passengers)
