from abc import ABCMeta, abstractmethod
import logging
import time
logging.basicConfig(level=logging.INFO)


class PooledObject:
    def __init__(self, obj):
        self._obj = obj
        self._busy = False

    def getObject(self):
        return self._obj

    def setObject(self, obj):
        self._obj = obj

    def isBusy(self):
        return self._busy

    def setBusy(self, busy):
        self._busy = busy


class ObjectPool(metaclass=ABCMeta):
    InitialNumOfObjects = 10
    MaxNumOfObjects = 50

    def __init__(self):
        self._pools = []
        for i in range(0, ObjectPool.InitialNumOfObjects):
            obj = self.createPooledObject()
            self._pools.append(obj)

    @abstractmethod
    def createPooledObject(self):
        pass

    def borrowObject(self):
        obj = self._findFreeObjects()
        if obj is not None:
            logging.info(
                f" {id(obj)} is borrowed. Time:{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))}")
            return obj
        if len(self._pools) < ObjectPool.MaxNumOfObjects:
            pooledObj = self.addObject()
            if pooledObj is not None:
                pooledObj.setBusy(True)
                logging.info(
                    f" {id(obj)} is borrowed. Time:{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))}")
                return pooledObj.getObject()
        return None

    def returnObject(self, obj):
        for pooledObj in self._pools:
            if pooledObj.getObject() == obj:
                pooledObj.setBusy(False)
                logging.info(
                    f" {id(obj)} is returned. Time:{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))}")
                break

    def addObject(self):
        obj = None
        if len(self._pools) < ObjectPool.MaxNumOfObjects:
            obj = self.createPooledObject()
            self._pools.append(obj)
            logging.info(
                f" {id(obj)} is added. Time:{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))}")
        return obj

    def clear(self):
        self._pools.clear()

    def _findFreeObjects(self):
        obj = None
        for pooledObj in self._pools:
            if not pooledObj.isBusy():
                obj = pooledObj.getObject()
                pooledObj.setBusy(True)
                break
        return obj
