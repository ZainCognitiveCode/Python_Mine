from tkinter import *
from tkinter import messagebox

from PIL import ImageTk, Image
def handle_login():
  email = email_input.get()
  password = password_input.get()

  if email== "xain.graphics69@gmail.com" and password == '1234':
    messagebox.showinfo('Login Successfully')
  else:
    messagebox.showerror('Error','Login Failed')

root = Tk()

root.title("Login Form")
root.iconbitmap("single_bird.png")

# root.minsize(400,400)
# root.maxsize(1000,1000)
root.geometry('350x500')

root.configure(background='light blue')
img = Image.open('snow.jpg')
resized_img = img.resize((100,100))
img = ImageTk.PhotoImage(resized_img)
img_label = Label(root,image=img)
img_label.pack(pady=(10,10))

# text ko add krny ky liye label use krty han

text_label = Label(root,text = "Zain", fg= 'white',bg = 'dark blue')
text_label.pack()
text_label.config(font=('rockwell',24))

email_label = Label(root,text='Enter Email',fg ='black',bg='light blue')
email_label.pack(pady=(20,5))
email_label.config(font=('rockwell',12))
email_input = Entry(root, width =50)
email_input.pack(ipady = 6,pady = (1,15))

password_label = Label(root,text='Enter Password',fg ='black',bg='light blue')
password_label.pack(pady=(20,5))
password_label.config(font=('rockwell',12))
password_input = Entry(root, width =50)
password_input.pack(ipady = 6,pady = (1,15))

login_btn = Button(root,text = 'Login Here',bg = 'black',fg = 'light blue', width=15,height=10,command= handle_login)
login_btn.pack(pady=(10,20))
login_btn.config(font=('rockwell',14))

root.mainloop()

