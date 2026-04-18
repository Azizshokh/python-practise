'''
    (1) Whati is class???
    (2) Ordinary vs static properties...
    (3) Special/magic methods 
'''
print("=================")

# class is a blueprint for creating objects
# structure of a class > state constructor method


class Person():
    # state
    message = "static state property"

    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method
    def introduce(self):
        print(f"The {self.name} says: How do you do???")

    def say_age(self):
        print(f"{self.name} says: I am  {self.age} years old!!!")

    @classmethod
    def explain(cls):
        print("Static method property executed!!!")


person1 = Person("Justin", 25)
person2 = Person("Sarah", 24)
person3 = Person("Michael", 30)

# ordinary state
name = person1.name
print("person1.name:", person1.name)

# ordinary method
person1.introduce()
person2.say_age()

print("==== ordinary vs static properties ====")
# static state
new_message = Person.message
print("new_message:", new_message)

# static method
Person.explain()

print("==== special/magic methods ====")
# Python's most common special methods are below:
# __init__ __new__ __str__ __call__ __getitem__ __eq__ __len__ ...


class Car():
    # state
    description = "This class makes cars!!!"

    # constructor
    def __new__(cls, *args):
        print("* __new__ *")
        return super().__new__(cls)

    def __init__(self, name, year):
        self.name = name
        self.year = year

    # method
    def start_engine(self):
        print(f"The {self.name} started engine!!!")

    def stop_engine(self):
        print(f"The {self.name} stopped engine!!!")

    def __str__(self):
        return f"{self.name} was produced in {self.year} year!!!"

    def __call__(self):
        print("Object called as a function!!!")
        return True


my_car = Car("Ferrari", 2025)
my_car.start_engine()
my_car.stop_engine()

print("=============")
your_car = Car("Tayoto", 2026)
print(your_car)
response = your_car()  # function look like function
print("Response:", response)
