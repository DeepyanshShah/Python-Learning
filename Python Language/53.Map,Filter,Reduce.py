# MAP
def cube(x):
    return x*x*x

print(cube(2))

l = [1, 2, 4, 6, 7, 9]
# newl = []
# for items in l:
#     newl.append(cube(items))

# Instead we can use map function
newl = list(map(lambda x: x*x*x, l))
print(newl)

# Filter
def filter_function(a):
    return a > 4

newnewl = list(filter(filter_function, l))
print(newnewl)

# Reduce
from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Calculated the sum of the numbers using the reduce function

def mysum(x, y):
    return x + y 

sum = reduce(mysum, numbers)

print(sum)