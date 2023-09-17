#Exampl 1
class Phone:
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera
        
class SmartPhone(Phone):
    pass
s = SmartPhone(2000,"Apple",13)
print(s.brand)
# agr class b, class A sy inherit kr rha ha to jb hum class B ka object banain gay to wo class A ka constructor ko call karay ga.

# Example 2:
class Phone:
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.price = price
        self.__brand = brand
        self.camera = camera
        
class SmartPhone(Phone):
    pass
s = SmartPhone(2000,"Apple",13)
print(s.__brand)

# code crash kr jaye ga,agr child class ka object parent class ky hidden item ko call kray ga to.

# is neechy wali example mein dono ky pass buy ha.
class Phone:
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera
    def buy(self):
        print("Buying a  phone")   
         
class SmartPhone(Phone):
    
    def buy(self):
        print("Buying a smart phone") 
        
s = SmartPhone(2000,"Apple",13)
s.buy()

# Smartphone ka buy call ho ga. isko method overriding kehty han. agr parent ur child mein same chezain han to child wala call ho ga.


# Method Overriding-> Polymorphism
# Method Overloading
# Operator Overloading

# Example 3

class parent:
    
    def __init__(self,num):
     self.__num = num
    def get_num(self):
     return self.__num
 
class Child(parent):
    
    def show(self):
        print("This is in child class")

son = Child(100)
print(son.get_num())        # 100
son.show()                  # This is in child class


# Example 4
class parent:
    
    def __init__(self,num):
     self.__num = num
     
    def get_num(self):
     return self.__num
 
class Child(parent):
    
    def __init__(self,val,num):
        self.__val = val
        
    def get_val(self):
        return self.__val
    
son = Child(100,10)
print("Parent: Num",son.get_num()) 
# is example mein child ky pass constructor bhi ha.
#output : code crash karay ga. kyukny child ka constructor kaam kr gya ha,lakin parent ka nhi kia kyunky agar child ky pass constructor ha to wo apna hi use kry ga srf, self.__num initalize hi nhi hua to uski value set nhi hui to get_num kesy kam karay ga.


# Example 5

class A:
    
    def __init__(self):
        self.var1 =100
        
    def display1(self,var1):
        print("class A:", self.var1)
        
class B(A):
    
    def display2(self,var1):
        print("class B:", self.var1)
        
obj = B()
obj.display1(200)       # output: class A: 100


# Example 6 (SUPER)

class Phone:
    
    def __init(self,price,brand,camera):
        print("Inside phone constructor")
        self.__price = price
        self.__brand = brand
        self.__camera = camera
        
    def buy(self):
        print("Buying a phone")

class SmartPhone(Phone):
    
    def buy(self):
        print("Buying a smartphone")
        super().buy()
  # jab bhi hum super() use kren gay to iska mtlab ye ha kay hum parent ky buy ko call kr skty han. super sy hum parent ka method ur constructor,attribute nhi kr skty.     
s = SmartPhone(20000, "Apple",14)
s.buy()


# Example 7
class Phone:
    
    def __init(self,price,brand,camera):
        print("Inside phone constructor")
        self.__price = price
        self.__brand = brand
        self.__camera = camera
        
class SmartPhone(Phone):
    
    def __init(self,price,brand,camera,os,ram):
        print("Pehle yahan")
        super().__init__(price,brand,camera)    #ab ye call karay ga parent ky construcot ko,
        self.os = os
        self.ram = ram
        print("Inside smartphone constructor")
s = SmartPhone(20000,"Samsung",12,"Android",2)
print(s.os)
print(s.brand)



# Eample 8

class Parent:
    
    def __init__(self,num):
        self.__num = num
    
    def get_num(self):
        return self.__num
    
class Child(parent):
    
    def init__(self,num,val):
     super().__init__(num)
     self.__val = val
     
     def get_val(self):
         return self.__val
     
son = Child(100,200)
print(son.get_num())        #output 100
print(son.get_val())        # output 200


# EXAMPLE 9

class Parent:
    
    def __init__(self,num):
        self.__num = 100
        
    def show(self):
        print("Parent:", self.__num)

class Child(parent):
    
    def __init__(self):
        super().__init()
        self.__var = 10
    
    def show(self):
        print("Child:", self.__var)         # ye wala son.show() pr show ho ga

dad = Parent()
dad.show()
son = Child()
son.show()


# Types of Inheritance

#1. Single level(one parent and one child)
#2. Multi level inheritance(dada,papa,child)(isky andar child papa ur dada ko access kr skta ha,ur papa dada ko)
#3. Hierarrchical inheritance (one parent and two child)
#4. Multiple inheritance (one child and two parent)

# pyhton mein multiple hota ha ur java mein nhi.

# hybrid inheritance
# is mein hr type ki inheritance hoti ha.


#1. Single level
# ye hum observe kr chukay han

#2. Multi level inheritance

class Product:
    def review(self):
        print("Product customer review")
    
class Phone(Product):
    def __init__(self,price,brand,camera):
      print("Inside phone constructor")
      self.__price = price
      self.brand = brand
      self.camera = camera
      
      def buy(self):
          print("Buying a phone")


class SmartPhone(Phone):
    pass

s = SmartPhone(20000, "Apple", 12)
p = Phone(100, "Samsung", 1)
s.buy()
s.review()
p.review()


# 3. Multiple inheritance

class Phone(Product):
    def __init__(self,price,brand,camera):
      print("Inside phone constructor")
      self.__price = price
      self.brand = brand
      self.camera = camera
      
    def buy(self):
        print("Buying a phone")
        

class Product:
    def review(self):
        print("Product customer review")

class SmartPhone(Phone,Product): # two things inherit. by comma (# agar upar dono mein constructor hoga to sb sy phle uska constructor call hoga jo bracket mein phly likha ha)
    pass

s = SmartPhone(20000, "Apple", 12)      

s.buy()
s.review()

# MRO (METHOD RESOLUTION ORDER)
#jis order mein inherit kr rhy ho,jis ko phly likha ha







    


