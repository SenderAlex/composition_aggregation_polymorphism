class Zoo:
    def __init__(self):
        self.stuff_name = []
        self.animal = []
        self.feeding_animal = []
        self.healing_animal = []

    def add_stuff_name(self, stuff_name):
        self.stuff_name.append(stuff_name)
        return stuff_name

    def add_animal(self, animal):
        self.animal.append(animal)
        return animal

    def show_stuff_name(self):
        for stuff_name in self.stuff_name:
            if isinstance(stuff_name, Zookeeper):
                print(f'Сотрудник {stuff_name.zookeeper_name}')
            elif isinstance(stuff_name, Veterinarian):
                print(f'Ветеринар {stuff_name.veterinarian_name}')

    def show_animal(self):
        print(f'В зоопарке есть животные:')
        for animal in self.animal:
            print(animal)

    def save_to_file(self, file_name='information.txt'):
        with open(file_name, "w", encoding="utf-8") as file:
            file.write('Animals:\n')
            for animal in self.animal:
                file.write(f'{animal}\n')

            file.write('\nZookeeper:\n')
            for stuff_name in self.stuff_name:
                if isinstance(stuff_name, Zookeeper):
                    file.write(f'{stuff_name.zookeeper_name}\n')

            file.write('\nVeterinarian:\n')
            for stuff_name in self.stuff_name:
                if isinstance(stuff_name, Veterinarian):
                    file.write(f'{stuff_name.veterinarian_name}\n')

            file.write(('\nZookeepers feed animals:\n'))
            for feeding_animal in self.feeding_animal:
                file.write(f'{feeding_animal}\n')

            file.write(('\nVeterinarian heal animals:\n'))
            for healing_animal in self.healing_animal:
                file.write(f'{healing_animal}\n')

    def load_from_file(self, file_name='information.txt'):
        try:
            self.animal.clear()
            self.stuff_name.clear()
            with open(file_name, "r", encoding="utf-8") as file:
                lines = file.readlines()
                section = None
                for line in lines:
                    line = line.strip()
                    if line == 'Animals:':
                        section = 'animals'
                    elif line == 'Zookeeper:':
                        section = 'zookeeper'
                    elif line == 'Veterinarian:':
                        section = 'veterinarian'
                    elif line:
                        if section == 'animals':
                            self.add_animal(line)
                        elif section == 'zookeepers':
                            self.add_stuff_name(Zookeeper(line, self))
                        elif section == 'veterinarian':
                            self.add_stuff_name(Veterinarian(line, self))
        except FileNotFoundError:
            print(f'Файл {file_name} не найден.')


class Zookeeper:
    def __init__(self, zookeeper_name, zoo):
        self.zookeeper_name = zookeeper_name
        self.zoo = zoo

    def feed_animal(self, animal_name):
        action = f'Сотрудник {self.zookeeper_name} должен покормить {animal_name}'
        self.zoo.feeding_animal.append(action)
        return action



class Veterinarian:
    def __init__(self, veterinarian_name, zoo):
        self.veterinarian_name = veterinarian_name
        self.zoo = zoo

    def heal_animal(self, animal_name):
        action = f'Ветеринар {self.veterinarian_name} должен вылечить {animal_name}'
        self.zoo.healing_animal.append(action)
        return action


zoo = Zoo()
zoo.load_from_file(file_name='information.txt')

tiger = zoo.add_animal('Тигр')
lion = zoo.add_animal('Лев')
elephant = zoo.add_animal('Слон')

zookeeper1 = Zookeeper('Людмила', zoo)
zookeeper2 = Zookeeper('Екатерина', zoo)
zookeeper3 = Zookeeper('Ирина', zoo)
zoo.add_stuff_name(zookeeper1)
zoo.add_stuff_name(zookeeper2)
zoo.add_stuff_name(zookeeper3)


veterinarian1 = Veterinarian('Александр', zoo)
veterinarian2 = Veterinarian('Максим', zoo)
veterinarian3 = Veterinarian('Миша', zoo)
veterinarian4 = Veterinarian('Сергей', zoo)
zoo.add_stuff_name(veterinarian1)
zoo.add_stuff_name(veterinarian2)
zoo.add_stuff_name(veterinarian3)
zoo.add_stuff_name(veterinarian4)

zoo.show_stuff_name()
zoo.show_animal()

print(zookeeper1.feed_animal(tiger))
print(zookeeper2.feed_animal(lion))
print(zookeeper3.feed_animal(elephant))

print(veterinarian1.heal_animal(tiger))
print(veterinarian2.heal_animal(elephant))
print(veterinarian3.heal_animal(lion))
zoo.save_to_file(file_name='information.txt')