class Organization:
    def __init__(self,__id,name,kind_of_aktivity,director,accountant,count_worker) -> None:
        self.__d = __id
        self.name = name
        self.kind_of_aktivity = kind_of_aktivity
        self.director = director
        self.accountant = accountant
        self.count_worker = count_worker
    
    def show_info(self):
        print('id =',self.__id,'найменування підприємства -',self.name,'основний вид діяльності -',self.kind_of_aktivity,'ПІБ директора ',self.director,'ПІБ бухгалтера',self.accountant,'кількість робітників',self.count_worker)

    
