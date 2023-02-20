class Register:
    def register(self, name):
        print(f"Activity Center: {name} student registers success")


class Payment:
    def pay(self, name, money):
        print(f"Payment Center: {name} student pays {money} success")


class DormitoryManagementCenter:
    def provideLivingGoods(self, name):
        print(f"Life Center: {name} student gets daily necessities")


class Dormitory:
    def meetRoommate(self, name):
        print(f"Dormitory: Welcome {name} student")


class Volunteer:
    def __init__(self, name):
        self._name = name
        self._register = Register()
        self._payment = Payment()
        self._lifeCenter = DormitoryManagementCenter()
        self._dormitory = Dormitory()

    def welcome(self, name):
        print(f"Hello {name} student! I'm {self._name} volunteer")
        self._register.register(name)
        self._payment.pay(name, 1000)
        self._lifeCenter.provideLivingGoods(name)
        self._dormitory.meetRoommate(name)

if __name__ == "__main__":
    volunteer = Volunteer("Frank")
    volunteer.welcome("Tony")