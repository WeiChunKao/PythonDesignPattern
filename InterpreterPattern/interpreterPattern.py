from abc import ABCMeta, abstractmethod


class Expression(metaclass=ABCMeta):
    @abstractmethod
    def interpreter(self, var):
        pass


class VarExpression(Expression):
    def __init__(self, key):
        self._key = key

    def interpreter(self, var):
        return var.get(self._key)


class SymbolExpression(Expression):
    def __init__(self, left, right):
        self._left = left
        self._right = right


class AddExpression(SymbolExpression):
    def __init__(self, left, right):
        super().__init__(left, right)

    def interpreter(self, var):
        return self._left.interpreter(var) + self._right.interpreter(var)


class SubExpression(SymbolExpression):
    def __init__(self, left, right):
        super().__init__(left, right)

    def interpreter(self, var):
        return self._left.interpreter(var) - self._right.interpreter(var)


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class Calculator:
    def __init__(self, text):
        self._expression = self.parseText(text)

    def parseText(self, expText):
        stack = Stack()
        left = right = None
        idx = 0
        while idx < len(expText):
            if expText[idx] == '+':
                left = stack.pop()
                idx += 1
                right = VarExpression(expText[idx])
                stack.push(AddExpression(left, right))
            elif expText[idx] == '-':
                left = stack.pop()
                idx += 1
                right = VarExpression(expText[idx])
                stack.push(SubExpression(left, right))
            else:
                stack.push(VarExpression(expText[idx]))
            idx += 1
        return stack.pop()

    def run(self, var):
        return self._expression.interpreter(var)


def getMapValue(expStr):
    preIdx = 0
    expressionMap = {}
    newExp = []
    for i in range(0, len(expStr)):
        if expStr[i] == '+' or expStr[i] == '-':
            key = expStr[preIdx:i].strip()  # exclude space char
            newExp.append(key)
            newExp.append(expStr[i])
            var = input(f"Enter parameter: {key}'s value:").strip()
            expressionMap[key] = float(var)
            preIdx = i + 1
    key = expStr[preIdx: len(expStr)].strip()
    newExp.append(key)
    var = input(f"Enter parameter: {key}'s value:").strip() # exclude space char
    expressionMap[key] = float(var)
    return newExp, expressionMap

if __name__ == "__main__":
    newExp, expressionMap = getMapValue(input("Enter expression:"))
    calculator = Calculator(newExp)
    result = calculator.run(expressionMap)
    print(f"Result:{result}")