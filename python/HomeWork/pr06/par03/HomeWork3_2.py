class converC_F:
    count = 0

    def __init__(self,number) -> None:
        if (type(number) == int) or (type(number) ==float):
            self.number = number
        

    @staticmethod
    def F_C(numberF):
        converC_F.count+=1
        return  (numberF - 32)/1.8

    @staticmethod
    def C_F(numberC):
        converC_F.count+=1
        return  numberC * 1.8 + 32
    

    @staticmethod
    def get_count():
        return converC_F.count


tempC=converC_F.F_C(56.0)
print("The temperature in Celcius  = ",tempC)

tempF = converC_F.C_F(13.333)
print('The temperature in Fahrenheit = ',tempF)

print("The number of temperature counts =",converC_F.get_count())
