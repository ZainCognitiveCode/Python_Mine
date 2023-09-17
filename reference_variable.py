#from class1 import Atm
#Atm()

# humnay aik object banaya lakin isko kahin store nhi kia humnay, ab hum isko access kesy kren.is trha object lost ho jaata ha. to usky liye reference variable use krty han hum. 

# hum aisay likhty han 
#sbi = Atm()
# Atm() aik object ha ur iska reference sbi mein store ha. is trha sbi ik variable ha jo us address pr point kr rha ha jaahn Atm() store ha.

class Customer:
     
    def __init__(self,name,gender):
         self.name = name
         self.gender = gender
    
def greet(customer):
    if customer.gender == "Male":
        print("Hello", customer.name,"sir")
    else:
        print("Hello",customer.name,"ma'am")
    
    cust2 =Customer("Nitish", "Male")
    return cust2
        
cust = Customer("Maryam","Female")
new_cust = greet(cust)
print(new_cust.name)
# is baar hum apny class ky object ko as argument pass lr rhy han. phly aisa nhi krty thay hum.
# agr hum function ko list de skty han,tuple ,dictionary de skty han, isi trha hum object bhi de skty han, at the end python mein sb object hi to ha.

# hum as argument bhi kr skty han ur return bhi kr ksty han.




