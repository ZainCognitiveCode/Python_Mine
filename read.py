#f = open('myfile.txt', 'r')
#while True:
   #  line = f.readline()
  #   if not line:
   #     break
   #  print(line)
   
f = open('myfile.txt', 'w')
lines = ['lin 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close()

           