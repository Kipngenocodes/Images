# Creation of radio buttion where you can choose the answers presented with
from tkinter import *
from PIL import Image, ImageTk

root = Tk()

r = IntVar()


# r.set("2")
def Clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()


root.title("Working With Radio Buttons")
Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: Clicked(r.get())).pack()
Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: Clicked(r.get())).pack()

myLabel = Label(root, text=r.get())
myLabel.pack()

mybutton = Button(root, text="Clicked here", command=lambda: Clicked(r.get()))
mybutton.pack()

root.mainloop()
