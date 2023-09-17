# SUPER KEYWORD

#super keyword is used to refer to the parent class. It is especially useful when a class inherits from multiple parent classes and you want to call a method from one of the parent class.

#class ParentClass:
#    def paret_method(self):
#        print("This is the parent method.")

#class ChildClass(ParentClass):
#    def child_method(self):
#        print("This is the child method.")
#        super().paret_method()

#child_object = ChildClass()
#child_object.child_method()

class Employee:
    
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Programmer(Employee):
    def __init__(self,name,id,lang):
            super().__init__(name,id)
            self.lang = lang
            
 
Zain = Employee("Zain Ul Abideen", "420")       
harry = Programmer("Harry", "42011", "python")
print(Zain.name)  
print(Zain.id)  
print(Zain.lang)  

# do not repeat yourself.

# ab programmer sub class ha ur Employee super class ha.     