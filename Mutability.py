# Mutability refers to the ability to change or edit data in its memory location
# Mutability depends on the data type

a= "Hello"
print(id(a))
a = a+"world"
print(a)
print(id(a))

# Addresses are changes

T = (1,2,3)
print(id(T))
T = T+(5,6)
print(T)
print(id(T))

L = [1,2,3]
print(L)
print(id(L))

L.append(4)
print(L)
print(id(L))

# Side effects of Mutation

l = [1,2,3,4,5]
L1= l
print(l)
print(L1)
print(id(l))
print(id(L1))

L1.append(6)
print(L1)
print(id(L1))


# Cloning
# We will not do like this l=L1
# But we will do it

L1=l[:]
print(id(l))
print(id(L1))
# Now,addresses have changed
L1.append(7)
print(L1)
print(l)

# Last Example

c = (1,2,3,[4,5])
print(c)
c[-1][-1]=500
print(c)
# At the end,it matters in which thing you are making changes


#d = [1,2,3(4,5)]
#d[-1][-1]=600
#print(d)
# It will not work because Tuples are immutable,while list is mutable

e = [1,2]
f = [3,4]
g =(e,f)
print(g)

print(id(e))
print(id(f))
print(id(g))

g[0][0]=100
print(g)
print(id(g))

print(id(e))

l2= [1,2,3]
print(id(l2))

l2 = l2+[4,5]
print(l2)
print(id(l2))

# In list, appending,edit,insert will not change address, but concatenate will change address

h = ([100,2],[3,4])
h[0]= h[0] + [5,6]
print(h)


