import random
class conver_M_ES:
    count = 0

    def __init__(self,number) -> None:
        if (type(number) == int) or (type(number) ==float):
            self.number = number
        

    @staticmethod
    def inch_to_sm(number):
        conver_M_ES.count+=1
        return  number * 2.54
    
    @staticmethod
    def sm_to_inch(number):
        conver_M_ES.count+=1
        return  number / 2.54
    
    @staticmethod
    def sm_to_foot(number):
        conver_M_ES.count+=1
        return  number / 30.48
    
    @staticmethod
    def foot_to_sm(number):
        conver_M_ES.count+=1
        return  number * 30.48
    
    @staticmethod
    def km_to_mile(number):
        conver_M_ES.count+=1
        return number / 1.609
    
    @staticmethod
    def mile_to_km(number):
        conver_M_ES.count+=1
        return number * 1.609    
    
    @staticmethod
    def litr_to_gallon(number):
        conver_M_ES.count+=1
        return number / 3.785
    
    @staticmethod
    def gallon_to_litr(number):
        conver_M_ES.count+=1
        return number * 3.785   

 
    @staticmethod
    def get_count():
        return conver_M_ES.count


number = random.randint(1,999)
print ("Сonversion result ",number,' sm ','=',conver_M_ES.sm_to_inch(number),'in')

number = random.randint(1,999)
print ("Сonversion result ",number,' in ','=',conver_M_ES.inch_to_sm(number),'sm')

number = random.randint(1,999)
print ("Сonversion result ",number,' sm ','=',conver_M_ES.sm_to_foot(number),'ft')

number = random.randint(1,999)
print ("Сonversion result ",number,' ft ','=',conver_M_ES.foot_to_sm(number),'sm')

number = random.randint(1,999)
print ("Сonversion result ",number,' km ','=',conver_M_ES.km_to_mile(number),'mi')

number = random.randint(1,999)
print ("Сonversion result ",number,' mi ','=',conver_M_ES.mile_to_km(number),'km')

number = random.randint(1,999)
print ("Сonversion result ",number,' gal ','=',conver_M_ES.gallon_to_litr(number),'l')

number = random.randint(1,999)
print ("Сonversion result ",number,' l ','=',conver_M_ES.litr_to_gallon(number),'gal')

