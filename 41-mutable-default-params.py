# Mutable default parameters (and why they're a bad idea)

from typing import List, Optional


class Student:
    # def __init__(self, name: str, grades: List[int] = []):  # this is bad, never assign default value to mutable param
    #     self.name = name
    #     self.grades = grades

    def __init__(self, name: str, grades: Optional[List[int]] = None):  # this is good
        self.name = name
        self.grades = grades or []

    def take_exam(self, result: int):
        self.grades.append(result)


bob = Student("Bob")
bob.take_exam(90)
rolf = Student("Rolf")
print(bob.grades)
print(rolf.grades)
