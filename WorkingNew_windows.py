from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


# Creating an open button which have to be clicked to open second window.


root = Tk()
root.title("Working With New windows.")

def open():
    global my_image
    top = Toplevel()
    top.title("Top Window.")
    label = Label(top, text="Helloworld").pack()
    my_image = ImageTk.PhotoImage(Image.open("hopsin5.png"))
    my_label = Label(top, image=my_image).pack()

buttonclicked= Button(root, text="Click to Open", command=open).pack()

root.mainloop()
