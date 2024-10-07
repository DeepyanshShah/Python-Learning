marks = {12, 56, 32, 98, 12, 45, 1, 4}

# NOTE: updating index in variable index

# Without enumerate

index =0
for mark in marks:
    print(mark)
    if(index == 3):
        print("Gojo, awesome!")
    index += 1    

# With enumerate

for index, mark in enumerate(marks):
    print(mark)
    if(index == 3):
        print("Gojo, awesome!")  

# Lets say we want our index to start from 1 instead of 0

for index, mark in enumerate(marks, start=1):
    print(mark)
    if(index == 3):
        print("Gojo, awesome!")  