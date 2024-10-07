print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\nData-Types\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
# type(variable or data) is a syntax which is used to print which type of data is it
integer = 5
string = "five"
point = 8.5
bool = True
com = 3 + 6j  # for complex we use j for iota
bin = 0b01011  # for writing in binary we use 0B before Binary number
hex = 0xF15A  # for writing in binary we use 0X before Hexadecimal number
oct = 0o73210  # for writing in binary we use 0O before Octadecimal number

print("\n", integer, " is a type of ", type(integer), "\n")

print(string, " is a type of ", type(string), "\n")

print(point, " is a type of ", type(point), "\n")

print(bool, " is a type of ", type(bool), "\n")  # boolean is a two option dataset which is only True and False

print(com, " is a type of ", type(com), "\n")

print(bin, " is a type of ", type(bin), "\n")

print(oct, " is a type of ", type(oct), "\n")

print(hex, " is a type of ", type(hex), "\n")
list_arr = ["tsk", "hmm", "asap"]  # this is a list, will be cover up later on
print(list_arr, " is a type of ", type(list_arr), "\n")

tuple = ("lol", "wud", "n8", 5)  # this is a tuple, will be cover up later on
print(tuple, " is a type of ", type(tuple), "\n")

dictionary = {"one": 1, 2: "two", "n8": "night"}  # this is a dictionary, will be cover up later on
print(dictionary, " is a type of ", type(dictionary), "\n")


def function():  # this is a function, will be cover up later on
    print("This is a function")


print("Below Function is Called...")
function()
print("above is a data type of ", type(function), "\n")

none = None
print(none, "is a type of", type(none), "\n")

# Comparing datatype for conditional statement

print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\nCOMPARISONS\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
# we use isinstance function for comparing data type
print(isinstance(dictionary, list))
print(isinstance(dictionary, dict))
print(isinstance("hello", str))
print(isinstance(5, int))
print(isinstance(5.5, float))