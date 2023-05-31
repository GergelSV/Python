class Flat:
    def __init__(self,square,price) -> None:
        self.square = square
        self.price = price

    def __eq__(self, __value: object) -> bool:
        if type(__value) == Flat:
            if self.square == __value.square:
                return True
            else:
                return False
            
    def __ne__(self, __value: object) -> bool:
        if type(__value) == Flat:
            if self.square != __value.square:
                return True
            else:
                return False

    def __lt__(self,other):
        if type(other) == Flat:
            if self.price < other.price:
                return True
            else:
                return False

    def __gt__(self,other):
        if type(other) == Flat:
            if self.price > other.price:
                return True
            else:
                return False    

    def __le__(self,other):
            if type(other) == Flat:
                if self.price <= other.price:
                    return True
                else:
                    return False    

    def __ge__(self,other):
            if type(other) == Flat:
                if self.price >= other.price:
                    return True
                else:
                    return False  
                            
kv1 = Flat(65,5500)
kv2 = Flat(32,3500)
  

print('square kv1 == square kv2 is',kv1 == kv2)
print('square kv1 != square kv2 is',kv1 != kv2)
print('price kv1 > price kv2 is',kv1 > kv2)
print('price kv1 < price kv2 is',kv1 < kv2)
print('price kv1 >= price kv2 is',kv1 >= kv2)
print('price kv1 <= price kv2 is',kv1 <= kv2)
