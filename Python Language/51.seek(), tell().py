# seek()

with open('50.x_read()_readline().txt', 'r') as f:
    print(type(f))
    # Moves the pointer to the 10th byte in the file
    f.seek(10)

    # tell() : gives us the CURRENT position of the pointer
    print(f.tell())
    # Read the next 5 bytes
    data = f.read(5)
    print(data)

# truncate(n) : removes the character post n positions
with open('51.x_seek()_tell().txt', 'w') as f:
    f.write('Hello World!')
    f.truncate(3)
    