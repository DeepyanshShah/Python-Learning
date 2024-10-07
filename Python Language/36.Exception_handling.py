# Basically we use exception handling to handle cases where we are bound to get errors or
# expecting code due to irregular input or edge case for a block 
# so that the programs doesn't hault at a spot and the whole program is executed along with the exception occured if any

a = input("Enter number: ")
print(f"Multiplication table of {a} is : ")

try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    print(e)

print("Some imp lines of code")            
print("End of program")

try:
    num = int(input("Enter an integer: "))
    a =[6,3]
    print(a[num])
except ValueError:
    print("Number entered is not a integer.")

except IndexError:
    print("Index Error")        