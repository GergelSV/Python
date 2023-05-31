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
            return self.Passengers + other
            
    def __sub__(self,other):
            if (self.Passengers - other) >= 0:
                self.Passengers -=  other
                return self
                    
    def __iadd__(self,other):
            self.Passengers += other 
            return self 
                    
    def __isub__(self,other):
            if (self.Passengers - other) >= 0:
                    self.Passengers -= other
                    return self

a1 = Airplane('Boyng',25,525)
a2 = Airplane('Boyng',20,260)
a3 = Airplane('Airbus',103,750)
a4 = Airplane('Airbus',501,750)
print('type airplane a1 == type airplane a2 is',a1 == a2)
print('the maximum possible number of passengers on board  a1 > maximum possible number of passengers on board a2 is',a1 > a2)
print('the maximum possible number of passengers on board  a1 < maximum possible number of passengers on board a2 is',a1 < a2)
print('the maximum possible number of passengers on board  a1 >= maximum possible number of passengers on board a2 is',a1 >= a2)
print('the maximum possible number of passengers on board  a1 <= maximum possible number of passengers on board a2 is',a1 <= a2)

numberPassengers = random.randint(1,10)
a1.Passengers = a1.Passengers - numberPassengers
print('after decreasing passengers by',numberPassengers,' in the  airplane a1  =',a1.Passengers)

numberPassengers = random.randint(1,25)
a2.Passengers = a2.Passengers + numberPassengers
print('after increaseing passengers by',numberPassengers,' in the  airplane a2  =',a2.Passengers)

#print ('type a2 =',type(a2))
number= random.randint(1,100)
a4.Passengers += number
print('expression (a4 += ',number,') is',a4.Passengers)

number= random.randint(1,100)
a3.Passengers -= number
print('expression (a3 -= ',number,') is',a3.Passengers)
