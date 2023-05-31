class ConverC_F:
    count = 0

    def __init__(self,number) -> None:
        if (type(number) == int) or (type(number) ==float):
            self.number = number
        

    @staticmethod
    def F_C(numberF):
        ConverC_F.count+=1
        return  (numberF - 32)/1.8

    @staticmethod
    def C_F(numberC):
        ConverC_F.count+=1
        return  numberC * 1.8 + 32
    

    @staticmethod
    def get_count():
        return ConverC_F.count



print("The temperature in Celcius  = ",ConverC_F.F_C(56.0))

print('The temperature in Fahrenheit = ',ConverC_F.C_F(13.34))

print("The number of temperature counts =",ConverC_F.get_count())
