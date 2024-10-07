class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id 

    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")

class Programmer(Employee):
    def showLanguage(self):
        print("The default language is Python")


e = Employee("Clark Kent", 100)
e.showDetails()

e1.Programmer("Alfred", 101)
e1.showDetails()
e1.showLanguage()
