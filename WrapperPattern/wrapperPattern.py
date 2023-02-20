from abc import ABCMeta, abstractmethod
import os


class Page:
    def __init__(self, pageNum):
        self._pageNum = pageNum

    def getContent(self):
        return f"Content in page {self._pageNum}"


class Catalogue:
    def __init__(self, title):
        self._title = title
        self._chapter = []

    def addChapter(self, title):
        self._chapter.append(title)

    def showInfo(self):
        print(f"Book:{self._title}")
        print("Catalog:")
        for chapter in self._chapter:
            print(f"   {chapter}")


class IBook(metaclass=ABCMeta):
    @abstractmethod
    def parseFile(self, filepath):
        pass

    @abstractmethod
    def getCatalogue(self):
        pass

    @abstractmethod
    def getPageCount(self):
        pass

    @abstractmethod
    def getPageCount(self):
        pass

    @abstractmethod
    def getPage(self):
        pass


class TxtBook(IBook):
    def parseFile(self, filepath):
        print(f"File: {filepath}")
        self._title = os.path.splitext(filepath)[0]
        self._pageCount = 500
        return True

    def getCatalogue(self):
        catalogue = Catalogue(self._title)
        catalogue.addChapter("First Chapter")
        catalogue.addChapter("Second Chapter")
        return catalogue

    def getPageCount(self):
        return self._pageCount

    def getPage(self, pageNum):
        return Page(pageNum)


class EpuBook(IBook):
    def parseFile(self, filepath):
        print(f"File: {filepath}")
        self._title = os.path.splitext(filepath)[0]
        self._pageCount = 800
        return True

    def getCatalogue(self):
        catalogue = Catalogue(self._title)
        catalogue.addChapter("First Chapter")
        catalogue.addChapter("Second Chapter")
        return catalogue

    def getPageCount(self):
        return self._pageCount

    def getPage(self, pageNum):
        return Page(pageNum)


class Outline:
    def __init__(self):
        self._outlines = []

    def addOutline(self, title):
        self._outlines.append(title)

    def getOutlines(self):
        return self._outlines


class PdfPage:
    def __init__(self, pageNum):
        self._pageNum = pageNum

    def getPageNum(self):
        return self._pageNum


class ThirdPdf:
    def __init__(self):
        self._pageSize = 0
        self._title = ""

    def open(self, filePath):
        print("Vendor's PDF")
        self._title = os.path.splitext(filePath)[0]
        self._pageSize = 1000
        return True

    def getTitle(self):
        return self._title

    def getOutline(self):
        outline = Outline()
        outline.addOutline("Fist Chapter PDF title")
        outline.addOutline("Second Chapter PDF title")
        return outline

    def pageSize(self):
        return self._pageSize

    def page(self, index):
        return PdfPage(index)


class PdfAdapterBook(ThirdPdf, IBook):
    def __init__(self, thirdPdf):
        self._thirdPdf = thirdPdf

    def parseFile(self, filePath):
        rtn = self._thirdPdf.open(filePath)
        if rtn:
            print(f"Parse {filePath} success")
        return rtn

    def getCatalogue(self):
        outline = self.getOutline()
        print(f"Transfer Outline to Catalogue")
        catalogue = Catalogue(self._thirdPdf.getTitle())
        for title in outline.getOutlines():
            catalogue.addChapter(title)
        return catalogue

    def getPageCount(self):
        return self._thirdPdf.pageSize()

    def getPage(self, pageNum):
        page = self.page(pageNum)
        print(f"Transfer Pdfpage to Page")
        return Page(page.getPageNum())


class Reader:
    def __init__(self, name):
        self._name = name
        self._filePath = ""
        self._curBook = None
        self._curPageNum = -1

    def _initBook(self, filePath):
        self._filePath = filePath
        extName = os.path.splitext(filePath)[1]
        name = extName.lower()
        if name == ".epub":
            self._curBook = EpuBook()
        elif name == ".txt":
            self._curBook = TxtBook()
        elif name == ".pdf":
            self._curBook = PdfAdapterBook()
        else:
            self._curBook = None

    def openFile(self, filePath):
        self._initBook(filePath)
        if self._curBook is not None:
            rtn = self._curBook.parseFile(filePath)
            if rtn:
                self._curPageNum = 1
            return rtn
        return False

    def closeFile(self):
        return True

    def showCatalogue(self):
        catalogue = self._curBook.getCatalogue()
        catalogue.showInfo()

    def prePage(self):
        print("Previous", end='')
        return self.gotoPage(self._curPageNum - 1)

    def nextPage(self):
        print("Next", end='')
        return self.gotoPage(self._curPageNum + 1)

    def gotoPage(self, pageNum):
        if pageNum > 1 and pageNum <= self._curBook.getPageCount() - 1:
            self._curPageNum = pageNum
            print(f"Show {self._curPageNum} page")
            page = self._curBook.getPage(self._curPageNum)
            page.getContent()
            return page


if __name__ == '__main__':
    reader = Reader("Reader")
    if reader.openFile("text.txt"):
        reader.showCatalogue()
        reader.prePage()
        reader.nextPage()
        reader.nextPage()
        reader.closeFile()
        print()