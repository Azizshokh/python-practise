''' OBJECTS
    (1) ENCAPSULATION
    (2) INHERITANCE
    (3) POLYMORPHISM   
'''
print("==== INHERITANCE ====")

# PARENT CLASS > CHILD CLASS
# PARENT only provides public & protected properties(state + methods) are inherited to CHILD


class Animal:  # Parent class
    # State
    description = "This class is parent for animals!!!"

    # Constructor
    def __init__(self, voice):
        self._status = "Animal is alive!!!"
        self.voice = voice

    # Method
    def make_voice(self):
        print(f"The animal can make voice: {self.voice}!!!")


class Dog(Animal):  # Child class
    # State

    # Constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # Method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}!!!")

    def protect(self):
        print("Yes, I can protect you!!!")


class Cat(Animal):  # Child class
    # State

    # Constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # Method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}!!!")

    def play(self):
        pass


class Fish(Animal):  # Child class
    # State

    # Constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # Method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}!!!")

    def swim(self):
        print("Yes, I can swim!!!")


dog = Dog("Rex", "woow", True)
cat = Cat("Tom", "myeow", True)
fish = Fish("Nemo", "ZzZ", False)

dog.introduce()
cat.introduce()
fish.introduce()

print("======================")
dog.make_voice()
fish.make_voice()

print("======================")
print(Animal.description)
print(Dog.description)

print(dog.voice, fish.voice)
print("Dog status:", dog._status)
print("Cat status:", cat._status)
