class Wheel:
    def __init__(self,r,width,tirePressure) -> None:
        self.r = r
        self.width = width
        self.tirePressure = tirePressure

    def showInfo(self):
        print('Radius wheel =',self.r,'width =',self.width)

    def pumpUp(self,number):
        if (self.tirePressure + number< 2.5):
            return self.tirePressure + number


class Door:
    def __init__(self,powerWindow,handle,typeDoor) -> None:
        self.powerWindow = powerWindow
        self.handle = handle
        self.typeDoor = typeDoor

    def showInfo(self):
        print ('Door is ',self.typeDoor,'handle is ',self.handle,'powerWindow is',self.powerWindow)

    def moveWindow(self,directionMove):
        if directionMove == 1:
            print ("The window is open")
        elif directionMove == 2:
            print ("The window is close")


class Engine:
    def __init__(self,typeFuel,power,typeEngine) -> None:
        self.typeFuel = typeFuel
        self.power = power
        self.typeEngine = typeEngine

    def showInfo(self):
        print ('Engine work is',self.typeFuel,'it power =',self.power,'horses power and engine type=',self.typeEngine )

    def startStopEngine (self,keyTurn):
        if keyTurn=='up':
            print ('The engine is start')
        elif keyTurn=='dowm':
            print ('The engine is stop')



class Avto(Engine,Wheel,Door):
    def __init__(self, typeFuel, power, typeEngine,r,width,tirePressure,powerWindow,handle,typeDoor,color,marka,countWheel,countDoor,) -> None:
        Engine.__init__(typeFuel, power, typeEngine)
        Wheel.__init__(self,r,width,tirePressure)
        Door.__init__(powerWindow,handle,typeDoor)
        self.color = color
        self.marka = marka
        self.countWheel = countWheel
        self.countDoor = countDoor

    def showInfo(self):
        Engine.showInfo(self)
        Door.showInfo(self)
        Wheel.showInfo(self)
        print('color avto is ',self.color,'marka = ',self.marka,' car have ',self.countDoor,'doors,',self.countWheel,'wheel')


car = Avto('дизель',1.6,'інжектор',15,1,1,'c замком',)







    



        