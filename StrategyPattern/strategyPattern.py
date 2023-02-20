from abc import ABCMeta, abstractmethod


class IVehicle(metaclass=ABCMeta):
    @abstractmethod
    def running(self):
        pass


class SharedBicycle(IVehicle):
    def running(self):
        print("SharedBicycle", end=" ")


class ExpressBus(IVehicle):
    def running(self):
        print("Bus", end=" ")


class Express(IVehicle):
    def running(self):
        print("Express", end=" ")


class Subway(IVehicle):
    def running(self):
        print("Survival", end=" ")


class Classmate:
    def __init__(self, name, vehicle):
        self._name = name
        self._vehicle = vehicle

    def attendTheDinner(self):
        print(self._name, end=" ")
        self._vehicle.running()
        print("Dinner", end=" ")


if __name__ == "__main__":
    sharedBicycle = SharedBicycle()
    joe = Classmate("Joe", sharedBicycle)
    joe.attendTheDinner()
