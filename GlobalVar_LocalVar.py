# Ram is city,global frame is your house. jab hum function ko call kren gay to ghr mein aik room create ho jaye ga. jb fnc ka kaam khatam hoga to ye room khatam ho jaye ga.agar koi func return nhi kr raha to uski value none ha.

# Local_Variable and Global_Variable

# agr func ky pass local varibale nhi ha to wo global varibale use kr lay ga.
# hum global ko use kr skty han, usky andar change nhi kr skty kuch.
# hum global keyword use krkay change kr skty han value, lakin ye acha nhi ha.

def f():
    print("Inside f")
    def g():
        print("Inside g")
    g()

print(f())

#print(g()) 
# inner func main program sy hidden rehta ha,is liye isko pata hi nhi ky g() ka func bhi banaya ha humnay

# evverything is object in python

# Functions as objects

def f(num):
    return num**2
print(f(2))
print(f(4))

x= f
print(x(2))

del f
#print(f(2))

print(x(2))

print(type(x))

L= [1,2,3,4,x]
print(L)

print(L[-1](3))
# mean isny function use kia ha ur usko 3 value de ha
L= [1,2,3,4,x(5)]
print(L)


