def isEventNumber(number):
    return number % 2 == 0


def isGreaterThanTen(number):
    return number > 10


def getResultNumber(fun, number):
    newList = []
    for item in number:
        if fun(item):
            newList.append(item)
    return newList

if __name__ == '__main__':
    number = [2,3,6,9,12,15,18]
    list1 = getResultNumber(isEventNumber, number)
    list2 = getResultNumber(isGreaterThanTen, number)
    print(f"Even Number:{list1}")
    print(f"Greater Than Ten:{list2}")