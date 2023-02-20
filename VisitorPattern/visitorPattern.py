from abc import ABCMeta, abstractmethod


class Visitor(metaclass=ABCMeta):
    @abstractmethod
    def visit(self, data):
        pass


class DataNode(metaclass=ABCMeta):
    def accept(self, visitor: Visitor):
        visitor.visit(self)


class ObjectStructure:
    def __init__(self):
        self._data = []

    def add(self, data):
        self._data.append(data)

    def action(self, visitor):
        for data in self._data:
            data.accept(visitor)


class DesignPattern(DataNode):
    def getName(self):
        return "DesignPattern"


class Engineer(Visitor):
    def visit(self, book):
        print(f"Engineer reads book:{book.getName()}")


class ProductManager(Visitor):
    def visit(self, book):
        print(f"ProductManager reads book:{book.getName()}")


class OtherFriend(Visitor):
    def visit(self, book):
        print(f"IT friends read book:{book.getName()}")


if __name__ == "__main__":
    book = DesignPattern()
    objMgr = ObjectStructure()
    objMgr.add(book)
    objMgr.action(Engineer())
    objMgr.action(ProductManager())
    objMgr.action(OtherFriend())
