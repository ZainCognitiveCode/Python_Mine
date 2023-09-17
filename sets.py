# Sets
# Rule 1: sets do not allow duplicates
# 2:+ Sets have no indexing
# 3: Sets do not allow mutable data types
#4: Set itself is a mutable data type

# Create 

S = {}
print(S)
print(type (S))
# Sets and dictionaries both use curly brackets
# We will create empty set by this method
S1 = set()
print(S1)
print(type(S1))

# Homogeneous sets

S2 = {1,2,3,4}
S3 = {"Hello",23,4.5}
print(S3)

# N+ow,see rule 1
S4 = {1,1,2,3,4,4}
print(S4)

# Now see rule 3
#S5 = {[1,2,3]."Hello"}
#print(S5)

# it gives error

S6 = {(1,2,3),"Hello"}
print(S6)
# Strings and tuples are immutable

# Sets have no indexing, so hello is printed first
# They follow hashing technique

# 2D,3D,4D sets are not possible
#S7 = {{1},{2}}
#print(S7)

# Access items
#print(S2[2])
#They do not suuport slicing,indexing

# Edit items
#They do not edit items too
#print(S2[2]=100)

print(id(S2))

l = list(S2)
print(l)
l[0]=100
print(l)

S2 = set(l)
print(S2)
print(id(l))

# We can not edit sets
# We can add items by add function
S2.add(6)
print(S2)

# Memory address also not get changes
print(id(S2))

# Delete,remove,del,pop

# del will delete the entire set
#del S2
#print(S2)

#we can not do slicing deletion
#del S2[0]
#print(S2)


S2.remove(100)
print(S2)

S2.pop()
print(S2)
# It has not deleted last item,but first item due to hashing


# Set Operations

a = {1,2,3,4,5}
b = {3,4,5,6,7}
#print(a+b)
# We can not concatinate in sets
# We can not multiply too

for i in a:
    print(i)
    
# Functions
print(len(S2))

# We can use min,max,sum and sorted function on it
sorted(a,reverse=True)
print(a)

S10 = {1,2,3,4,5}
S11 = {5,6,7,8,9}

print(S10.union(S11))

print(S10.intersection(S11))

print(S10.difference(S11))
print(S11.difference(S10))

print(S10.symmetric_difference(S11))

print(S10.isdisjoint(S11))
# As S10 and S11 have some common items

print(S10.issubset(S11))
# bECAUSE S10 is not a subset of S11

print(S10.issuperset(S11))
# it is not superset so thats why it is wrong











