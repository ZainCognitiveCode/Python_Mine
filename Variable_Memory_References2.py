# Weird Stuff

#WB 1
import sys
a = 2
b = a
c = b

print(sys.getrefcount(a))
# It is showing weird stuff because other variables are already created
d = 61
c = d
f = c
print(sys.getrefcount(d))

e = 4
g = 4
# The above is not aliasing
print(id(e))
print(id(g))

#The above ids are same

h = 257
i = 257
print(id(h))
print(id(i))

h = 258
i = 258
print(id(h))
print(id(i))

# -5 to 256 have same id



# 3RD Weird
l = "Haldi"
m = "Haldi"
print(id(l))
print(id(m))

n = "Haldia inst tech"
o = "Haldia inst tech"
print(id(n))
print(id(o))

# My addresses are coming same, hahahahahah
# Valid identifiers are those which have underscore in them

