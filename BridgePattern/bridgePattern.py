from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):
    def __init__(self, color):
        self._color = color

    @abstractmethod
    def getShapeType(self):
        pass

    def getShapeInfo(self):
        return f"{self._color.getColor()} {self.getShapeType()}"


class Rectangle(Shape):
    def __init__(self, color):
        super().__init__(color)

    def getShapeType(self):
        return "Rectangle"


class Ellipse(Shape):
    def __init__(self, color):
        super().__init__(color)

    def getShapeType(self):
        return "Ellipse"


class Color(metaclass=ABCMeta):
    @abstractmethod
    def getColor(self):
        pass


class Red(Color):
    def getColor(self):
        return "Red"


class Green(Color):
    def getColor(self):
        return "Green"

if __name__ == "__main__":
    redRect = Rectangle(Red())
    print(f"redRect:{redRect.getShapeInfo()}")
    greenEllipse = Ellipse(Green())
    print(f"greenEllipse:{greenEllipse.getShapeInfo()}")