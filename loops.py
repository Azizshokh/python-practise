'''OPERATORS and CONDITIONS
(1) for
(2) break/else
(3) while
'''

print("===== for operator ======")
# Iterable objects > list tuple range dict string map filter // takrorlanish hususiyatiga ega obyektlar
text = "MIT"
numbs = [10, 7, 3, 4]
car_obj = dict(brand="Ferrari", year=2025)
range_obj = range(5)

for letter in text:
    print(f"The letter: {letter}")

print("=====")

for number in numbs:
    print(f"The number: {number}")
for x in range_obj:
    print(f"The element: {x}")
for key in car_obj:
    # key orqali qiymatni olish
    print(f"The key: {key} => value: {car_obj.get(key)}")

print("==========")
for x in range(1, 20, 5):
    print(f"The element: {x}")

print("===== break/else ======")
# break => loopni to'xtatish
for x in range(1, 20, 5):
    print(f"The x: {x}")
    if x > 10:
        print("Reached break")
        break
else:
    print("Executed successfully")

print("+++++++++++")

print("===== while operator ======")
# while => shart bajarilguncha takrorlanadi
numb = 40
while numb > 0:
    numb -= 10
    print(f"The numb equals: {numb}")

print("=========")
count = 0
while True:
    count += 1
    x = int(input("Find a number: "))

    if x == 41:
        print(f"You found the number in {count} steps")
        break
    else:
        print("Wrong, please find again!!!")
