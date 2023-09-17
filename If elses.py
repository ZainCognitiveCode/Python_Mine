# IF else Statement
# correct email is campusx@gmail.com
# passwrod -1234

email = input("Enter your Email:") 
if '@' in email:
    password = input("Enter your Password :")

    if email == "campusx@gmail.com" and  password == "1234":
        print("Welcome")

    elif email == "campusx@gmail.com" and password != "1234": 
        print("Password is incorrect")   
        password =input("Password again :")
        if password == "1234":
         print("Finally correct")
        else:
         print("Still incorrect")
    else:
        print("Incorrect credentials")
else:
        print("Email is wrong")

