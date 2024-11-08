# 1 Нұсқа Бегимов Инкапсуляция
class Pet:
    def _init_(self, name, age):
        self._name = name
        self._age = age

    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        self._age = age

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def make_sound(self):
        pass

# Наследование
class Dog(Pet):
    def bark(self):
        return "Woof!"

    def make_sound(self):
        return self.bark()

class Cat(Pet):
    def meow(self):
        return "Meow!"

    def make_sound(self):
        return self.meow()

class Bird(Pet):
    def chirp(self):
        return "Chirp!"

    def make_sound(self):
        return self.chirp()

# Демонстрация полиморфизма
def demo_polymorphism(pet):
    print(f"{pet.get_name()} ({pet.get_age()} лет): {pet.make_sound()}")

# Создание объектов и вызов методов
dog = Dog("Buddy", 3)
cat = Cat("Whiskers", 2)
bird = Bird("Tweety", 1)

demo_polymorphism(dog)
demo_polymorphism(cat)
demo_polymorphism(bird)
