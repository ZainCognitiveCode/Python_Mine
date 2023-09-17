# Arithmetic Operators

a="Hello" + "-"+ "World"
print(a)

# Multiplication

print("*"*50)

#Subtraction and division do not work in string

# Relational Operaotr
b="Hello" == "World"
print(b)

c="Hello" !="world"
print(c)
d = "Mumbai" > "Pune"
print(d)
# Lexiographically
# In Englsih Dictionary, the word with first letter(p of pune) is after the first letter of previous #word(m of mumbai) then it will be greater,means the second one.

e = "Goa" < "Kolkata"
print(e)

#Capital letters comes first 
f = "kol" < "Kol"
print(f)

# LogicalOperations

g = "Hello" and "World"
print(g)
# In Strings, Python shows empty strings as false and non empty strings are true
h= "" and "Hello"
print(h)

i = "" or "world"
print(i)

j = "Hello" or "World"
print(j)
# There is already 1 in hello,as we conside it as 1 in realtional operator.
k= "Hello" and "World"
print(k)

l = not "Hello"
print(l)
m= not ""
print(m)

# Loops on Strings
n= "Hello world"

for i in n[2:7]:
    print(i)
    
# Membership Operator
print("H" in n)
print("h" in n)





