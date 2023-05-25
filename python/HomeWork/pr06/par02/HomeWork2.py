import random
class Ship:
    def __init__(self,name,Production_year,displacement,speed,) -> None:
        self.name = name
        self.Production_year = Production_year
        self.displacement = displacement
        self.speed = speed
        self.__id = random.randint(1,100)

    def show_info(self):
        print(self.__id,self.name,self.Production_year,self.displacement,self.speed,end=' ')   


class Frigate (Ship):
    def __init__(self, name, Production_year, displacement, speed,sail) -> None:
        super().__init__(name, Production_year, displacement, speed)
        self.sail = sail

    def show_info(self):
        super().show_info()
        print(self.sail)
    
    def put_sail(self,new_sail):
        self.sail = new_sail

class Destroyer(Ship):
    def __init__(self, name, Production_year, displacement, speed,torpedo) -> None:
        super().__init__(name, Production_year, displacement, speed)
        self.torpedo = torpedo

    def show_info(self):
        super().show_info()
        print(self.torpedo)

    def put_torpedo(self,new_torpedo):
        self.torpedo = new_torpedo


class Cruiser(Ship):
    def __init__(self, name, Production_year, displacement, speed,machine_guns,guns,rockets) -> None:
        super().__init__(name, Production_year, displacement, speed)
        self.machine_guns = machine_guns
        self.guns = guns
        self.rockets = rockets

    def show_info(self):
        super().show_info()
        print(self.machine_guns,self.guns,self.rockets)

    def put_rocket(self,new_rocket):
        self.machine_guns=new_rocket

Ship1 = Frigate("Гетьман Сагайдачний",1995,"200 тон","20 вузлів на годину","білі вітрила")   
Ship1.show_info()
Ship1.put_sail("багряні вітрила")
Ship1.show_info()

Ship2 = Destroyer("Арлі Берк",1988,"3 200 тон","30 вузлів на годину","MU90 Impact")
Ship2.show_info()
Ship2.put_torpedo("Mark 48")
Ship2.show_info()       


Ship3 = Cruiser("Україна",1990,"9 800 тон","32,5 вузлів на годину","130 mm","30 mm","С-300 Ф")
Ship3.show_info()
Ship3.put_rocket("ATACMS")
Ship3.show_info()     

