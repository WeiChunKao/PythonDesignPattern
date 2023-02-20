from abc import ABCMeta, abstractmethod


class Flyweight(metaclass=ABCMeta):
    @abstractmethod
    def operation(self, extrinsicState):
        pass


class FlyweightImpl(Flyweight):
    def __init__(self, color):
        self._color = color

    def operation(self, extrinsicState):
        print(f" {extrinsicState} gets {self._color}")


class FlyweightFactory:
    def __init__(self):
        self._flyweights = {}

    def getFlyweights(self, key):
        pigment = self._flyweights.get(key)
        if pigment is None:
            pigment = FlyweightImpl(key)
            return pigment
if __name__ == '__main__':
    factory = FlyweightFactory()
    pigmentRed = factory.getFlyweights("Red")
    pigmentRed.operation("Dream Team")
