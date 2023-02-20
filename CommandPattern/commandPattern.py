from abc import ABCMeta, abstractmethod


class Chef():
    def steamFood(self, originalMaterial):
        msg = f"Steaming {originalMaterial}"
        print(msg)
        return msg

    def stirFriedFood(self, originalMaterial):
        msg = f"Stir Fry {originalMaterial}"
        print(msg)
        return msg


class Order(metaclass=ABCMeta):
    def __init__(self, name, originalMaterial):
        self._chef = Chef()
        self._name = name
        self._originalMaterial = originalMaterial

    def getDisplayName(self):
        return f"{self._name} {self._originalMaterial}"

    @abstractmethod
    def processingOrder(self):
        pass


class SteamedOrder(Order):
    def __init__(self, originalMaterial):
        super().__init__("Steaming", originalMaterial)

    def processingOrder(self):
        if self._chef is not None:
            return self._chef.steamFood(self._originalMaterial)
        return ""


class SpicyOrder(Order):
    def __init__(self, originalMaterial):
        super().__init__("Spicy", originalMaterial)

    def processingOrder(self):
        if self._chef is not None:
            return self._chef.stirFriedFood(self._originalMaterial)
        return ""


class Waiter:
    def __init__(self, name):
        self._name = name
        self._order = None

    def receiveOrder(self, Order):
        self._order = Order
        print(f"Waiter:{self._name} receives {self._order.getDisplayName()}")

    def placeOrder(self):
        food = self._order.processingOrder()
        print(f"Waiter:{self._name} ready {food} ")
if __name__ == "__main__":
    waiter = Waiter("Awei")
    steamedOrder = SteamedOrder("Shrimp")
    print(f"Client:David order {steamedOrder.getDisplayName()}")
    waiter.receiveOrder(steamedOrder)
    waiter.placeOrder()