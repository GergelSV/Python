class fraction:
    count = 0

    def __init__(self,number) -> None:
        self.number = number
        fraction.count+=1

    @staticmethod
    def get_count():
        return fraction.count



num1 = fraction(5)
num2 = fraction(4)
print("Count inilializathin class fraction =",fraction.get_count())
