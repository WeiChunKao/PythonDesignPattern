def singleTonDecorator(cls, *args, **kwargs):
    instance = {}

    def wrapperSingleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return wrapperSingleton

@singleTonDecorator
class Singleton1:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name


if __name__ == "__main__":
    t = Singleton1("Tony")
    k = Singleton1("kiven")
    print(t.getName(), k.getName())
    print(f"t'id={id(t)}, k's id={id(k)}")
    print(t == k)
