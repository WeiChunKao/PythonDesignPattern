from abc import ABCMeta, abstractmethod


class Request:
    def __init__(self, name, dayoff, reason):
        self._name = name
        self._dayoff = dayoff
        self._reason = reason
        self._leader = None

    def getName(self):
        return self._name

    def getDayoff(self):
        return self._dayoff

    def getReason(self):
        return self._reason


class Responsible(metaclass=ABCMeta):
    def __init__(self, name, title):
        self._name = name
        self._title = title
        self._nextHandler = None

    def getName(self):
        return self._name

    def getTitle(self):
        return self._title

    def setNextHandler(self, nextHandler):
        self._nextHandler = nextHandler

    def getNextHandler(self):
        return self._nextHandler

    def handleRequest(self, request):
        self._handleRequestImpl(request)
        if self._nextHandler is not None:
            self._nextHandler.handleRequest(request)

    @abstractmethod
    def _handleRequestImpl(self, request):
        pass


class Person:
    def __init__(self, name):
        self._name = name
        self._leader = None

    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name

    def setLeader(self, leader):
        self._leader = leader

    def getLeader(self):
        return self._leader

    def sendRequest(self, request):
        print(
            f"{self._name} requests {request.getDayoff()} dayoff, reason={request.getReason()}")
        if self._leader is not None:
            self._leader.handleRequest(request)


class Supervisor(Responsible):
    def __init__(self, name, title):
        super().__init__(name, title)

    def _handleRequestImpl(self, request):
        if request.getDayoff() <= 2:
            print(
                f"{self.getTitle()}:{self.getName()} approves {request.getName()}'s dayoff")


class DepartmentManager(Responsible):
    def __init__(self, name, title):
        super().__init__(name, title)

    def _handleRequestImpl(self, request):
        if request.getDayoff() > 2 and request.getDayoff() <= 5:
            print(
                f"{self.getTitle()}:{self.getName()} approves {request.getName()}'s dayoff")


class CEO(Responsible):
    def __init__(self, name, title):
        super().__init__(name, title)

    def _handleRequestImpl(self, request):
        if request.getDayoff() <= 22:
            print(
                f"{self.getTitle()}:{self.getName()} approves {request.getName()}'s dayoff")


class Admin(Responsible):
    def __init__(self, name, title):
        super().__init__(name, title)

    def _handleRequestImpl(self, request):
        print(f"{self.getTitle()}:{self.getName()} Done")


if __name__ == "__main__":
    director = Supervisor("Eren", "Manager")
    departmentLeader = DepartmentManager("Eric", "DepLeader")
    ceo = CEO("Helen", "CEO")
    admin = Admin("Nina", "Admin")
    director.setNextHandler(departmentLeader)
    departmentLeader.setNextHandler(ceo)
    ceo.setNextHandler(admin)

    sunny = Person("Sunny")
    sunny.setLeader(director)
    sunny.sendRequest(Request(sunny.getName(), 1, "MDCC Meeting"))

    pony = Person("Pony")
    pony.setLeader(director)
    pony.sendRequest(Request(pony.getName(), 15, "Go abroad"))
