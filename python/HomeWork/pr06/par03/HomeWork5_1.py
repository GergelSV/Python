
class Circle:
    def __init__(self,r,circumference) -> None:
        self.r = r
        self.circumference = circumference
    
    def __eq__(self, __value: object) -> bool:
        if type(__value) == Circle:
            if self.r == __value.r:
                return True
            else:
                return False
            
    


a1 = Circle(5,25)
a2 = Circle(5,20)

print(a1 == a2)

    





# class Money:
#     def __init__(self,name,integer_part,fractional_part,exchange):
#         self.name = name
#         self.integer_part = integer_part
#         self.fractional_part = fractional_part
#         self.exchange = exchange
#         self.__id = random.randint(1,10)
    
#     def show_info(self):
#         print("ID - ",self.__id," Name money is ",self.name," count = ",self.integer_part,'.',self.fractional_part,' dollar exchange rate = ',self.exchange,sep='',)

#     def put_integer_part(self,new_int_part):
#         self.integer_part = new_int_part

#     def put_fractional_part(self,new_fract_part):
#         self.fractional_part = new_fract_part
    

#     def displaySumOnScreen(self):
#         print('сумма = ',self.integer_part,'.',self.fractional_part,' ',self.name,sep='')

# oper1 = Money('грн',"25","05","36,5")
# oper1.displaySumOnScreen()
# oper1.show_info()

# oper1.put_integer_part(356)
# oper1.displaySumOnScreen()

# oper1.put_fractional_part(26)
# oper1.displaySumOnScreen()

# oper1.show_info()


