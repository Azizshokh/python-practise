""" FUNCTION
(1) DEFINE vs CALL
(2) PARAMETERS vs ARGUMENTS
(3) KEYWORD & DEFAULT ARGUMENTS
(4) SCOPE
"""

print("======= DEFINE (parameters) vs CALL (arguments) =======")

# build-in function > print() input() type() int() str() bool() len() sum() max() min()
# Function definition - reusable block of code!!!
# Instead of block {} in JAVA, Python uses indentation!!!


# Define - parameters
def greet(a):
    print(f"How do you do, {a}?")


def greeting(b):
    print("greeting is executed")
    return f"Hi {b}!"


# Call - argument
result1 = greet("ALI")
print("the result1:", result1)

result2 = greeting("Justin")
print("the result2:", result2)


print("======= KEYWORD & DEFAULT ARGUMENTS =======")


# Define
def give_greet(name, age=22):  # default argument
    print("give_greet is executed")
    return f"Hi {name}, you are {age} years old!!!"


# Call
result3 = give_greet(name="ALi", age=27)  # keyword arguments
print("the result3:", result3)

result4 = give_greet("Jack")
print("the result4:", result4)
