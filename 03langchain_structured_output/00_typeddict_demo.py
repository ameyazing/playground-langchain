from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

new_person: Person = {
    "name": "Ameya",
    "age": 42
}
print(new_person)
