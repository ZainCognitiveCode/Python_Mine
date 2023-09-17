# pass by refernce mein id same ho ge.
# just like aliasing.

# agar humnay aik function mein object ko send kia h to us function nay agar object ko change kr dia to wo f=generally bhi change ho jaye ga.

class Customer:
     
    def __init__(self,name,gender):
         self.name = name
         
    
def greet(customer):
    print(id(customer))
    customer.name = "Nitish"
    print(customer.name)
    print(id(customer))
       
        
cust = Customer("Maryam","Female")
#print(id(cust))

greet(cust)
print(cust.name)

# class ke objects bhi mutalbe han,yani change ho skty han like list,dict and sets

def change(L):
   print(id(L))
   L.append(5)
   print(id(L))
L1 = [1,2,3,4]
print(id(L1))
print(L1)

change(L1)
print(L1)

# yani list mein change to ho gya lakin address wahi raha ha. humain list ky liye cloning krna chahiye
# agr hum tuple pr krty to wo immutable ha.

# tuple example
def change(l):
   print(id(l))
   l = l + (5,6)
   print(id(l))
   
l1 = (1,2,3,4)
print(id(l1))
print(l1)

change(l1)
print(l1)

# tuple mein change nhi aya ha.



