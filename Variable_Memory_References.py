# Python calls a as a name
a = 4
print(id(a))
print(hex(140723251504008))

# We call this by Object Reference

# Aliasing
a = 5;
b = a;
#Aliasing it is
print(id(a))
print(id(b))

del(a)
#print(a) We are deleting only reference,not the value
print(b)

#Suppose if a=4, b=a and than a=6 than b will show only 4

# Reference Counting

import sys

d = "Covid"
c = d
e= c
print(id(d))
print(id(c))
print(id(e))

# Now we have to check that how many variables are pointing at Covid

print(sys.getrefcount(d))
print(sys.getrefcount(d))

f = "Zdfd"
g = f
h = g
print(sys.getrefcount(f))

# I do not know why but it should be showing only 4, three by itself and fourth itself is pointing


# Garbage Collection

#When a memory varibale is deleted than its value remains in memory,we can not delete it,we only delete memory variable

# Garbage Collector is used to free up the memory








