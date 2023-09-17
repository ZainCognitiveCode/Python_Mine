# Common Functions
a = "punjab"

print(len(a))

print(max(a))
print(min(a))
print(sorted(a))

# Capitalize/Title/Upper/Lower/Swapcase
# Capitalize will make first letter capital
a.capitalize()
print(a.capitalize())
b = "this is zain"
# Title will made title like text
b.title()
print(b.title())
# Upper will made all the letters upper
b.upper()
print(b.upper())
b.lower()
print(b.lower())
# Swap case will change lower to upper and upper to lower
c= "KoLkAtA"
print(c.swapcase())

# Count
# it will count how many a letter has come in the phrase
c.count("k")
print(c.count("k"))

# Find
d = "It is raining"
print(d.find("g"))
# If a particular letter is not found than it will return -1

# Index
print(d.index("r"))

#endswith
e = "I am zain"
print(e.endswith("zain"))
print(e.endswith("zadf"))

# startswith
print(e.startswith("I"))

# Format
f="Hello my name is {} and I am {}".format("Nitish",20)
print(f)
g="Hello my name is {1} and I am {0}".format("Nitish",20)
print(g)
#In upper example,Nitish is at zero position and 20 is at first position
h="Hello my name is {name} and I am {age}".format(name="Nitish",age=20)
print(h)
i="Hello my name is {name} and I am {weight}".format(name="Nitish",age=20,weight=44)
print(i)






