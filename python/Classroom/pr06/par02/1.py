import random
class Animal:
    def __init__(self, hand, paw, cover,tail,family ) -> None:
        self.hand = hand
        self.paw = paw
        self.cover = cover
        self.tail = tail
        self.family=family
        self.__id=random.randint(1,10)
    
    def show_info(self):
        print(self.__id,self.hand, self.paw, self.cover, self.tail,self.family, end=' ')

class Tiger(Animal):
         
    def __init__(self, hand, paw, cover, tail, family,roars) -> None:
        super().__init__(hand, paw, cover, tail, family)
        self.roars=roars

    def put_paw(self,y):
        self.paw=y


    def show_info(self):
        super().show_info()
        print (self.roars)
        

class Crocodile(Animal):
    def __init__(self, hand, paw, cover, tail, family,crawls) -> None:
        super().__init__(hand, paw, cover, tail, family)
        self.crawls=crawls
            
    def show_info(self):
        super().show_info()
        print(self.crawls)
        

class Kangaroo(Animal):
    def __init__(self, hand, paw, cover, tail, family,jumps) -> None:
        super().__init__(hand, paw, cover, tail, family)
        self.jumps=jumps
    
    def show_info(self):
        super().show_info()
        print(self.jumps)        

animal1=Kangaroo('Голова з довгими вухами','міцні задні лапи, короткі передні','коротка вовна','гнучкий хвіст, як нога','сімейство сумчатих','високо стрибає')
animal1.show_info()

animal2=Tiger('Плямиста голова з вушками-китицями','міцні лапи','коротка  плямиста вовна','гнучкий хвіст','сімейство котячих','гучно ричить')
animal2.show_info()
animal2.put_paw('пруткі лапи')
animal2.show_info()





# class zav_kaf(Teacher):
#     def __init__(self, name, surname, age, tel, disc) -> None:
#         Persona.__init__(self, name, surname, age, tel)
#         self.disc = 123
#         print(zav_kaf.mro())



# teacher = Teacher("Dmytro", 'Medvediev', 37, '+380688535681', 'QA')
# teacher.show_info()
# persona = Persona("Dmytro", 'Medvediev', 37, '+380688535681')
# persona.show_info()
# zav = zav_kaf("Dmytro", 'Medvediev', 37, '+380688535681', 'QA')
# zav.show_info()

# class Base:
#     pass

# class Camera:
#     def __init__(self, r) -> None:
#         self.__size = r
#     def get_info(self):
#         print('Camera', self.__size)

# class Radio(Base):
#     def __init__(self) -> None:
#         pass
#     def get_info(self):
#         # print('Radio', self.__size)
#         print('radio', self)

# class Telephon(Camera, Radio):
#     def __init__(self, size) -> None:
#         Radio.__init__(self)
#         Camera.__init__(self, size)
#     def get_info(self):
#         Radio.get_info(self)
#         Camera.get_info(self)

# tel = Telephon(1)
# tel.get_info()
# print('tel  ', tel)
# print(Telephon.mro())