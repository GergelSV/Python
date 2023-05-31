from opganization import Organization
class Insurance_Company (Organization):
    def __init__(self,insurance_policy) -> None:
        super().__init__()
        self.insurance_policy =insurance_policy

    def show_info(self):
        super().show_info()
        print('Договір страхування',self.insurance_policy)

  

    
