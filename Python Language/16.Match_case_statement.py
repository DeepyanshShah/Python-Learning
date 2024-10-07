# Introduced from Python 3.10
# We don't have match case in python

day:str = str(input("Enter the day of week: "))
# day is the variable to match
match day:
    case "sunday":
        print("you have choosen sunday")

    case "monday":
        print("you have choosen monday")

    case "tuesday":
        print("you have choosen tuesday")

    case "wednesday":
        print("you have choosen wednesday")

    case "friday":
        print("you have choosen friday")

    case "saturday":
        print("you have choosen saturday")

    case _:
        print("you have been invalid!")   

# simple match case statement
def simpleMatch():
    num = int(input("Enter a number between 1 and 3: "))
    
    # match case
    match num:
        # pattern 1
        case 1:
            print("One")
        # pattern 2
        case 2:
            print("Two")
        # pattern 3
        case 3:
            print("Three")
        # default pattern
        case _:
            print("Number not between 1 and 3")

# python match case with OR operator
def operatorMatch():
    num = int(input("Enter a number between 1 and 6: "))
    
    # match case
    match num:
        # pattern 1
        case 1 | 2:
            print("One or Two")
        # pattern 2
        case 3 | 4:
            print("Three or Four")
        # pattern 3
        case 5 | 6:
            print("Five or Six")
        # default pattern
        case _:
            print("Number not between 1 and 6")
            
# python match case with if condition
def if_elseMatch():
    num = int(input("Enter a number: "))
    
    # match case
    match num:
        # pattern 1
        case num if num > 0:
            print("Positive")
        # pattern 2
        case num if num < 0:
            print("Negative")
        # default pattern
        case _:
            print("Zero")
            
# match case to check a character in a string
def stringMatch():
    myStr = "Hello World"
     
    # match case
    match (myStr[6]):
        case "w":
            print("Case 1 matches")
        case "W":
            print("Case 2 matches")
        case _:
            print("Character not in the string")
            
# python match case with list
def patternMatch(mystr):
    
    # match case
    match mystr:
        # pattern 1
        case ["a"]:
            print("a")
        # pattern 2
        case ["a", *b]:
            print(f"a and {b}")
        # pattern 3
        case [*a, "e"] | (*a, "e"):
            print(f"{a} and e")
        # default pattern
        case _:
            print("No data")
            
patternMatch([])
patternMatch(["a"])
patternMatch(["a", "b"])
patternMatch(["b", "c", "d", "e"])

# match case with python dictionaryu
def dictMatch(dictionary):
    # match case
    match dictionary:
        # pattern 1
        case {"name": n, "age": a}:
            print(f"Name:{n}, Age:{a}")
        # pattern 2
        case {"name": n, "salary": s}:
            print(f"Name:{n}, Salary:{s}")
        # default pattern
        case _ :
            print("Data does not exist")

dictMatch({"name": "Jay", "age": 24})
dictMatch({"name": "Ed", "salary": 25000})
dictMatch({"name": "Al", "age": 27})
dictMatch({})



     