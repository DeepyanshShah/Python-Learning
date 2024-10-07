class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"The employee is {self.name}")

class Dancer:
    def __init__(self, dance):
        self.dance = dance

    def show(self):
        print(f"The dance is {self.dance}")

class DancerEmpployee(Employee, Dancer):
    def __init__(self, dance, name):
        self.dance = dance
        self.name = name

o = DancerEmployee("Kathak", "jill")
print(o.name)
print(o.dance)
print(DancerEmpployee.mro())