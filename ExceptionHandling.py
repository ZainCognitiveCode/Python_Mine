try:
  f = open('Filstext.txt')
#   var = bad_var
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print('Error!')
else:
    print(f.read())
    f.close()
finally: #it will run always
    print("Executing Finally...")

# hum apna bhi error handling raise kr skty han.

try:
    f = opne('corrutfile.txt')
    if f.name == 'corrutfile.txt':
     raise Exception