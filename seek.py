#with open('myfile.txt', 'r') as f:
    #print(type(f))
    
    #f.seek(10)
# move to the 10th byte in the file

# read the next 5 bytes
    #print(f.tell())
    #data = f.read(5)
    #print(data)

# seek is used to move to the required byte and read is used to read the file.
# tell is used to tell that how many bytes tk hum hain.


with open('myfile.txt', 'w') as f:
    f.write('Hello World! ')
    f.truncate(5)

with open('myfile.txt', 'r') as f:
    print(f.read())
    
# truncate is used to write upto required byte




