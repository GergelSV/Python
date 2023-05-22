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
    # def __init__(self) -> None:
    #     super().__init__()
      
    def __init__(self, hand, paw, cover, tail, family,characteristic) -> None:
        super().__init__(hand, paw, cover, tail, family)
        self.characteristic=characteristic

    def put_paw(self,y):
        self.paw=y


    def show_info(self):
        super().show_info()
        print (self.jungle_dweller)
        

class Crocodile(Animal):
    def __init__(self) -> None:
        super().__init__()
            
    def show_info(self):
        super().show_info()
        

class Kangaroo(Animal):
    def __init__(self,length) -> None:
        super().__init__()
        self.lengh =length
    
    def show_info(self):
        super().show_info()
        print(self.lengh)        

#animal1=Animal('Плямиста голова з вушками-китицями','міцні лапи','коротка  плямиста вовна','гнучкий хвіст','сімейство котячих')
#animal1.show_info()
#animal2=Tiger()
animal2=Tiger('Плямиста голова з вушками-китицями','міцні лапи','коротка  плямиста вовна','гнучкий хвіст','сімейство котячих','самое быстрое животное')
animal2.show_info()
animal2.put_paw('короткі лапи')
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