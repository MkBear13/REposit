class Director:
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getCar(self):
        car = Car()
        tires = self.__builder.getTires()
        car.setTires(tires)
        engine_type = self.__builder.getEngine_type()
        car.setEngine_type(engine_type)
        transmission = self.__builder.getTransmission()
        car.setTransmission(transmission)
        return car


class Car:
    def __init__(self):
        self.__tires = list()
        self.__engine_type = None
        self.__transmission = None

    def setTires(self, tires):
        self.__tires = tires

    def setEngine_type(self, engine_type):
        self.__engine_type = engine_type

    def setTransmission(self, transmission):
        self.__transmission = transmission

    def __str__(self):
        return 'Quantity of tires: {} Engine type: {} Transmission: {}'.format(self.__tires, self.__engine_type, self.__transmission)



class Builder:
    def getTires(self): pass

    def getEngine_type(self): pass

    def getTransmission(self): pass


class Auto_builder(Builder):
    def getTires(self):
        tires = 4
        return tires

    def getEngine_type(self):
        engine_type = 'petrol'
        return engine_type

    def getTransmission(self):
        transmission = 'auto'
        return transmission


class Moto_builder(Builder):
    def getTires(self):
        tires = 2
        return tires

    def getEngine_type(self):
        engine_type = 'petrol'
        return engine_type

    def getTransmission(self):
        transmission = 'manual'
        return transmission


def main():
    auto_builder = Auto_builder()
    director = Director()
    print("Auto")
    director.setBuilder(auto_builder)
    auto = director.getCar()
    print(auto)

    moto_builder = Moto_builder()
    director = Director()
    print("Motocycle")
    director.setBuilder(moto_builder)
    moto = director.getCar()
    print(moto)


if __name__ == "__main__":
    main()
