from abc import ABCMeta, abstractmethod


class Subject(metaclass=ABCMeta):
    def __init__(self, name):
        self._name = name

    def getName(self):
        return self._name

    @abstractmethod
    def request(self, content=""):
        pass


class RealSubject(Subject):
    def request(self, content=""):
        print("RealSubject todo something")


class ProxySubject(Subject):
    def __init__(self, name, subject):
        super().__init__(name)
        self._realSubject = subject

    def request(self, content=""):
        self.preRequest()
        if self._realSubject is not None:
            self._realSubject.request(content)
        self.afterRequest()

    def preRequest(self):
        print("preRequest")

    def afterRequest(self):
        print("afterRequest")
if __name__ == "__main__":
    realObj = RealSubject('RealSubject')
    proxyObj = ProxySubject('ProxySubject', realObj)
    proxyObj.request()