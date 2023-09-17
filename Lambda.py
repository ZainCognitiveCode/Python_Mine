# Lambda Functions: These are single line functions

# lambda input: expression

# where x= means we have stored the value in the variable and x**2 is an expression
x= lambda x: x**2
print(x(9))


a=lambda z,y: z+y
print(a(4,5))
print(type(a))

# Difference
# 1. lambda has no return value
# 2. Only one line
# 3. Not used for code reusability
# 4. No name

# Why use it?
# Along with higher order functions
# aisay functions jinko apna kaam krny ky liye input mein aik ur function chahiye
 
 
b = lambda x: x[0]=='a' 
print(b('apple'))
print(b('banana'))


c = lambda x:"Even" if x%2==0 else "Odd"
print(c(3))
print(c(4))







