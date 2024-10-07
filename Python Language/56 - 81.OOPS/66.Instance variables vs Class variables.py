class Employee:

    companyName = "Greek" #class variable

    noOfEmployee = 0
    def __init__(self, name):
        self.name = name
        self.raise_ammount = 0.02 #instance variable
        Employee.noOfEmployee += 1
    def showDetails(self):
        print(f"The name of the Employee is {self.name} and the raise amount in {self.noOfEmployee} sized {self.companyName} is {self.raise_amount}")

emp1 = Employee("Kratos")
emp1.raise_ammount = 0.3
emp1.companyName = "Greek Santa Monica studio"
Employee.showDetails(emp1)

emp2 = Employee("Ares")
Employee.showDetails(emp2)