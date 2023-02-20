from abc import ABCMeta, abstractmethod
class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, observable, objcet):
        pass

class Observalbe:
    def __init__(self):
        self.observers = []
    def addObserver(self, observer):
        self.observers.append(observer)
    def removeObserver(self, observer):
        self.observers.remove(observer)
    def notifyObserver(self, object = 0):
        for o in self.observers:
            o.update(self, object)