import random
class Device:
    def __init__(self,name,version,manufacturer,weight,price):
        self.name = name
        self.version = version
        self.manufacturer = manufacturer
        self.weight = weight
        self.price = price
        self.__id = random.randint(1,10)
    
    def show_info(self):
        print(self.__id,self.name,self.version,self.manufacturer,self.weight,self.price,end=' ')

    def put_price(self,new_price):
        self.price = new_price


class CoffeeMachine(Device):
    def __init__(self, name, version, manufacturer,  weight, price,typeOfCoffeeDrink,coffeeGrinder,cappuccinatore):
        super().__init__(name, version,manufacturer,  weight, price)
        self.typeOfCoffeeDrink = typeOfCoffeeDrink
        self.coffeeGrinder = coffeeGrinder
        self.cappuccinatore = cappuccinatore
        self.__portionCounter = random.randint(1,100)

    def show_info(self):
        super().show_info()
        print(self.typeOfCoffeeDrink,self.coffeeGrinder,self.cappuccinatore," кількість зварених чашок  = ",self.__portionCounter)  
    
    def change_cappuccnatore(self,new_cappuccinatore):
        self.cappuccinatore = new_cappuccinatore 

class Blender(Device):
    def __init__(self, name, version, manufacturer, weight, price,speed,nozzle):
        super().__init__(name, version, manufacturer,weight, price)
        self.speed = speed
        self.nozzle = nozzle

    def show_info(self):
        super().show_info()
        print(self.speed,self.nozzle)

    def put_nozzle(self,new_nozzle):
        self.nozzle = new_nozzle

class MeatGrinder(Device):
    def __init__(self, name, version, manufacturer, weight, price,power,typeOofMmeat):
        super().__init__(name, version, manufacturer, weight, price)
        self.power = power
        self.typeOfMeat = typeOofMmeat

    def show_info(self):
        super().show_info()
        print(self.power,self.typeOfMeat)

    def put_type_of_meat(self,new_meat):
        self.typeOfMeat = new_meat


cofmashin=CoffeeMachine('Кавомашина',"LatteGo 5400","Philips","8 кг","31 999 грн ","12 видів кави "," з млинком"," з капучінатором ")

cofmashin.show_info()
cofmashin.put_price("20 000 грн ")
cofmashin.change_cappuccnatore("без капучінатора")
cofmashin.show_info()

#print(CoffeeMachine.mro())

Dev_blend=Blender('Блендер',"Brawn 530","Philips","1 кг","1 999 грн "," 15 швідкостей ","венчік")

Dev_blend.show_info()
Dev_blend.put_nozzle("для пюре ")
Dev_blend.show_info()
#print(Blender.mro())

Dev_meat_g=MeatGrinder('Мясорубка',"Brawn 630","Philips","3 кг","5 999 грн "," 1500 ","яловичина")

Dev_meat_g.show_info()
Dev_meat_g.put_type_of_meat("курятина ")
Dev_meat_g.show_info()
#print(MeatGrinder.mro())

