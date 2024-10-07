# Walrus operator :=
# Assigns values to variables as part of a larger expression
a = True
# print(a=False) Gives error because you can't assign a value to within an expression
print(a:=False)

# Example in While Loop
# while(n := len(numbers)) > 0:
#     print(numbers.pop())

# example:

# method 1: normal approach

foods = list()
while True:
    food = input("What food do you like?: ")
    if food == "quit":
        break
    foods.append(food)    

# method 2: walrus approach

foods = list()
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)    