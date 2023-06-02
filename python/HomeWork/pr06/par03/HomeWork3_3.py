import random
class Conver_M_ES:
    count = 0

    def __init__(self,number) -> None:
        if (type(number) == int) or (type(number) ==float):
            self.number = number
        

    @staticmethod
    def inch_to_sm(number):
        Conver_M_ES.count+=1
        return  number * 2.54
    
    @staticmethod
    def sm_to_inch(number):
        Conver_M_ES.count+=1
        return  number / 2.54
    
    @staticmethod
    def sm_to_foot(number):
        Conver_M_ES.count+=1
        return  number / 30.48
    
    @staticmethod
    def foot_to_sm(number):
        Conver_M_ES.count+=1
        return  number * 30.48
    
    @staticmethod
    def km_to_mile(number):
        Conver_M_ES.count+=1
        return number / 1.609
    
    @staticmethod
    def mile_to_km(number):
        Conver_M_ES.count+=1
        return number * 1.609    
    
    @staticmethod
    def litr_to_gallon(number):
        Conver_M_ES.count+=1
        return number / 3.785
    
    @staticmethod
    def gallon_to_litr(number):
        Conver_M_ES.count+=1
        return number * 3.785   

 
    @staticmethod
    def get_count():
        return Conver_M_ES.count


number = random.randint(1,999)
print ("Conversion result ",number,' sm ','=',Conver_M_ES.sm_to_inch(number),'in')

number = random.randint(1,999)
print ("Conversion result ",number,' in ','=',Conver_M_ES.inch_to_sm(number),'sm')

number = random.randint(1,999)
print ("Conversion result ",number,' sm ','=',Conver_M_ES.sm_to_foot(number),'ft')

number = random.randint(1,999)
print ("Conversion result ",number,' ft ','=',Conver_M_ES.foot_to_sm(number),'sm')

number = random.randint(1,999)
print ("Conversion result ",number,' km ','=',Conver_M_ES.km_to_mile(number),'mi')

number = random.randint(1,999)
print ("Conversion result ",number,' mi ','=',Conver_M_ES.mile_to_km(number),'km')

number = random.randint(1,999)
print ("Conversion result ",number,' gal ','=',Conver_M_ES.gallon_to_litr(number),'l')

number = random.randint(1,999)
print ("Conversion result ",number,' l ','=',Conver_M_ES.litr_to_gallon(number),'gal')

