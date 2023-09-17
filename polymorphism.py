# Polymorphism
#1. method overriding(done)
#2. method overloading
#3. operator overloading



#2. method overloading
class Geometry:
    
    def area(self,a,b=0):
        if b==0:
            print("Circle",3.14*a*a)
        else:
            print("Rect",a*b)
        
obj = Geometry()
(obj.area(4))
obj.area(4,5)
# mein chahta hon ky agr ik value don to upar wala method call ho ur agar aik 2 don to neechay wala.
# technically method overloading python mein kaam nhi krta.


#3. operator overloading

# hum operator overloading magic method sy krty han,jaisy fraction banany mein kia tha.
