class Organization:
    def __init__(self,name,kind_of_aktivity,director,accountant,count_worker,telefon,adress,email) -> None:
        self.name = name
        self.kind_of_aktivity = kind_of_aktivity
        self.director = director
        self.accountant = accountant
        self.count_worker = count_worker
        self.telefon = telefon
        self.adress = adress
        self.email = email
      
    
    def show_info(self):
        print (' Найменування підприємства -',self.name,'основний вид діяльності -',self.kind_of_aktivity,'\n',\
            'ПІБ директора -',self.director,'ПІБ бухгалтера -',self.accountant,'\n','кількість робітників -',self.count_worker,\
            '\n','телефон : ',self.telefon,'\n','адреса :',self.adress,'\n','електрона пошта - ' ,self.email, '\n',end=' ')


