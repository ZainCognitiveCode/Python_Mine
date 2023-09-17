#def double(x):
  #  return x*2

double = lambda x: x*2
print(double(5))

avg = lambda x,y : (x+y) /3
print(avg(3,5))
cube = lambda x: x*x*x

# lambda ko phly variable mein store kia ur phir argument dia ur phir arhument ky sth value de jo deny the jaisy x*2 ur phr print krwa dia.
# hum kafi values bhi de skty han.

def appl(fx,value):
    return 6 + fx(value)
print(appl(cube, 2))


# Lambda Syntax(lambda arguments : expression)

