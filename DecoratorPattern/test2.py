class ClassDecorator:
    def __init__(self,func):
        self._numOfCall = 0
        self._func = func
    def __call__(self, *args, **kwargs):
        self._numOfCall += 1
        obj = self._func(*args, **kwargs)
        print(f"Number {self._numOfCall} instance, id={id(obj)}")
        return obj

@ClassDecorator
class MyClass:
    def __init__(self, name):
        self._name = name
    def getName(self):
        return self._name
if __name__ == "__main__":
    t = MyClass("Tony")
    w = MyClass("Wei")
    print(f"t's id={id(t)}")
    print(f"w's id={id(w)}")