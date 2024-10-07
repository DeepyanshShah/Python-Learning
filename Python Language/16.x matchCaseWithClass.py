# match case with python classes
# import dataclass module
from dataclasses import dataclass

#Class 1
@dataclass
class Person:
    name: str
    curse_tool: str
    gender: str

# class 2
@dataclass
class Sorcerer:
    name: str
    Grade: str
    speciality: str

def runMatch(instance):
    # match case
    match instance:
        # pattern 1
        case Sorcerer("Gojo Saturo", Grade="Special", speciality="Six Eyes"):
            print(f"Name: Gojo Saturo, Grade:Special, speciality:Six Eyes")
        # pattern 2
        case Sorcerer("Yuji Itadori", "C++"):
            print("Name:Yuji Itadori, Grade:C++")
        # pattern 3
        case Person("Nobara", curse_tool="Playfull cloud", gender="Male"):
            print("Name:Nobara")
        # pattern 4
        case Sorcerer(name, Grade, speciality):
            print(f"Name:{name}, Grade:{Grade}, speciality:{speciality}")
        # pattern 5
        case Person():
            print("He is just a person !")
        # default case
        case _:
            print("This person is nothing!")

Sorcerer1 = Sorcerer("Gojo Saturo", "Special", "Six Eyes")
Sorcerer2 = Sorcerer("Yuji Itadori", "Special", None)
Sorcerer3 = Sorcerer("Suguru Geto", "Special", "Curse Spirit Manipulation")
person1 = Person("Toji", "Playfull cloud", "Male")
runMatch(Sorcerer1)
runMatch(Sorcerer2)
runMatch(person1)
runMatch(Sorcerer3)
