from tkinter import *
from PIL import ImageTk, Image
def rotate_image():
    global counter
    img_label.config(image=img_array[counter%len(img_array)])
    counter = counter + 1

counter = 1

import os

root = Tk()
root.title("Wallpaper Viewer")
root.geometry("250x400")
root.config(background='black')

files=os.listdir('Wallpapers')

img_array = []
for file in files:
    img = Image.open(os.path.join('Wallpapers',file))
    resized_img = img.resize((700,800))
    img_array.append(ImageTk.PhotoImage(resized_img))


img_label = Label(root,image=img_array[0])
img_label.pack(pady=(15,10))

next_btn = Button(root,text= "Next",bg='white', fg='black',width=25, height=2,command = rotate_image)
# hum command ko btn mein add kren gay takay isko link kr sakain function ky sth.
next_btn.pack()
next_btn.config(font='rockwell')
# pack ka matlab ky dekhai de humain screen pr

root.mainloop()