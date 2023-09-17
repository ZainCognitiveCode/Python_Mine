# OOP is a different style of writing code.
# Requirement of OOP

L = [1,2,3,4]
#L.upper()
# agar hum upper func ko call kren to ye error de ga kay attribute error. list object has no attribute upper.

city ="Kolkata"
#city.append("a")

#a = 3
#a.upper()

# Everything in python is object

# What is object

# The problem
# Everything is online. We can do 8 months work in 2 months.

# Generality to specificity
# general ho ur specific ho.

# hum OOP sy khud ky data type bana skty han. takay hum apna jo bhi software banain wo humaray use ky liye hi ho. 

# OOP ky concepts:
# class
# object
# polymorphism
# Encapsulation
# Inheritance
# Abstraction 

# What is class?
# class is a blueprint
# object jo python mein hota ha na wo ksi class ka hota ha object.

a = 2
print(type(a))
# yahan a object ha,integer object. iski class integer ha.

# hum jb l. likhty han to kuch func show hotay han jo hum us object ky liye use kr skty han,jaisay list ky liye append,clear,copy waghera. isi trha hum khud bhi apny object ky func bana skty han.

# datatype class hota ha, ur us datatype ko jb variable banaty ho to wo object of class hota ha.
L = [1,2,3,4]
# yahan pr jo L h wo object ha, list class ka.
# class ko banany mein ziada time lagay ga.


# class ky andar 2 chezain han

# 1.data or property/ attribute
# 2.functions or behavior/ method

# jaisay car ky andar 
# class : color,no. of wheels,engine type
# behavior: speed,velocity, air bag,gps waghera



# Class Basic Structure

class Car:
    color = "blue" # data
    model = "sports" # data
def calculateAvgSpeed(km,time):
    # some code


# hum class ko define krty han,phr fucntion ko define krty han usky baad. car class ha upar, ur calculateAvgSpeed function ha

# Class ka naam should be in Pascal case
#ThisIsPascalCase
# snake case : snake_case
# jb bhi class bnao to class ka name pascal mein ho, ur variables or data ka name snakecase ho ga.

    # Car
    
# Class 
 # color    -
 # mileage  -
 # engine   -
 
 # Function
 
 #cal_avg_speed +
 #open_airbage  +
 
 # + ka mtlab public ha. ur - ka mtlab private ha.
 
 # Object is an instance of the class
 
 # Object Examples
 
 # 1. car       wagorR  //  wagnor=car()
 # yahan object name wagnor ha ur class car() ha.
 
 # L= [1,2,3]

 # list aik class ha, to hum iska object upr ki trha kyun banatay han.
 
 # hum built-in function ky liye object literal use krtay han. 
 # hum is trha bhi object bana skty han list ka: L= list()
 # exp : city = str()
 
 
 # function vs methods
# methods are functions which are written inside a class,where function is a normal function.

 # len(L)
 # L.append(L)
 # is mein upar wala function ha ur neechay wala method ha. jb hum L. ky zariye call kren ur agay phir ik list ajaye functions ki to wo method functions han . ur baki general functions ko waisy hi likhty han.
 # method ky function ko srf class call kr skta ha.

# hum class ky andar variable aisy define krty han:
# def __init__():