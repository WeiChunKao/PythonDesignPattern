from abc import ABCMeta, abstractmethod


class Toy(metaclass=ABCMeta):
    def __init__(self, name):
        self._name = name
        self._component = []

    def getName(self):
        return self._name

    def addComponent(self, component, count=1, unit='classifier'):
        self._component.append([component, count, unit])

    @abstractmethod
    def features(self):
        pass


class Car(Toy):
    def features(self):
        print(f"{self._name} Car")


class Manor(Toy):
    def features(self):
        print(f"{self._name} Manor")


class ToyBuilder(metaclass=ABCMeta):
    @abstractmethod
    def buildProduct(self):
        pass


class CarBuilder(ToyBuilder):
    def buildProduct(self):
        car = Car("Mini Car")
        print(f"Build {car.getName()} ...")
        car.addComponent("Wheels", 4)
        car.addComponent("Body", 1)
        car.addComponent("Engine", 1)
        car.addComponent("Steering Wheel", 1)
        return car


class ManorBuilder(ToyBuilder):
    def buildProduct(self):
        manor = Manor("Little Manor")
        print(f"Build {manor.getName()} ...")
        manor.addComponent("Dining Room", 1, "room")
        manor.addComponent("Bed Room", 1, "room")
        manor.addComponent("Kitchen", 1, "room")
        return manor


class BuilderMgr:
    def __init__(self):
        self._carBuilder = CarBuilder()
        self._manorBuilder = ManorBuilder()

    def buildCar(self, num):
        count = 0
        products = []
        while count < num:
            car = self._carBuilder.buildProduct()
            products.append(car)
            count += 1
            print(f"Finish Building {count} vehicle {car.getName()}")
        return products

    def buildManor(self, num):
        count = 0
        products = []
        while count < num:
            manor = self._manorBuilder.buildProduct()
            products.append(manor)
            count += 1
            print(f"Finish Building {count} classifier {manor.getName()}")
        return products

if __name__ == "__main__":
    builderMgr = BuilderMgr()
    builderMgr.buildManor(2)
    print()
    builderMgr.buildCar(4)