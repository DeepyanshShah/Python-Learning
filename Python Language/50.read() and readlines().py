# readline() 

f = open('50.x_read()_readline().txt', 'r')
i = 0

while True:
    i += 1
    line = f.readline()
    if not line:
        break
    m1 = line.split(",")[0]
    m2 = line.split(",")[1]
    m3 = line.split(",")[2]
    print(f"Marks of students {i} in Maths is: {m1}")
    print(f"Marks of students {i} in English is: {m2}")
    print(f"Marks of students {i} in Science is: {m3}")
    print(line)

# writeline()

f = open('50.x_read()_readline().txt', 'r')
lines = ['line 1\n', 'line 2\n','line 3\n',]
f.writelines(lines)
f.close()