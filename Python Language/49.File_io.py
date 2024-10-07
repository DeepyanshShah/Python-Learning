# READ A FILE

# Read file , if file doesn't exists it will return ERROR
# open('file_name', 'rt')  reads as text file
# open('file_name', 'rb')   reads as binary file
f = open('myfile.txt', 'r')
print(f)
text = f.read()
print(text)
f.close()


# WRITE A FILE

# Write file , if file doesn't exists it will CREATE this file
f = open('myfile.txt', 'w')
f.write('Hello, World!')
# NOTE: if we dont use f.close() the file wont save the stuff we want to write
f.close()
# ALTERNATE without closing thru f.close()
with open ('myfile.txt', 'a') as f:
    f.write("Hey i am inside with")

# APPEND A FILE

# Add the text
f = open('myfile.txt', 'a')
f.write('Hello, World!')

f.close()