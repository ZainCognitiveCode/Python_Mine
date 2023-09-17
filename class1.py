class Atm:
 
 # class ky data ko object hi access kr skta ha.
 # Constructor: special/magic/dunder, agr kisi method ky liye agay ur peechy double underscore laga ho. ye python mein pre defined han. object constructor ko call nhi kr skta. iska code us waqt execute hoga jb hum object bana lain gy. constructor ka control user ky pass nhi ha. constructor ko configuration ky liye use krty han hum.ismein wo code hota ha jo app ky start hotay hi user sy pochy bina execute ho jaye.
 
 
 # init constructor ha. it is a special method,whose code automatically executes when we make an object of class Atm: python ky constructor ka name init hi hona chahiye   
    
    # static/class: we access instance var by self. method and statuc variable hum class ky name ko likh kr phr variable likhty han
    
    counter = 1
    def __init__(self):
        self.__pin = ""
        self.__balance = 0
        self.sno = Atm.counter
        Atm.__counter = Atm.__counter + 1
        
        print(id(self))
        self.__menu()
    
    @staticmethod
    # is upr walay ka mtlab ye ha ky in variables ko keyword ki zaroorat nhi ha.
    def get_counter():
        return Atm.__counter
    
    @staticmethod
    def set_counter(new):
        if type(new)== int:
            Atm.__counter = new
        else:
            print("Not allowed")        
    def get_pin(self):
        return self.__pin
    
    
    def set_pin(self,new_pin):
     if type(new_pin)==str:
         self.__pin = new_pin
         print("Pin changed")
     else:
          print("Not allowed")
        
    def __menu(self):
        user_input =input("""
                     Hello,how would you like to proceed?
                     1. Enter 1 to create pin
                     2. Enter 2 to deposit
                     3. Enter 3 to withdraw
                     4. Enter 4 to check balance
                     5. Enter 5 to exit     
                          """)
        if user_input == "1":
            self.create_pin()
        elif user_input== "2":
            self.deposit()
        elif user_input== "3":
            self.withdraw()
        elif user_input== "4":
            self.check_balance()
        else:
            print("Bye")
            
    def create_pin(self):
        self.__pin = input("Enter your pin")
        print("pin set successfully")
        self.__menu()
        
    def deposit(self):
        temp = input("Enter your pin")
        if temp == self.__pin:
            amount = int(input("Enter the amount"))
            self.__balance = self.__balance+amount
            print("Deposit successfully")
        else:
            print("Invalid pin")
        self.__menu()
        
    def withdraw(self):
        temp = input("Enter your pin")
        if temp == self.__pin:
            amount = int(input("Enter the amount")) 
            if amount<self.__balance:
                self.__balance= self.__balance - amount
                print("Withdrawl successful")
            else:
                print("Insufficient funds")
        else:
            print("invalid pin")
        self.__menu() 
              
    def check_balance(self): 
         temp = input("Enter your pin")
         if temp == self.__pin: 
             print(self.__balance)
         else:
            print("invalid pin")    
         self.__menu()
        

# instance variable:
# jo variables constructor mein banaty han wo instance variable han, inki value har object ky liye alag ha.



        
     
        