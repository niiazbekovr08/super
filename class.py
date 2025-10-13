class Animal:
    def __init__(self, name, age, diet):
        self.name = name
        self.age = age
        self.diet = diet

    def make_sound(self):
        print(f"{self.name} издаёт звук.")

    def info(self):
        print(f"Имя: {self.name}, Возраст: {self.age}, Питание: {self.diet}")


class Mammal(Animal):
    def __init__(self, name, age, diet, has_fur):
        super().__init__(name, age, diet)
        self.has_fur = has_fur

    def feed_babies(self):
        print(f"{self.name} кормит детёнышей молоком.")


class Reptile(Animal):
    def __init__(self, name, age, diet, is_venomous):
        super().__init__(name, age, diet)
        self.is_venomous = is_venomous

    def lay_eggs(self):
        print(f"{self.name} откладывает яйца.")


animal = Animal("Неизвестное животное", 5, "всёядное")
print("=== Animal ===")
animal.info()
animal.make_sound()

print("\n=== Mammal ===")
lion = Mammal("Лев", 8, "плотоядное", has_fur=True)
lion.info()
lion.feed_babies()

print("\n=== Reptile ===")
snake = Reptile("Кобра", 4, "плотоядное", is_venomous=True)
snake.info()
snake.lay_eggs()
