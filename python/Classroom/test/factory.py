from opganization import Organization
class Factory(Organization):        
        def __init__(self, name, kind_of_aktivity, director, accountant, count_worker, telefon, adress, email,products) -> None:
                super().__init__(name, kind_of_aktivity, director, accountant, count_worker, telefon, adress, email)
                self.products = products

        def show_info(self):
                super().show_info()
                print('виготовляє наступну продукцію - ',self.products)
        
        def hiring_for_a_job(self,count_people):                # прийом на роботу людей - додавання людей
                if type(count_people) == int:
                        self.count_worker+=count_people
                        return Factory(self.name, self.kind_of_aktivity, self.director, self.accountant, self.count_worker, self.telefon, self.adress, self.email,self.products)
                
        def dismissal_for_a_job(self,count_people):                # звільнення з роботи людей 
                if type(count_people) == int:
                        self.count_worker-=count_people
                        return Factory(self.name, self.kind_of_aktivity, self.director, self.accountant, self.count_worker, self.telefon, self.adress, self.email,self.products)
                        
