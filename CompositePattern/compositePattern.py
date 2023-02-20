import os
from abc import ABCMeta, abstractmethod


class Component(metaclass=ABCMeta):
    def __init__(self, name):
        self._name = name

    def getName(self):
        return self._name

    def isComposite(self):
        return False

    @abstractmethod
    def features(self, indent):
        pass


class Composite(Component):
    def __init__(self, name):
        super().__init__(name)
        self._component = []

    def addComponent(self, component):
        self._component.append(component)

    def removeComponent(self, component):
        self._component.remove(component)

    def isComposite(self):
        return True

    def features(self, indent):
        indent += '\t'
        for component in self._component:
            print(indent, end="")
            component.features(indent)


class FileDetail(Component):
    def __init__(self, name):
        super().__init__(name)
        self._size = 0

    def setSize(self, size):
        self._size = size

    def getFileSize(self):
        return self._size

    def features(self, indent):
        fileSize = round(self._size / float(1024), 2)
        print(f"File Name:{self._name}, Size:{fileSize}")


class FolderDetail(Composite):
    def __init__(self, name):
        super().__init__(name)
        self._count = 0

    def setCount(self, count):
        self._count = count

    def getCount(self):
        return self._count

    def features(self, indent):
        print(f"Folder Name:{self._name}, File Numbers{self._count}")
        super().features(indent)


def scanDir(rootPath, folderDetail):
    if not os.path.isdir(rootPath):
        raise ValueError(f"RootPath={rootPath} is not a directory")
    if folderDetail is None:
        raise ValueError(f"FolderDetail={folderDetail} is empty")
    fileNames = os.listdir(rootPath)
    for fileName in fileNames:
        filePath = os.path.join(rootPath, fileName)
        if os.path.isdir(filePath):
            folder = FolderDetail(filePath)
            scanDir(filePath, folder)
            folderDetail.addComponent(folder)
        else:
            fileDetail = FileDetail(filePath)
            fileDetail.setSize(os.path.getsize(filePath))
            folderDetail.addComponent(fileDetail)
            folderDetail.setCount(folderDetail.getCount() + 1)


if __name__ == '__main__':
    folder = FolderDetail("Pattern")
    scanDir("CompositePattern", folder)
    folder.features("")
