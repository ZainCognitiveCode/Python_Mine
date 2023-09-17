# Lists
# List is a datatype where we can store data
# Array is homogeneous while list can be hetrogeneous
# arrays are faster because items are placed side by side,while in array items are scattered
# Lists are more programmer friendly

# Create a list
L =[]
print(L)
# Homogeneous List
L2 = [1,2,3,4,5]
print(L2)
# hetrogeneous list
L3 = ["hello",2,3,4,True,5+6j]
print(L3)

# Multi-dimensional lists
#2d List
l4 = [1,2,3,[4,5]]
print(l4)

#3D
l5 = [[[1,2],[3,4]],[[5,6],[7,8]]]
print(l5)

l6 = list("Hadia")
print(l6)

# How to access items from a list
print(l6[0])
print(l6[-1])
print(l6[::-1])
# It works in a way just like string
l7 = [1,2,3,[4,5]]
print(l7)
print(l7[3])
print(l7[-1])
x=(l7[-1])
print(x)
print(x[0])
print(x[1])

l8= [[[1,2],[3,4]],[[5,6],[7,8]]]
print(l8[1][1][0])
# 1 shows first part of brackets
# Now do one for yourself
print(l8[0][0][1])
# List in python are mutable
# How to edit lits
l9= [1,2,3,4,5,6,7,8,9]
l9[0]=11
l9[-1]=33
print(l9)
l9[1:2]=[200,300,400,600]
print(l9)

# How to add items
#ADD,APPEND,EXTEND,INSERT
L10 = [2,4,6,7,8]
L10.append(100)
print(L10)
# Append will add one item while extend will add multiple items
L10.extend([500,600,700])
print(L10)
L10.append([5,4])
print(L10)
L10.extend("go")
print(L10)

# insert is used to add on required postion. We have to first tell the index position and the item to add
L10.insert(1,"world")
print(L10)
    # How to delete in a list
#Del,remove,pop,clear
list = [1,2,34,4,5,6,8,9,0]
del list[0]
print(list)
del list[-4]
print(list)

del list[-3:]
print(list)

list.remove(34)
print(list)

list.pop()
print(list)

# pop will delete the last item

list.clear()
print(list)

# Operations

lst =[1,2,3,4,5,6]
lst2 =[7,8,9,10]

print(lst+lst2)

print(lst*3)

for i in lst:
    print(i)
    
lst3=[1,2,3,4,5,6,[7,8]]

for i in lst3:
    print(i)
    
# if we say that 7 in lst3 than it will be false

# Functions
print(len(lst3))

#we can also use min and max in it

print(sorted(lst))
print(min(lst))
print(sorted(lst,reverse=True))


# sorted is temporary and sort is permanent function
# we can also use index

"Hello how are you".title()













