# Relationship
# do classes ky darmyan mein relationship hota ha
# 1. Aggregation(Has-A)
# 2. Inheritance(Is-A)

# aik humary pass class ha product ur dosri smartphone ha, to smartphone ur product ka relationship inheritance ha. ye dono classes han.

# aik vehicle ha ur car class ha. ye dono ka relation bhi inheritance ha.

# let's say ky humaray pass aik class h jaisy customer ki details,ur aik ur class ha address. means "customer has a address".
# agar ksi class ko koi class chahiye hota ha to wo aggregation ha.


class Customer:
    
    def __init__(self,name,gender,address):
        self.name = name       
        self.gender = gender      
        self.address = address 
        
    def edit_profile(self,new_name,new_city,new_pin,new_state):
      self.name = new_name  
      self.address.change_address(new_city,new_pin,new_state)  
      
       
class Address:
       def __init__(self,city,pincode,state):
        self.city = city
        self.pincode = pincode
        self.state = state

       def change_address(self,new_city,new_pin,new_state):
        self.city = new_city
        self.pincode = new_pin
        self.state = new_state
        
add = Address("Kolkata",7001565,"WB")
cust = Customer("Nitish","Male", add)

cust.edit_profile("Nitish","Gurgaon",122011,"Punjab")
print(cust.address.pincode)

# isi relationship ko aggregation kehty han.











