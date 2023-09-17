# # Exception handling is the process of responding to unwanted or unexpected events when a computer program runs. Exception handling deals with these events to avoid the program or system crashing, and without this process, exceptions would disrupt the normal operation of a program.


# mein chahta hon ky agr mera prograam shi sy run hota ha to theek ha,agar nhi to phir kuch ur run ho jaye.
a = input("Enter the number: ")
print(f"Multiplication table of {a} is:")

try:
 for i in range(1,11):
    print(f"{int(a)}X {i}= {int(a)*i}")
     
except Exception as e:
 print("Sorry some error occurred")
 
 # or 
 # except:
 # print("Invalid Input!")
 
 # is ka mtlab ky try mein code jo ha wo chalay ur agar error ata ha to usko nikaal kr bki program run karay.
 
# hum multiple except bhi use kr skty han.

 


