# Python program showing
# abstract base class work
from abc import ABC, abstractmethod


class Polygon(ABC):

    @abstractmethod
    def noofsides(self):
        pass


class Triangle(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 3 sides")


class Pentagon(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 5 sides")


class Hexagon(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 6 sides")


class Quadrilateral(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 4 sides")


# Driver code
R = Triangle()
R.noofsides()

K = Quadrilateral()
K.noofsides()

R = Pentagon()
R.noofsides()

K = Hexagon()
K.noofsides()

# ------------------------------------------------------------------------------

# Python program showing
# implementation of abstract
# class through subclassing
import abc

class parent:       
    def geeks(self):
        pass

class child(parent):
    def geeks(self):
        print("child class")

# Driver code
print( issubclass(child, parent))
print( isinstance(child(), parent))


# ------------------------------------------------------------------------------------

# Python program showing
# abstract properties

import abc
from abc import ABC, abstractmethod


class parent(ABC):
    @abc.abstractproperty
    def geeks(self):
        return "parent class"


class child(parent):

    @property
    def geeks(self):
        return "child class"


try:
    r = parent()
    print(r.geeks)
except Exception as err:
    print(err)

r = child()
print(r.geeks)
