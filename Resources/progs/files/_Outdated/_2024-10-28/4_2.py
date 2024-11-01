class Animal:
    def __init__(self, name):
        self.name = name

    def is_alive(self):
        return True

class Mammal(Animal):
    def has_hair(self):
        return True

class Bird(Animal):
    def can_fly(self):
        return True

dog = Mammal('Dog')
eagle = Bird('Eagle')

print(f"{dog.name} is a mammal with hair: {dog.has_hair()}")
print(f"{eagle.name} is a bird that can fly: {eagle.can_fly()}")
