# Tuples
 
# Create

# it is empty tuple
T1=()

#Homogeneous tuple
T2 = (1,2,3,4,5)

#heterogeneous tuple

T3 = ("Hello",4,5.6)

# 2D Tuples

T4= (1,2,3,(5,6))

# There will be a problem with a single element tuple
T5 = (1)
print(type(T5))

T6 = ("Hello")
print(type(T6))

# We can use comma to declare single type tuple
T7 = ("Hello",)
print(type(T7))

# Type conversion

T8 = tuple("Hello")
print(T8)

T9 = tuple([1,2,3,4])
print(T9)

# Access 

print(T2[0])
print(T4[-1][0])

# Edit Tuple
# In list
L = [1,2,3,4,5]
L[0]=100
print(L)

# Now in Tuple
#print(T2[0]=100)

# We can not edit objects of tuple,tuples are immutable.
# We can not add new items into tuple

# Delete tuple

del T9
# We can not delete a part of tuple

print(T3+T4)

for i in T3:
    print(i)
    
print(4 in T3)

print(len(T3))
 # We can do max,min,sum,sorted
 # Tuples are read only data, but we can not write data
 
 





