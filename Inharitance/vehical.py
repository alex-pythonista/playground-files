# Best functions are those that have no parameters

class Vehical():

    def __init__(self):
        self.color = "black"
        self.licenseNumber = "BD-"
        self.engineNumber = "EN-"
        self.cc = 1500
    
    # Methods
    def start(self):
        print("Engine has started!")
    
    def left(self):
        print('turned left!')

    def right(self):
        print('turned left!')

    def stop(self):
        print('Engine has stoped!')

v1 = Vehical()
v1.color = "White"
v1.cc = 135
print(v1.cc)