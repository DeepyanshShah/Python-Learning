# NOTE: the best case to use lambda function is ad places where we need to pass function as an arguement to another.

# Writing a function 
# normal functions:

def double(x):
    return x*2
# OR
# Lambda functions(mini one-liner function):

double = lambda x: x*2
print(double(5))

cube = lambda x: x*x*x
print(cube(5))

avg = lambda x, y, z: (x+y+z) / 3
print(avg(5))

# Passing cube function as a paramter to appl function here:
def appl(fx, value):
    return 6 + fx(value)
print(appl(cube,6))
# or
print(appl(lambda x: x*x*x, 2))
