#isalnum/isalpha/isdecimal/isdigit/isidentifier

a = "Flat20".isalnum()
print(a)
b = "flat#".isalnum()
print(b)
c = "flat20".isalpha()
print(c)
d= "Hello World".isidentifier()
print(d)
# Because there is a spcae between characters
#if we put underscore then it will be true

    #Split
e = "Who are you?".split()
print(e)
# It converts string to list
f = "Who are you?".split("are")
print(f)
    #Join
# it joins a list into string
" ".join(['Who', 'are', 'you?'])
print(" ".join(['Who', 'are', 'you?']))
"/".join(['Who', 'are', 'you?'])
print("/".join(['Who', 'are', 'you?']))

    #replace
"Hi i am zain".replace("zain","Umer")
print("Hi i am zain".replace("zain","Umer"))

    #Strip
# it removes spcae which are leading 
h = "           Zain        "
print(h.strip())
 
