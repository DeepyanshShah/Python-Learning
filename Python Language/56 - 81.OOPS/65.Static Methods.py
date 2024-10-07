class Math:
    def __init__(self, num):
        self.num = num

    def addtonum(self, n):
        self.num = self.num +n

    @staticmethod 
    #creates a function which can be accessed without creating object
    # No need to pass self as arguement
    def add(a, b):
        return a + b
        
class avg():

# result = Math.add(1, 2)
# print(result) 
a = Math(5)
print(a.num)
a.addtonum(6)
print(a.num)
result = add(8)
print(result)

# --------------------------------------------------------------------------------------------------------------

# Python program to 
# demonstrate static methods 

class Person: 
	def __init__(self, name, age): 
		self.name = name 
		self.age = age 
		
	# a static method to check if a Person is adult or not. 
	@staticmethod
	def isAdult(age): 
		return age > 18
		
# Driver's code 
if __name__ == "__main__": 
	res = Person.isAdult(12) 
	print('Is person adult:', res) 
	
	res = Person.isAdult(22) 
	print('\nIs person adult:', res) 

