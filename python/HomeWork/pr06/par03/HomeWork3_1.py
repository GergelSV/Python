class Fraction:
    count = 0

    def __init__(self,number) -> None:
        self.number = number
        Fraction.count+=1

    @staticmethod
    def get_count():
        return Fraction.count



num1 = Fraction(5)
num2 = Fraction(4)
print("Count inilializathin class Fraction =",Fraction.get_count())
