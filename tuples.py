''' Tuple
    (1) What is tuple: tuple vs list
    (2) Unpacking arguments
    (3) Zip
'''

print("===== What is tuple: tuple vs list ======")
# Java/PHP/Node JS array => Python list

# List => mutable (o'zgartirilishi mumkin) => [] => list()
numbs = [3, 5, 1, 2]
print("numbs:", numbs)
# car_dic = {"brand": "Ferrari", "year": 2026}

# Construction function => list()
letters = list("Hello World!!!")
print("letters:", letters)
# person_dic = dict(name="ALI", age=27)

fruits = ["apple", "banana", "cherry", "banana"]
print("Before fruits:", fruits)

fruits[2] = "orange"
print("After fruits:", fruits)

# Tuple => immutable (o'zgartirilishi mumkin emas) => () => tuple()

animals = ("cat", "dog", "fish", "lion")
print("animals:", animals)
# animals[0] = "tiger" => TypeError: 'tuple' object does not support item assignment
print(animals[0])
# animals[0] = "tiger"


tuple_obj = {"MIT", 100, True, None}
