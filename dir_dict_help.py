# dir return a list of all the attributes and methods(including dunder methods) available for an object. it is a useful tool for discovering what you can do with an object.

x = [1,2,3]
print(dir(x))

# ( __dict__) is sy hum kisi data ko dictionary mein save krty han, data ko organized kr kay

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p = person("John", 30)
print(p.__dict__)

print(help(str))

# help sy hum help lay skty han 




