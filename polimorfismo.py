class Animal:
    def __init__(self, name):
        self.name = name

    def falar(self):
        pass

class Gato(Animal):
    def falar(self):
        return 'Meow'

class Cachorro(Animal):
    def falar(self):
        return ' Woof! Woof!'

animais = [Gato('Missy'),
           Cachorro('Lassie'),
           Gato('Bichano')]

for animal in animais:
    print(animal.name + ':' + animal.falar())
