class Animal():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        return ''

class Bird(Animal):
    def __init__(self, name, age, fly):
        super().__init__(name, age)
        self.fly = fly

    def make_sound(self):
        return 'чик-чирик'

class Mammal(Animal):
    def __init__(self, name, age, leg):
        super().__init__(name, age)
        self.leg = leg

    def make_sound(self):
        return 'мяу и гав'

class Reptile(Animal):
    def __init__(self, name, age, tail):
        super().__init__(name, age)
        self.tail = tail

    def make_sound(self):
        return 'шшш...'

def animal_sound(animals):
    for animal in animals:
        print(f'Животное {animal.name} возраста {animal.age} издает звук {animal.make_sound()}')

animals = [Bird('Воробей', 3, 'может летать'),
           Mammal('Горилла', 10, 'может ходить'),
           Reptile('Ящерица', 5, 'есть хвост')]

animal_sound(animals)
