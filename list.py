''' List
    (1) Working with lists
    (2) List  methods
    (3) Lambda function
    (4) enumerate, map and filter
'''

print("===== Working with lists ======")
# Java/PHP/Node JS array => Python list

# Literal
person = {"name": "ALI", "age": 27}  # dictionary
person = ("John", "Mikel", "Sara")  # tuple
group = ["MIT", "FLEXY", "DEVEX", "MG"]  # list
for team in group:
    print(f"The team: {team}")

# constructor
result = list("Hello World!!!")
print(f"The letters: {result} and size: {len(result)}")

print("===============")
fruits = ["apple", "orange", "lemon", "kiwi"]

a = fruits[0]
b = fruits[0:2]  # [0, 2) 2 is not included
c = fruits[::3]  # 3- qadam, 3- qiymatni olish
d = fruits[::-1]  # teskari tartibda olish


print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)

print("====== List  methods ======")
# methods => append(), insert(), remove(), clear(), sort(): => mutable ; index(), sorted(): => immutable

letters = ["a", "b", "c"]

letters.append("d")  # listning oxiriga element qo'shish
print(f"The append result: {letters}")

letters.insert(0, "z")  # index 0 ga "z" ni qo'shish oldidan
print(f"The insert result: {letters}")

size = len(letters) - 1
# listning oxiridan elementni o'chirish va o'chirilgan elementni qaytarish
result1 = letters.pop(size)
print(f"The pop result1: {result1} and letters: {letters}")

result2 = letters.pop(0)  # index 0 ni o'chirish
print(f"The pop result2: {result2} and letters: {letters}")

print("============")
animals = ["cat", "dog", "capybara", "fish", "lion"]
print("animals:", animals)

animals.remove("lion")  # elementni o'chirish
print("Animals after remove:", animals)

del animals[2:4]  # index bo'yicha elementni o'chirish
print("Animals after del:", animals)

exist = animals.index("cat")  # mavjud elementning indexini qaytarish
print("Index of 'cat':", exist)

animals.clear()  # listni tozalash
print("Animals after clear:", animals)

# mavjud bo'lmagan elementning indexini qaytarish => ValueError: 'cat' is not in list
# exist2 = animals.index("cat")
# print("Index of 'cat':", exist2)

if "cat" in animals:
    print("The index of CAT :", animals.index("cat"))
else:
    print("'CAT' does not exist in the list...")

print("===============")

numbers = [2, 20, 12, 8, 57]
numbers.sort()  # listni o'sish tartibida sortlash
print("Numbers sorted:", numbers)
numbers.sort(reverse=True)  # listni kamayish tartibida sortlash
print("Numbers sorted in reverse:", numbers)

# immutable sorted() => yangi list qaytaradi
numbs = [2, 20, 12, 100]
new_numbs = sorted(numbs)  # o'sish tartibida sortlash
print(f"The sorted numbers: {numbs} and new_numbers: {new_numbs}")
