from abc import ABCMeta, abstractmethod


class ReaderView(metaclass=ABCMeta):
    def __init__(self):
        self._curPageNum = 1

    def getPage(self, pageNum):
        self._curPageNum = pageNum
        return f"No. {pageNum} page"

    def prePage(self):
        content = self.getPage(self._curPageNum - 1)
        self._displayPage(content)

    def nextPage(self):
        content = self.getPage(self._curPageNum + 1)
        self._displayPage(content)

    @abstractmethod
    def _displayPage(self, content):
        pass


class SmoothView(ReaderView):
    def _displayPage(self, content):
        print(f"Left and Right smoothly:{content}")


class SimulationView(ReaderView):
    def _displayPage(self, content):
        print(f"Turn Page:{content}")


if __name__ == "__main__":
    smooth = SmoothView()
    smooth.nextPage()
    smooth.prePage()
    
    simulationView = SimulationView()
    simulationView.nextPage()
    simulationView.prePage()
