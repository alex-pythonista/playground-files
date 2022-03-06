from vehical import Vehical

class Car(Vehical):

    def __init__(self, tireSize, engineType, gearType):
        self.tireSize = tireSize
        self.engineType = engineType
        self.gearType = gearType

    # Methods
    def wipe(self):
        print('wiping windshields...')

    def speedReading(self):
        print("Your speed: 63Kph")

car1 = Car(14, "Disel Engine", "Auto")
car1.start()
car1.wipe()
