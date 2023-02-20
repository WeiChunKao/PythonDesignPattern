from observer import Observer, Observalbe

class WaterHeater(Observalbe):
    def __init__(self):
        super().__init__()
        self._temperature = 25
    def getTemperature(self):
        return self._temperature
    def setTemperature(self, temperature):
        self._temperature = temperature
        print(f"Current Temperature is {temperature}")
        self.notifyObserver()

class WashingMode(Observer):
    def update(self, observalbe, object):
        if isinstance(observalbe, WaterHeater) and observalbe.getTemperature()>= 50 and observalbe.getTemperature() < 70:
            print(f"Water is heat already!! Take shower")

class DrinkingMode(Observer):
    def update(self, observalbe, object):
        if isinstance(observalbe, WaterHeater) and observalbe.getTemperature()>= 100:
            print(f"Water is heat already!! Drink ")


if __name__ == '__main__':
    heater  = WaterHeater()
    washingObser = WashingMode()
    drinkingObser = DrinkingMode()
    heater.addObserver(drinkingObser)
    heater.addObserver(washingObser)
    heater.setTemperature(40)
    heater.setTemperature(60)
    heater.setTemperature(100)