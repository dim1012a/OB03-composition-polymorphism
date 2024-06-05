class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass
    def eat(self):
        print(f"{self.name} Жрет, не влезай!")

class Bird(Animal):
    def make_sound(self):
        print("Чирик, чирик!")

class Mammal(Animal):
     def make_sound(selfself):
        print("Я - млекопитающее, питаю молоком и издаю звуки!")

class Reptile(Animal):
    def make_sound(selfself):
        print("Добро пожаловать к нам, рептилоидам!")

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

class Zoo():
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Зверь {animal.name} в клетке!")

    def add_staff(self, new_staff):
        self.staff.append(new_staff)
        print(f"Сотрудник {new_staff} нанят в Зоо!")

class ZooKeeper():
    def feed_animal(self, animal):
        print(f"Сотрудник кормит {animal.name}!")

class Veterinarian():
    def heel_animal(self, animal):
        print(f"Сотрудник лечит {animal.name}!")


bird_01 = Bird("Кеша", "345")
mammal_01 = Mammal("Валентин", '14')
reptile_01 = Reptile("Геннадий", "126")

zoo = Zoo()
keeper = ZooKeeper()
veterinarian = Veterinarian()

zoo.add_animal(bird_01)
zoo.add_animal(mammal_01)
zoo.add_animal(reptile_01)

zoo.add_staff(keeper)
zoo.add_staff(veterinarian)

animal_sound(zoo.animals)

keeper.feed_animal(bird_01)
veterinarian.heel_animal(mammal_01)

