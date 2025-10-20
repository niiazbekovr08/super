# 1. Account
class Account:
    def __init__(self, number, balance, pin):
        self.__number = number
        self.__balance = balance
        self.__pin = pin

    def deposit(self, amount, pin):
        if pin == self.__pin:
            self.__balance += amount
            return f"Пополнено на {amount}"
        return "Неверный PIN"

    def withdraw(self, amount, pin):
        if pin == self.__pin:
            if amount <= self.__balance:
                self.__balance -= amount
                return f"Снято {amount}"
            return "Недостаточно средств"
        return "Неверный PIN"

    def get_balance(self, pin):
        if pin == self.__pin:
            return f"Баланс: {self.__balance}"
        return "Неверный PIN"

acc = Account("12345", 1000, 1111)
print(acc.deposit(500, 1111))
print(acc.withdraw(200, 1111))
print(acc.get_balance(1111))


# 2. Product
class Product:
    def __init__(self, price):
        self.__price = price

    def set_discount(self, percent):
        discount = self.__price * (percent / 100)
        new_price = self.__price - discount
        if new_price < 0:
            self.__price = 0
        else:
            self.__price = new_price

    def final_price(self):
        return self.__price

p = Product(100)
p.set_discount(30)
print(p.final_price())


# 3. Course
class Course:
    def __init__(self, name, max_students):
        self.__name = name
        self.__students = []
        self.__max_students = max_students

    def add_student(self, name):
        if len(self.__students) < self.__max_students:
            self.__students.append(name)
            return f"{name} добавлен"
        return "Мест нет"

    def remove_student(self, name):
        if name in self.__students:
            self.__students.remove(name)
            return f"{name} удалён"
        return "Не найден"

    def get_students(self):
        return self.__students.copy()

c = Course("Python", 2)
print(c.add_student("Иван"))
print(c.add_student("Мария"))
print(c.add_student("Павел"))
print(c.get_students())
print(c.remove_student("Иван"))
print(c.get_students())


# 4. SmartWatch
class SmartWatch:
    def __init__(self):
        self.__battery = 100

    def use(self, minutes):
        self.__battery -= (minutes // 10)
        if self.__battery < 0:
            self.__battery = 0

    def charge(self, percent):
        self.__battery += percent
        if self.__battery > 100:
            self.__battery = 100

    def get_battery(self):
        return self.__battery

w = SmartWatch()
w.use(50)
print(w.get_battery())
w.charge(30)
print(w.get_battery())


# 5. Transport
class Transport:
    def __init__(self, speed, capacity):
        self.speed = speed
        self.capacity = capacity

    def travel_time(self, distance):
        return distance / self.speed

class Bus(Transport):
    pass

class Train(Transport):
    pass

class Airplane(Transport):
    def travel_time(self, distance):
        return (distance / self.speed) * 0.8

b = Bus(60, 50)
t = Train(120, 200)
a = Airplane(800, 150)
print(b.travel_time(120))
print(t.travel_time(120))
print(a.travel_time(800))


# 6. Order
class Order:
    def __init__(self, amount):
        self.amount = amount

class DineInOrder(Order):
    def calculate_total(self):
        return self.amount * 1.05

class TakeAwayOrder(Order):
    def calculate_total(self):
        return self.amount

class DeliveryOrder(Order):
    def calculate_total(self):
        return self.amount * 1.10

o1 = DineInOrder(100)
o2 = TakeAwayOrder(100)
o3 = DeliveryOrder(100)
print(o1.calculate_total())
print(o2.calculate_total())
print(o3.calculate_total())


# 7. Character
class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

class Warrior(Character):
    def attack(self):
        return f"{self.name} атакует мечом!"

class Mage(Character):
    def attack(self):
        return f"{self.name} использует магию!"

class Archer(Character):
    def attack(self):
        return f"{self.name} стреляет из лука!"

chars = [Warrior("Боец", 100, 20), Mage("Маг", 80, 30), Archer("Лучник", 90, 25)]
for ccc in chars:
    print(ccc.attack())


# 8. MediaFile
class MediaFile:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

class AudioFile(MediaFile):
    def play(self):
        return f"Воспроизводится аудио: {self.name}"

class VideoFile(MediaFile):
    def play(self):
        return f"Воспроизводится видео с изображением: {self.name}"

class Podcast(MediaFile):
    def play(self):
        return f"Воспроизводится эпизод подкаста: {self.name}"

media = [AudioFile("Песня", 3), VideoFile("Фильм", 120), Podcast("Подкаст", 45)]
for m in media:
    print(m.play())


# 9. PaymentSystem
from abc import ABC, abstractmethod

class PaymentSystem(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(PaymentSystem):
    def process_payment(self, amount):
        return f"Оплата картой {amount}"

class CryptoPayment(PaymentSystem):
    def process_payment(self, amount):
        return f"Оплата криптой {amount}"

class BankTransfer(PaymentSystem):
    def process_payment(self, amount):
        return f"Банковский перевод {amount}"

payments = [CreditCardPayment(), CryptoPayment(), BankTransfer()]
for ppp in payments:
    print(ppp.process_payment(500))


# 10. Animal
class Animal(ABC):
    @abstractmethod
    def eat(self): pass
    @abstractmethod
    def sleep(self): pass

class Lion(Animal):
    def eat(self): return "Лев ест мясо"
    def sleep(self): return "Лев спит в саванне"

class Elephant(Animal):
    def eat(self): return "Слон ест траву"
    def sleep(self): return "Слон спит стоя"

class Snake(Animal):
    def eat(self): return "Змея ест мышей"
    def sleep(self): return "Змея спит свернувшись"

animals = [Lion(), Elephant(), Snake()]
for a in animals:
    print(a.eat(), "|", a.sleep())


# 11. Document
class Document(ABC):
    @abstractmethod
    def open(self): pass
    @abstractmethod
    def edit(self): pass
    @abstractmethod
    def save(self): pass

class WordDocument(Document):
    def open(self): return "Word открыт"
    def edit(self): return "Редактирование Word"
    def save(self): return "Word сохранён"

class PdfDocument(Document):
    def open(self): return "PDF открыт"
    def edit(self): return "Редактирование PDF"
    def save(self): return "PDF сохранён"

class SpreadsheetDocument(Document):
    def open(self): return "Таблица открыта"
    def edit(self): return "Редактирование таблицы"
    def save(self): return "Таблица сохранена"

docs = [WordDocument(), PdfDocument(), SpreadsheetDocument()]
for d in docs:
    print(d.open(), d.edit(), d.save())


# 12. Lesson
class Lesson(ABC):
    @abstractmethod
    def start(self): pass

class VideoLesson(Lesson):
    def start(self): return "Начинается видеоурок"

class QuizLesson(Lesson):
    def start(self): return "Начинается тест"

class TextLesson(Lesson):
    def start(self): return "Начинается текстовый урок"

lessons = [VideoLesson(), QuizLesson(), TextLesson()]
for l in lessons:
    print(l.start())


# 13. Notification
class EmailNotification:
    def send(self, message):
        return f"Отправлено по email: {message}"

class SMSNotification:
    def send(self, message):
        return f"Отправлено по SMS: {message}"

class PushNotification:
    def send(self, message):
        return f"Push уведомление: {message}"

notifs = [EmailNotification(), SMSNotification(), PushNotification()]
for n in notifs:
    print(n.send("Привет!"))


# 14. Shapes
class Square:
    def __init__(self, a): self.a = a
    def perimeter(self): return self.a * 4

class Circle:
    def __init__(self, r): self.r = r
    def perimeter(self): return 2 * 3.14 * self.r

class Triangle:
    def __init__(self, a, b, c): self.a, self.b, self.c = a, b, c
    def perimeter(self): return self.a + self.b + self.c

shapes = [Square(4), Circle(5), Triangle(3,4,5)]
for s in shapes:
    print(s.perimeter())


# 15. Employees
class Manager:
    def work(self): return "Управляет проектами"

class Developer:
    def work(self): return "Пишет код"

class Designer:
    def work(self): return "Делает дизайн"

emps = [Manager(), Developer(), Designer()]
for e in emps:
    print(e.work())


# 16. Spells
class FireSpell:
    def cast(self, target): return f"{target} получает урон огнём"

class IceSpell:
    def cast(self, target): return f"{target} заморожен"

class HealingSpell:
    def cast(self, target): return f"{target} восстановил здоровье"

spells = [FireSpell(), IceSpell(), HealingSpell()]
for s in spells:
    print(s.cast("Враг"))
