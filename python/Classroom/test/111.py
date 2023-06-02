import random
class Person:
    def __init__(self, firstName, lastName, age):
# public properties
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
#private properties
        self.__personID=random.randint(1,100)
#private methods
    def __getID(self):
        return f"{self.__personID}\n"
# public methods
    # def getInfo(self):
    #     return f"{self.__getID()}
    #              {self.firstName}
    #              {self.lastName}
    #              {self.age}."
    
person1=Person("Joe","Black",30)
person1.__personID =100
print(person1.__getID())
