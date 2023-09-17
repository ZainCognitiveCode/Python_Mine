# Dictionary
d ={"Name":"Nitish","Gender":"Male"}
print(d)

# R1: Has no indexind
# R2: Is a mutable types
# R3: Keys-> immutable,values->they can be mutable
# R4: Keys should be unique

# Mutable->Lists,sets,Dictionary
# Immutable: Strings,tuples,int,float,Boolean,complex

# Create
D = {}
print(D)

D1= {"Name":"Nitish","Gender":"Male"}
print(D1)

#D2 ={[1,2,3]:"Nitishh"}
#print(D2)
# It is also using hashing technique

# kEYS WILL BE IMMUTABLE

d3 = {"Name":"Rahul","Name":"Rohit"}
print(d3)
# Python thought that you want to update the value of the key,so it only shows rohit

# 2D Dictionary
D4 = {"Name":"Zain","College":"PGC","Marks":{"M1":"56","Ds":"54"}}
print(D4)
# We can also make 3D,4D Dictionary

# Access items from Dictionary

#print(d3[0])
# This above method will not work

# We can only access by using key
print(d["Name"])


# Access in 2D,3D
 
D4 = {"Name":"Zain","College":"PGC","Marks":{"M1":"56","Ds":"54"}}
print(D4["Marks"])

print(D4["Marks"]["M1"])

# Edit
D4 = {"Name":"Zain","College":"PGC","Marks":{"M1":"56","Ds":"54"}}
D4["Name"]="Bilal"
print(D4)

D4["Marks"]["M1"]=55
print(D4)

# We can also access by get function

print(D4.get("Name"))

# Add new key-value pairs
D5 = {"Name":"Zain","College":"PGC","Marks":{"M1":"56","Ds":"54"}}
D5["Age"]=32
print(D5)
D5["Marks"]["M2"]=33
print(D5)

# Delete 
# we can delete a dictionary by del
#del D5
#print(D5)

del D5["Name"]
print(D5)

D5.clear()
print(D5)

# Operations

D6 = {"Name":"Zain","College":"PGC","Marks":{"M1":"56","Ds":"54"}}
D7 = {6,7,8,9,10}
# We can not do concatenation in Dictionary and multiplication

for i in D6:
    print(i)
# We will only get key values in loop

for i in D6:
    print(i,D6[i])


# Membership

print("Zain" in D6)

# In Dictionary, it only about keys, so use key only in membership

print("Name" in D6)

print(len(D6))

print(min(D6))
print(max(D6))
print(sorted(D6))
print(sorted(D6,reverse=True))

print(D6.keys())
print(D6.values())














