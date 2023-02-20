from modelClass import ObjectPool, PooledObject


class PowerBank:
    def __init__(self, serialNum, electricQuantity):
        self._serialNum = serialNum
        self._electricQuantity = electricQuantity
        self._user = ""

    def getSerialNumber(self):
        return self._serialNum

    def getElectricQuantity(self):
        return self._electricQuantity

    def setUser(self, user):
        self._user = user

    def getUser(self):
        return self._user

    def showInfo(self):
        print(
            f"Serial Number: {self._serialNum} Electricity:{self._electricQuantity} User: {self._user}")


class PowerBankPool(ObjectPool):
    _serialNum = 0

    @classmethod
    def getSerialNumber(cls):
        cls._serialNum += 1
        return cls._serialNum

    def createPooledObject(self):
        powerBank = PowerBank(PowerBankPool.getSerialNumber(), 100)
        return PooledObject(powerBank)


if __name__ == "__main__":
    powerBankPool = PowerBankPool()
    powerBank1 = powerBankPool.borrowObject()
    if powerBank1 is not None:
        powerBank1.setUser("Tony")
        powerBank1.showInfo()

    powerBank2 = powerBankPool.borrowObject()
    if powerBank2 is not None:
        powerBank2.setUser("Sam")
        powerBank2.showInfo()
    powerBankPool.returnObject(powerBank1)
    
    powerBank3 = powerBankPool.borrowObject()
    if powerBank3 is not None:
        powerBank3.setUser("John")
        powerBank3.showInfo()
    powerBankPool.returnObject(powerBank2)
    powerBankPool.returnObject(powerBank3)
    powerBankPool.clear()
