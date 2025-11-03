from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass


class CreditCardPayment(Payment):
    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        print(f"Оплачено {amount:.2f} ₽ с карты ****{self.card_number[-4:]}")

    def refund(self, amount):
        print(f"Возврат {amount:.2f} ₽ на карту ****{self.card_number[-4:]}")


class CryptoPayment(Payment):
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address

    def pay(self, amount):
        print(f"Отправлено {amount:.6f} BTC с кошелька {self.wallet_address[:6]}...")

    def refund(self, amount):
        print(f"Возврат {amount:.6f} BTC на кошелёк {self.wallet_address[:6]}...")


if __name__ == "__main__":
    payments = [
        CreditCardPayment("1234 5678 9012 3456"),
        CryptoPayment("bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh"),
    ]

    for payment in payments:
        payment.pay(1000)
        payment.refund(500)


# 2)

        from abc import ABC, abstractmethod

class Course(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def get_materials(self):
        pass

    @abstractmethod
    def end(self):
        pass


class PythonCourse(Course):
    def start(self):
        print("Курс по Python запущен")

    def get_materials(self):
        print("Материалы: основы синтаксиса, функции, классы, модули")

    def end(self):
        print("Курс по Python завершён")


class MathCourse(Course):
    def start(self):
        print("Курс по математике начался")

    def get_materials(self):
        print("Материалы: алгебра, геометрия, тригонометрия")

    def end(self):
        print("Курс по математике завершён")


if __name__ == "__main__":
    courses = [PythonCourse(), MathCourse()]

    for course in courses:
        course.start()
        course.get_materials()
        course.end()
        print()


# 3)
from abc import ABC, abstractmethod

class Delivery(ABC):
    @abstractmethod
    def calculate_cost(self, distance):
        pass

    @abstractmethod
    def deliver(self):
        pass

class AirDelivery(Delivery):
    def __init__(self, rate_per_km=10):
        self.rate_per_km = rate_per_km

    def calculate_cost(self, distance):
        return distance * self.rate_per_km

    def deliver(self):
        return "Доставка по воздуху ✈️"

class GroundDelivery(Delivery):
    def __init__(self, rate_per_km=5):
        self.rate_per_km = rate_per_km

    def calculate_cost(self, distance):
        return distance * self.rate_per_km

    def deliver(self):
        return "Доставка по суше 🚚"

class SeaDelivery(Delivery):
    def __init__(self, rate_per_km=3):
        self.rate_per_km = rate_per_km

    def calculate_cost(self, distance):
        return distance * self.rate_per_km

    def deliver(self):
        return "Доставка по морю 🚢"

if __name__ == "__main__":
    deliveries = [AirDelivery(), GroundDelivery(), SeaDelivery()]
    distance = 1200
    for d in deliveries:
        print(d.deliver())
        print(f"Стоимость: {d.calculate_cost(distance)}")



# 4)

class BankAccount:
    def __init__(self, owner, balance=0, pin="0000"):
        self.__owner = owner
        self.__balance = balance
        self.__pin = pin

    def __check_pin(self, pin):
        return pin == self.__pin

    def deposit(self, amount, pin):
        if not self.__check_pin(pin):
            return "Неверный PIN"
        if amount <= 0:
            return "Сумма должна быть больше 0"
        self.__balance += amount
        return f"На счет внесено {amount}. Баланс: {self.__balance}"

    def withdraw(self, amount, pin):
        if not self.__check_pin(pin):
            return "Неверный PIN"
        if amount <= 0:
            return "Сумма должна быть больше 0"
        if amount > self.__balance:
            return "Недостаточно средств"
        self.__balance -= amount
        return f"Снято {amount}. Баланс: {self.__balance}"

    def change_pin(self, old_pin, new_pin):
        if not self.__check_pin(old_pin):
            return "Неверный текущий PIN"
        if len(new_pin) != 4 or not new_pin.isdigit():
            return "PIN должен состоять из 4 цифр"
        self.__pin = new_pin
        return "PIN изменен"

    def get_balance(self, pin):
        if not self.__check_pin(pin):
            return "Неверный PIN"
        return self.__balance


if __name__ == "__main__":
    acc = BankAccount("Иван", 1000, "1234")
    print(acc.deposit(500, "1234"))
    print(acc.withdraw(200, "1234"))
    print(acc.change_pin("1234", "5678"))
    print(acc.get_balance("5678"))



# 5)

class UserProfile:
    def __init__(self, email, password):
        self.__email = email
        self.__password = password
        self._status = "free"
        self.__logged_in = False

    def login(self, email, password):
        if email == self.__email and password == self.__password:
            self.__logged_in = True
            return "Вход успешен"
        return "Неверный email или пароль"

    def upgrade_to_premium(self):
        if not self.__logged_in:
            return "Доступ запрещён"
        self._status = "premium"
        return "Статус обновлён до premium"

    def get_info(self):
        if not self.__logged_in:
            return "Доступ запрещён"
        return {"email": self.__email, "status": self._status}


if __name__ == "__main__":
    user = UserProfile("user@example.com", "1234")
    print(user.get_info())
    print(user.login("user@example.com", "wrong"))
    print(user.login("user@example.com", "1234"))
    print(user.get_info())
    print(user.upgrade_to_premium())
    print(user.get_info())



# 6)    

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.__discount = 0

    def get_price(self):
        return self.price * (1 - self.__discount / 100)

    def set_discount(self, discount, is_admin=False):
        if not is_admin:
            return "Доступ запрещён"
        if not (0 <= discount <= 100):
            return "Скидка должна быть от 0 до 100"
        self.__discount = discount
        return f"Скидка установлена: {self.__discount}%"


if __name__ == "__main__":
    p = Product("Ноутбук", 1000)
    print(p.get_price())
    print(p.set_discount(10))
    print(p.set_discount(10, is_admin=True))
    print(p.get_price())



# 7)    

class TextFile:
    def __init__(self, name):
        self.name = name

    def open(self):
        return f"Открыт текстовый файл: {self.name}"


class ImageFile:
    def __init__(self, name):
        self.name = name

    def open(self):
        return f"Открыт изображение файл: {self.name}"


class AudioFile:
    def __init__(self, name):
        self.name = name

    def open(self):
        return f"Открыт аудио файл: {self.name}"


def open_all(files):
    for f in files:
        print(f.open())


if __name__ == "__main__":
    files = [TextFile("doc.txt"), ImageFile("photo.png"), AudioFile("song.mp3")]
    open_all(files)



# 8)    

class Car:
    def __init__(self, fuel_consumption=8, speed=100):
        self.fuel_consumption = fuel_consumption
        self.speed = speed

    def move(self, distance):
        time = distance / self.speed
        fuel = distance * self.fuel_consumption / 100
        return f"Car: время {time:.2f} ч, расход топлива {fuel:.2f} л"


class Truck:
    def __init__(self, fuel_consumption=20, speed=80):
        self.fuel_consumption = fuel_consumption
        self.speed = speed

    def move(self, distance):
        time = distance / self.speed
        fuel = distance * self.fuel_consumption / 100
        return f"Truck: время {time:.2f} ч, расход топлива {fuel:.2f} л"


class Bicycle:
    def __init__(self, speed=20):
        self.speed = speed

    def move(self, distance):
        time = distance / self.speed
        return f"Bicycle: время {time:.2f} ч, расход топлива 0 л"


def simulate_transport(transport_list, distance):
    for t in transport_list:
        print(t.move(distance))


if __name__ == "__main__":
    transport = [Car(), Truck(), Bicycle()]
    simulate_transport(transport, 200)
    