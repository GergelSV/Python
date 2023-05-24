import random
class Money:
    def __init__(self,name,integer,fractional,exchange):
        self.name = name
        self.integer = integer
        self.fractional = fractional
        self.exchange = exchange
        self.__id = random.randint(1,10)
    
    def show_info(self):
        print("ID - ",self.__id," Name money is ",self.name," count = ",self.integer,'.',self.fractional,' dollar exchange rate = ',self.exchange,sep='',)

    def put_exchange(self,new_exchange):
        self.exchange = new_exchange

    def displaySumOnScreen(self):
        print('сумма = ',self.integer,'.',self.fractional,' ',self.name,sep='')

oper1 = Money('грн',"25","05","36,5")
oper1.displaySumOnScreen()
oper1.show_info()

