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

fruits = ["apple", "banana", "cherry",]
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

# try avoid these
people = "ALI", "John"
aniimas = "elephant",

print("===== Unpacking arguments ======")

groups = ["MIT", "FLEXY", "DEVEX", "MG"]
# (a, b, c, d) = groups
(a, b, *z) = groups
# print(f"a: {a}, b: {b}, c: {c}, d: {d}")
print(f"a: {a}, b: {b}, z: {z}")  # list

# *args => tuple


def calculate(*args):
    print("*args >", args)
    total = 1
    for x in args:
        total *= x
    print(f"The type of args: {type(args)}")
    print(f"The total: {total}")
    return total


# CALL
calculate(1, 7, 2, 3)
calculate(0, 2, 300)
calculate(5, 7)


# **kwargs => dictionary
def introduce(**kwargs):
    print(f"The type(**kwargs): {type(kwargs)}")
    print(
        f"Hi, I am {kwargs['name']}, I am {kwargs['age']} years old!!!")
    pass


# CALL
introduce(name="ALI", age=27)
introduce(name="John", age=30, single=True)
print("============")


def greeting(*args, **kwargs):
    print("*args:", args)
    print("**kwargs:", kwargs)


# CALL
greeting("Hi", True, 10, name="ALI", age=27)


print("===== Zip ======")
# zip => bir nechta iterable obyektlarni birlashtirish
tuple1 = (1, 2, 3, 4)
tuple2 = ("a", "b", "c")

zipped = zip(tuple1, tuple2)
print("Zipped object:", zipped)
result = list(zipped)
# Tarkibini ko'rish uchun list() ga o'tkazamiz
print(f"Zipped result: {result}")
