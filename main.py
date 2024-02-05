# from dataclasses import dataclass, field


# def get_default_age(gender: str) -> int:
#     return 0 if gender == "male" else 1


# @dataclass
# class Person:
#     name: str
#     age: int = field(default_factory=lambda title: get_default_age(title))
#     gender: str = "male"


# p1 = Person(name="John", title="male")
# print(p1)  # Person(name='John', age=18, gender='male')


# from dataclasses import dataclass


# @dataclass(frozen=True)
# class Person:
#     name: str
#     age: int


# person = Person(name="Jonas", age=17)
# person.name = "Gedas"
# print(person.name)

from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int


@dataclass
class Employee(Person):
    id: str
    department: str


employee = Employee(name="Jonas", age=25, id=1616516, department="IT")

print(employee)
