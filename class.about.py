'''
    (1) Whati is class???
    (2) Ordinary vs static properties...
    (3) Special methods 
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
