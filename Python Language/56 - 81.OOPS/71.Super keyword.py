class ParentClass:
    def parent_method(self):
        print("This is the parent method")
        
class ChildClass(ParentClass):
    def child_method(self):
        print("This is the child method")
        super().parent_method() # calling parents method

child_object = ChildClass()
child_object.child_method()

# ---------------------------------------------------------------

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id) # calling parents constructor
        self.lang = lang

steve = Employee("Steve", "100")
tim = Employee("tim", "999","Swift")
print(tim.name)
print(tim.id)
print(tim.lang)