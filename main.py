class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass
    def eat(selfself):
        print("Жрем, не влезай!")

class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def make_sound(selfself):
        print("Чирик, чирик!")

class Mammal(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def make_sound(selfself):
        print("Я - млекопитающее, питаю молоком и издаю звуки!")

class Reptile(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def make_sound(selfself):
        print("Добро пожаловать к нам, рептилоидам!")

animals = [Bird("Кеша", "345"), Mammal("Валентин", '14'), Reptile("Геннадий", "126")]
for animal in animals:
    animal.make_sound()