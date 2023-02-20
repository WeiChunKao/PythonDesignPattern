from abc import ABCMeta, abstractmethod
from enum import Enum


class PenType(Enum):
    PenTypeLine = 1
    PenTypeRect = 2
    PenTypeEllipse = 3


class Pen(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def getType(self):
        pass

    def getName(self):
        return self.name


class LinePen(Pen):
    def __init__(self, name):
        super().__init__(name)

    def getType(self):
        return PenType.PenTypeLine


class RectanglePen(Pen):
    def __init__(self, name):
        super().__init__(name)

    def getType(self):
        return PenType.PenTypeRect


class EllipsePen(Pen):
    def __init__(self, name):
        super().__init__(name)

    def getType(self):
        return PenType.PenTypeEllipse


class PenFactory:
    def __init__(self):
        self._pens = {}

    def createPen(self, penType):
        if self._pens.get(penType) is None:
            if penType == PenType.PenTypeLine:
                pen = LinePen("Line")
            elif penType == PenType.PenTypeRect:
                pen = RectanglePen("Rect")
            elif penType == PenType.PenTypeEllipse:
                pen = EllipsePen("Ellipse")
            else:
                pen = Pen("")
            self._pens[penType] = pen
        return self._pens[penType]

if __name__ == "__main__":
    factory = PenFactory()
    linePen = factory.createPen(PenType.PenTypeLine)
    print(f"Name:{linePen.getName()} Type:{linePen.getType()}")