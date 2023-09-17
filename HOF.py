# Higher order Functions

def return_sum(func,L):
    
    result = 0
    
    for i in L:
        if func(i):
            result= result + i
        return result
        

L = [11,14,21,23,56,78,45,29,28]
x = lambda x:x%2==0
y = lambda x:x%2!=0
z = lambda x:x%3 ==0

print(return_sum(x,L))
print(return_sum(y,L))
print(return_sum(z,L))

# Map
# Filter
# Reduce

# Map Function
# it has a function and an iterable(list,tuple etc)

l = [1,2,3,4,5,6,7]
map(lambda x:x*2,l)
print(map(lambda x:x*2,l))
# We have to convert map object in type convert list
print(list(map(lambda x:x*2,l)))
print(list(map(lambda x:x%2==0,l)))

students = [
{
    "name":"Jacob",
    "father name":"Ros Martin",
    "Address": "123 Hill Street",
},
    {
        "name":"Angela",
        "father name":"Robert Steven",
        "Address": "3 Hill Street",
    },
    {
        "name":"Ricky",
        "father name":"William Smart",
        "Address": "Unknown",
    },
]

print(map(lambda student:student["name"],students))
print(list(map(lambda student:student["name"],students)))

# Filter Function
# We can write a condition and it will work only on condition

l = [1,2,3,4,5,6,7]
print(list(filter(lambda x:x>4,l)))

fruits = ["Apple","Orange","Mango","Guava"]
print(list(filter(lambda fruit:"e" in fruit,fruits)))


# Reduce Function
# it reduce our given expression


import functools
l1 = [1,2,3,4,5,6,7]
print(functools.reduce(lambda x,y: x+y,l1))

l2 = [12,34,56,11,21,58]
print(functools.reduce(lambda x,y: x if x>y else y,l2))
print(functools.reduce(lambda x,y: x if x<y else y,l2))

# List Comprehension
# To make a list from a given list

l1 = [1,2,3,4,5,6,7]

l3=[number*2 for number in l1]
print(l3)

l4 = [i**2 for i in range(10)]
print(l4)

l5 =[i**2 for i in range(10) if i%2!=0]
print(l5)


fruits = ["Apple","Orange","Mango","Guava"]
l6 = [fruit for fruit in fruits if fruit[0]=="O"]
print(l6)

# Dictionary Comprehension

D = {"Name": "Zain", "Gender": "Male", "Age": 30}
# We can get list of tuple by this below
print(D.items())

# In this example we will create a new dictionary whose keyword's length is greater than 3
# We use : instead of comma in dictionary for just like with key:value
D1 ={key:value for key,value in D.items() if len(key)>3}
print(D1)

l1 = [1,2,3,4,5,6,7]
D2 = {item: item**2 for item in l1}
print(D2)
D2 = {item: item**2 for item in l1 if item %2==0}
print(D2)






