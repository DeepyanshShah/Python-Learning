# break :

for i in range(12):
    if (i == 10):
        break  # leaves the loop immediately when break is encountered
    print("5 X", i+1, "=", 5* (i+1))
    
print("Loop has been terminated")

# continue

for i in range(12):
    if (i == 10):
        print("Skip the iteration")
        continue  # Skips the current iteration and moves to next, loop is being continued if valid
    print("5 X", i, "=", 5* i)
    
#  Lets try to emulate do while loop in python

i = 0
while True:
    print(i)
    i += 1
    if (i % 100 == 0):
        break
