class Person:

    def __init__(self ,n, o):
        print("Hey i am from Person class")
        self.name = n
        self.occ = o
    
    def info(self):
        print(f"{self.name} is a {self.occ}")

a = Person("Thor", "Thunder-God")
b = Person("Odin", "Allfather")
a.info()
b.info()


# -----------------------------------------------------------------------------------------

class MyClass:
    def __init__(self, name=None):
        if name is None:
            print("Default constructor called")
        else:
            self.name = name
            print("Parameterized constructor called with name", self.name)
    
    def method(self):
        if hasattr(self, 'name'):
            print("Method called with name", self.name)
        else:
            print("Method called without a name")

# Create an object of the class using the default constructor
obj1 = MyClass()

# Call a method of the class
obj1.method()

# Create an object of the class using the parameterized constructor
obj2 = MyClass("John")

# Call a method of the class
obj2.method()


