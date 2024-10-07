class Employee:
    company = "Apple"
    
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")

    @classmethod()
    def changeCompany(cls, newCompany):
            cls.company = newCompany

e1 = Employee()
e1.name = "Tim Cook"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(e1.instanceof)

# ---------------------------------------------------------------------------------------------------

class Geeks:
    course = 'DSA'
    list_of_instances = []

    def __init__(self, name):
        self.name = name
        Geeks.list_of_instances.append(self)

    @classmethod
    def get_course(cls):
        return f"Course: {cls.course}"

    @classmethod
    def get_instance_count(cls):
        return f"Number of instances: {len(cls.list_of_instances)}"

    @staticmethod
    def welcome_message():
        return "Welcome to Geeks for Geeks!"

# Creating instances
g1 = Geeks('Alice')
g2 = Geeks('Bob')

# Calling class methods
print(Geeks.get_course())  
print(Geeks.get_instance_count())  

# Calling static method
print(Geeks.welcome_message())  

# ---------------------------------------------------------------------------------------------------------------

# USING classmethod()

class Student:

    # create a variable
    name = "Geeksforgeeks"

    # create a function
    def print_name(obj):
        print("The name is : ", obj.name)


# create print_name classmethod
# before creating this line print_name()
# It can be called only with object not with class
Student.print_name = classmethod(Student.print_name)

# now this method can be called as classmethod
# print_name() method is called a class method
Student.print_name()

# ---------------------------------------------------------------------------------------------------------------------------

# Factory method using a Class Method

# A common use case for class methods is defining factory methods. Factory methods are methods that return an instance of the class, often using different input parameters.

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_string):
        year, month, day = map(int, date_string.split('-'))
        return cls(year, month, day)
