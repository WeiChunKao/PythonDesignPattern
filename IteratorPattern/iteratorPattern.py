class BaseIterator:
    def __init__(self, data):
        self._data = data
        self.toBegin()

    def toBegin(self):
        self._curIndex = -1

    def toEnd(self):
        self._curIndex = len(self._data)

    def next(self):
        if self._curIndex < len(self._data) - 1:
            self._curIndex += 1
            return True
        else:
            return False

    def previous(self):
        if self._curIndex > 0:
            self._curIndex -= 1
            return True
        else:
            return False

    def current(self):
        return self._data[self._curIndex] if self._curIndex < len(self._data) and self._curIndex >= 0 else None

if __name__ == "__main__":
    print("Forward")
    iterator = BaseIterator(range(0, 10))
    while(iterator.next()):
        customer = iterator.current()
        print(f"Customer:{customer}", end='\t')
    print()
    print("Backward")
    iterator.toEnd()
    while(iterator.previous()):
        customer = iterator.current()
        print(f"Customer:{customer}", end='\t')