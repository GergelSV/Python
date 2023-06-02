from factory import Factory
class ShipbuilC(Factory):
    def __init__(self, name, kind_of_aktivity, director, accountant, count_worker, telefon, adress, email, products,shipyard) -> None:
        super().__init__(name, kind_of_aktivity, director, accountant, count_worker, telefon, adress, email, products)
        self.shipyard = shipyard

    def show_info(self):
        super().show_info()
        print(' кількість верфей -',self.shipyard)

    def add_shipyard(self,count_shipyard):                # збільшення кількості верфей
                if type(count_shipyard) == int:
                        self.shipyard+=count_shipyard
                        return ShipbuilC(self.name, self.kind_of_aktivity, self.director, self.accountant, self.count_worker, self.telefon, self.adress, self.email, self.products,self.shipyard)
                

    def __le__(self,other):
                if type(other) == ShipbuilC:
                        if self.count_worker <= other.count_worker:
                            return True
                        else:
                            return False    

    def __lt__(self,other):
            if type(other) == ShipbuilC:
                    if self.count_worker < other.count_worker:
                          return True
                    else:
                        return False    
                    
    def __gt__(self,other):
           if type(other) == ShipbuilC:
                if self.count_worker > other.count_worker:
                        return True
                else:
                    return False               
                
    def __ge__(self,other):
           if type(other) == ShipbuilC:
                if self.count_worker >= other.count_worker:
                        return True
                else:
                    return False     
    
    def __eq__(self,other):
           if type(other) == ShipbuilC:
                if self.count_worker == other.count_worker:
                        return True
                else:
                    return False                 
    