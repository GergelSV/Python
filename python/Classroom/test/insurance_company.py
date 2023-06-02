from opganization import Organization
class Insurance_Company (Organization):
    def __init__(self, name, kind_of_aktivity, director, accountant, count_worker, telefon, adress, email,insurance_policy) -> None:
        super().__init__(name, kind_of_aktivity, director, accountant, count_worker, telefon, adress, email)
        self.insurance_policy =insurance_policy
    
    def show_info(self):
        super().show_info()
        print('Види договірів страхування :',self.insurance_policy)

    def add_insurance_policy(self,other):
        if type(other) == str:
            self.insurance_policy.append(other)
            return Insurance_Company(self.name, self.kind_of_aktivity, self.director, self.accountant, self.count_worker, self.telefon, self.adress, self.email,self.insurance_policy) 

  

    
