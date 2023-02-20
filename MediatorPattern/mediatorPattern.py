from abc import ABCMeta, abstractmethod
from enum import Enum


class DeviceType(Enum):
    TypeSpeaker = 1
    TypeMicrophone = 2
    TypeCamera = 3


class DeviceItem:
    def __init__(self, id, name, type, isDefault=False):
        self._id = id
        self._name = name
        self._type = type
        self._isDefault = isDefault

    def __str__(self):
        return f"type={self._type} id={self._id} name={self._name} isDefault={self._isDefault}"

    def getId(self):
        return self._id

    def getName(self):
        return self._name

    def getType(self):
        return self._type

    def getIsDefault(self):
        return self._isDefault


class DeviceList:
    def __init__(self):
        self._devices = []

    def add(self, deviceItem):
        self._devices.append(deviceItem)

    def getCount(self):
        return len(self._devices)

    def getByIndex(self, index):
        if index < 0 or index >= self.getCount():
            return None
        return self._devices[index]

    def getById(self, id):
        for item in self._devices:
            if item.getId() == id:
                return item
        return None


class DeviceMgr(metaclass=ABCMeta):
    @abstractmethod
    def enumerate(self):
        pass

    @abstractmethod
    def active(self, deviceId):
        pass

    @abstractmethod
    def getCurrentDevice(self):
        pass


class SpeakerMgr(DeviceMgr):
    def __init__(self):
        self._currentDeviceId = None

    def enumerate(self):
        devices = DeviceList()
        devices.add(DeviceItem("123", "Realtek", DeviceType.TypeSpeaker))
        devices.add(DeviceItem("456", "NV Audio",
                    DeviceType.TypeSpeaker, True))
        return devices

    def active(self, deviceId):
        self._currentDeviceId = deviceId

    def getCurrentDevice(self):
        return self._currentDeviceId


class DeviceUtil:
    def __init__(self):
        self._mgrs = {}
        self._mgrs[DeviceType.TypeSpeaker] = SpeakerMgr()

    def _getDeviceMgrs(self, type):
        return self._mgrs[type]

    def getDeviceList(self, type):
        return self._getDeviceMgrs(type).enumerate()

    def active(self, type, deviceId):
        self._getDeviceMgrs(type).active(deviceId)

    def getCurDeviceId(self, type):
        return self._getDeviceMgrs(type).getCurrentDevice()


if __name__ == "__main__":
    deviceUtil = DeviceUtil()
    deviceList = deviceUtil.getDeviceList(DeviceType.TypeSpeaker)
    if deviceList.getCount() > 0:
        deviceUtil.active(DeviceType.TypeSpeaker,
                          deviceList.getByIndex(0).getId())
    for idx in range(0, deviceList.getCount()):
        device = deviceList.getByIndex(idx)
        print(device)
