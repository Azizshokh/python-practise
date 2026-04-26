''' OPERATORS & CONDITION
(1) Operators
(2) Condition
(3) Logical Operators
'''

print("===========")
# + - > >= < <= == is * /   // % += **

a = 19
b = 5

print("a > b", a > b)
print(" a * b", a * b)
print(" a / b", a / b)

print(a / b)  # 3.8
result = a // b
left = a % b

# a = a + 100
a += 100
print("a:", a)
print("b*b:", b**2)
print("b*b*b:", b**3)

print("="*5)

c = dict(name="ALI", age=27)
d = dict(name="ALI", age=27)
e = c

print("c == d:", c == d)  # only value is checked
print(id(c), id(d), id(e))

data = c is d
print("c is d:", data)
print("c is e:", c is e)

print("===== CONDITION =====")

# x = 5
x = 15

if x > 50:
    print("Case A")
elif x > 10:
    print("Case B")
else:
    print("Case C")

print("===== TERNARY OPERATOR =====")

age = 20
# age = 18
# person = None

# if age > 16:
#     person = "Adult"
# else:
#     person = "Child"

# print("Person:", person)

# Ternary Operator
person = "Adult" if age > 18 else "Minor"
print("Person:", person)

is_student = True
is_admin = False
is_guest = True
is_parent = False

# if is_student:
#     print("Executed")

if not is_student:
    print("Welcome here, do you want to be a student???")
elif is_admin:
    print("Please, go to this office!!!")
# elif is_guest or is_parent:
#     print("Waiting room is over there!!!")
    # elif is_parent or is_guest:
elif is_guest and is_parent:
    print("Waiting room is over there!!!")
else:
    print("Other cases!!!")
