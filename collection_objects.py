# Collection of objects
class Customer:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def intro(self):
        print("I am",self.name, "and I am", self.age)
        
c1 = Customer("Nitish",33)
c2 = Customer("Zain",45)
c3 = Customer("Bilal",32)

L = [c1,c2,c3]
# it is list of objects

for i in L:
    i.intro()
# intro ko call kr rhy han is liye print use nhi kia.



