class Car(object):
    def __init__(self,brand,colour,numberplate):
        self.brand = brand
        self.colour = colour
        self.numberplate = numberplate

    def setBrand(self,brand):
        self.brand = brand

    def setColor(self,color):
        self.colour = color

    def setNum(self,numberplate):
        self.numberplate = numberplate

    def getColour(self):
        return (self.colour)

    def getBrand(self):
        return(self.brand)

    def getNum(self):
        return(self.numberplate)

car1 = Car("Mercedece Benz", "white", "MH03")
car2 = Car("Honda Jazz", "off-white", "WB0523")
color = car1.getColour()
print(color)
car1.setColor("Red")
colour = car1.getColour()
print(colour)
nump = car2.getNum()
print(nump)
car2.setNum("CH04DA2121")
nump = car2.getNum()
print(nump)
