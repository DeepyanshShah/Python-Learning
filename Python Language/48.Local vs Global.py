x = 4 # global variable
y = 10
print(x)


def hello():
    x = 5 # local variable
    # lets try to modify global variable x from this function hello()
    global y
    y = 7
    print(f"The local x is {x}")
    print("Hello")


print(f"The global x is {x}")

hello()
print(f"The global x is {x}")