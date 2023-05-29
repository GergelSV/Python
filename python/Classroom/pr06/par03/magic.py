from re import A


class MyNumber:
    def __init__(self, n) -> None:
        self.n = n

    def __str__(self):
        return str(self.n)
    def __add__(self, o):
        return MyNumber(self.n + o.n)

a = MyNumber(20)
b = a + a
print(b)