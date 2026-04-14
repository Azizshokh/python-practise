""" OBJECTS
    (1) What is an object???
    (2) Iterable objects & RANGE
    (3) DICTIONARY
    (4) Error handling system
"""
import array  # package/module
import math  # package
from math import ceil
print("======= What is an object??? =======")
# An Object has state and method properties
# Everything is an object in Python!!!

print(type("Hello World!!!"))
print(type(100))
print(type(True))
print(type(array))
print(type(math))

# Paradigm > Functional Programming & OOP
# OOP 4 Concepts > Abstraction | Encapsulation | Inheritance | Polymorphism
result1 = math.ceil(97.7)  # Call
print("the result1:", result1)

result2 = ceil(98.7)
print("the result2:", result2)
