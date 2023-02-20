from copy import deepcopy
import logging


class Memento:
    def setAttributes(self, dict):
        self.__dict__ = deepcopy(dict)

    def getAttributes(self):
        return self.__dict__


class Caretaker:
    def __init__(self):
        self._mementos = {}

    def addMemento(self, name, memento):
        self._mementos[name] = memento

    def getMemento(self, name):
        return self._mementos[name]


class Originator:
    def createMemento(self):
        memento = Memento()
        memento.setAttributes(self.__dict__)
        return memento

    def restoreFromMemento(self, memento):
        self.__dict__.update(memento.getAttributes())


class TerminalCmd (Originator):
    def __init__(self, text):
        self._cmdName = ""
        self._cmdArgs = []
        self.parseCmd(text)

    def parseCmd(self, text):
        subStrs = self.getArgumentsFromString(text, " ")
        if len(subStrs) > 0:
            self._cmdName = subStrs[0]
        if len(subStrs) > 1:
            self._cmdArgs = subStrs[1:]

    def getArgumentsFromString(self, str, splitFlag):
        if splitFlag == "":
            logging.warning("SplitFlag is empty")
            raise ValueError("SplitFlag is empty")
        data = str.split(splitFlag)
        result = []
        for item in data:
            item.strip()
            if item != "":
                result.append(item)
        return result

    def showCmd(self):
        print(f"{self._cmdName} {self._cmdArgs}")


class TerminalCaretaker(Caretaker):
    def showHistoryCmds(self):
        for k, v in self._mementos.items():
            name = ""
            value = []
            if v._TerminalCmd_cmdName:
                name = v._TerminalCmd_cmdName
            if v._TerminalCmd_cmdArgs:
                value = v._TerminalCmd_cmdArgs
            print(f"No. {k} Name:{name} Cmd:{value}")
if __name__ == "__main__":
    cmdIdx = 0
    caretaker = TerminalCaretaker()
    curCmd = TerminalCmd("")
    while(True):
        strCmd = input("Enter Command:",)
        strCmd = strCmd.lower()
        
        if strCmd.startswith("q"):
            exit(0)
        elif strCmd.startswith("h"):
            caretaker.showHistoryCmds()
        elif strCmd.startswith("!"):
            idx = int(strCmd[1:])
            curCmd.restoreFromMemento(caretaker.getMemento(idx))
            curCmd.showCmd()
        else:
            curCmd = TerminalCmd(strCmd)
            curCmd.showCmd()
            caretaker.addMemento(cmdIdx, curCmd.createMemento())
            cmdIdx += 1