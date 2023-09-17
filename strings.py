# Strings
# strings are sequence of characters
# in python, strings are sequence of Unicode Characters

# create strings
c = 'hello'
print(c)

d = "helloo"
print(d)

e="It's raining outside"
print(e)

f= '''eref'''
print(f)
# multi line string

# we can create string like this too
c= str("hello")
print(c)

# Acessing Substrings from a string
# Concept of indexing
i = "fsdg"
print(i)

print(i[1])
print(i[3])

# Types of Indexing
# positive Indexing as like above
# Negative Indexing

print(i[-1])
print(i[-2])

# Slicing
tt = "Hello world"
print(tt)

# we use slicing by this
print(tt[0:5])

print(tt[2:])

print(tt[:4])

print(tt[:])

print(tt[2:6:2])

print(tt[0:8:3])

print(tt[0:6:-1])

print(tt[-5:-1:2])

print(tt[::-1])

print(tt[-1:-5:-1])

# Editing and Deleting Strings
e = "Hello"
print(e)
#e[0] ='x'
# Strings are a Immutable Data Type. Immutable means can not be changed
e = 'World'
print(e)
#c[5]= "s"
#print(c[5])

# Deletion
#del e
#print(e)

w = "hello"
print(w)
del w[0]
del c[:3:2]
# cHANGES IN STRINGS ARE NOT ALOUD






