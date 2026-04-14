print("======= Iterable Objects & RANGE =======")
# Iterable objects > list tuple range dict string map filter // takrorlanish hususiyatiga ega obyektlar

range_obj = range(3)  # [0,3]
print("range_obj:", range_obj)

text = "MIT"
for letter in text:
    print(f"the letter: {letter}")

for ele in range_obj:
    print(f"the element: {ele}")

print("======= DICTIONARY =======")
# DICTIONARY  is JSON object!!!
person = {
    "name": "Justin",
    "age": 25,
    "single": True
}
person_object = dict(name="Justin", age=25, single=True)
print(f"person: {person}")
print(f"person_object: {person_object}")

# method: get()
# name = person_obj["name"]
name = person_object.get("name")
hobby = person_object.get("hobby")
balance = person_object.get("balance", 0)
print(f"name: {name}, hobby: {hobby} and balance: {balance}")

del person_object["single"]
for key in person_object:
    print(f"the key: {key} => value: {person_object.get(key)}")
