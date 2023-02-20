from copy import copy, deepcopy


class Clone:
    """Shallow Copy"""

    def shallowClone(self):
        return copy(self)
    """Deep Copy"""

    def deepClone(self):
        return deepcopy(self)


class Person(Clone):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def showMyself(self):
        print(f"Id={id(self)} Name={self._name} age={self._age}")

    def coding(self):
        print(f"Id={id(self)} Coding")

    def reading(self):
        print(f"Id={id(self)} Reading")

    def playing(self):
        print(f"Id={id(self)} Playing")


if __name__ == "__main__":
    p = Person("One", 2)
    print(f"P's id ={id(p)}")
    p.showMyself()
    p.coding()
    
    p1 = p.shallowClone()
    print(f"P1's id ={id(p1)}")
    p1.showMyself()
    p1.reading()
    
    p2 = p.deepClone()
    print(f"P2's id ={id(p2)}")
    p2.showMyself()
