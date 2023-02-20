from abc import ABCMeta, abstractmethod


class Person(metaclass=ABCMeta):
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def wear(self):
        print("Wear")


class Engineer(Person):
    def __init__(self, name, skill):
        super().__init__(name)
        self._skill = skill

    def getSkill(self):
        return self._skill

    def wear(self):
        print(f"I'm {self.getSkill()} Engineer {self._name} end=")
        super().wear()


class Teacher(Person):
    def __init__(self, name, title):
        super().__init__(name)
        self._title = title

    def getTitle(self):
        return self._title

    def wear(self):
        print(f"I'm {self._name} { self._title} end=")
        super().wear()


class ClothingDecorator(Person):
    def __init__(self, person):
        self._decorated = person

    def wear(self):
        self._decorated.wear()
        self.decorate()

    @abstractmethod
    def decorate(self):
        pass


class CasualPantDecorator(ClothingDecorator):
    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("Blue Pant")


class BeltDecorator(ClothingDecorator):
    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("Black Belt")


class LeatherShoesDecorator(ClothingDecorator):
    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("Deep Color Shoes")


class KnittedSweaterDecorator(ClothingDecorator):
    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("Purple Red Sweater")


class WhiteShirtDecorator(ClothingDecorator):
    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("White T-Shirt")


class GlassesDecorator(ClothingDecorator):
    def __init__(self, person):
        super().__init__(person)

    def decorate(self):
        print("Black Glasses")
if __name__ == "__main__":
    tony = Engineer("Tony","CS")
    pant = CasualPantDecorator(tony)
    belt = BeltDecorator(pant)
    belt.wear()