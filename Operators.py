# Operators are used to perform operations on variables and values.

# Arithmetic 
x = 5
y = 2
print(x+y)
print(x-y)
print(x*y)
print(x/y)
# modulus operator is %. The remainder after division is modulus
print(x%y)
# Power operator
print(x**y)
# Integer Division is used to show only true part, such as 2.5 will be shown as 2 only.
print(x//2)


# Comparison Operator
print(x>y)
print(x<y)
print(x >=y)
print(x<=y)
print(x==y)
#!= is used to show not equal to
print(x !=y)

#Logical Operators
x = True
y = False
# Or is used to add as you know 
print(x or y)

# AND is used to multiply
print(x and y)

# Not is used to negate
print(not x)


# Bitwise Operators
# They only work on binary values

x = 2
y = 3
print(x & y)
#  x as binary value and y too as binary value
# & it will use 'and' operator and it multiply values
# 010
# 110
# ---
# 010
# (2)

print(x|y)
# here | is used for 'OR' Operator and it add
# 010
# 110
# ---
# 110

print(x>>2)
print(x<<3)
print(~x)

# Assignment Operator
a = 3
print(a)
a +=3
# a = a+3
print(a)

a -=3
# a = a-3
a *=3
# a = a*3
a &=3
# a = a&3

# a++ and ++a do not work in python


# Identity Operator
a = 3
b = 3
print(a is b)
# It means a nad b are on same memory location
a = 'Hello'
b = 'Hello'
print(a is b)

a = [1,2,3]
b = [1,2,3]
print(a is b)
# IF two things have same value than it does not matter that they will be on same memory location.
a = "Hello-world"
b = "Hello-world"
print(a is b)

# Membership Operator
# it shows to check one thing in a statement
x = "Delhi"
print("D" in x)

x = [1,2,3]
print(5 in x)

y = [1,2,3]
print("4" not in y)






