# r for read, a for append and w for write

#f = open('myfile.txt', 'r')
#print(f)
#text = f.read()
#print(text)
#f.close()

#f = open('myfile.txt', 'a')
#f.write('Hello, world!')
#f.close()

with open('myfile.txt', 'a') as f:
  f.write("Hey I am inside")