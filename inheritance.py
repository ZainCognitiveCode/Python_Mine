# Inheritance Relationship

# user on udemy:
# 1. student(login,reg,enroll)
# 2. Teacher(login,reg,create,answer)
# ye upar dono ka data ha. inky andar kuch data repeat ho rhy han dono chezzon mein. iska mtlab ky hum ko code repeat krny ki zaroorat nhi ha blaky hum DRY(do not repeat yourself) use kren gay, phir hum aik ur class banain gay jo student ur teacher mein  repeat ho rhy han ur hum un dono ko inherit kr skain gay un dono mein.

# ab user mein (login,reg) ho ga.
# ab hum ye student ur teacher mein use kr ksty han.

# inheritance gives benifit of code usability.
# inheritance upar ki direction mein hota ha, mean ky ap as a student user sy data lay skty ho lakin user student ka data nhi use kr skta ha.

# hum "Data members", "methods", "constructors", ye 3 chezain inherit krty han hum.
# private members are not inheritance, koi underscore wala data.


class User:
    
    # ye nechy wala method ha,constructor __ is say show hota ha
    def login(self):
        print("Login")
    def register(self):
        print("Register")
 # hum neechy bracket mein User likhain gy jis sy pata lagay ga kay student child ha ur User parent ha.       
class Student(User):
    
    def enroll(self):
        print("Enroll")

    def review(self):
        print("Review")
 
        
stu1 = Student()
stu1.enroll()
stu1.review()
stu1.register()
stu1.login()


# hum inheritance mein reverse nhi kr skty.
 
u = User()   
u.enroll()
u.review()
u.register()
u.login()
# ye code crash kr jaye ga.

