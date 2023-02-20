from abc import ABCMeta, abstractmethod


class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def algorithm(self):
        pass


class StrategyA(Strategy):
    def algorithm(self):
        print("StrategyA")


class StrategyB(Strategy):
    def algorithm(self):
        print("StrategyB")


class Context:
    def interface(self, strategy, *args, **kwargs):
        print("Before Back")
        strategy.algorithm()
        print("After Back")

if __name__ == "__main__":
    context = Context()
    context.interface(StrategyA())
    context.interface(StrategyB())