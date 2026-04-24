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
