from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("Working With New windows.")
top = Toplevel()
top.title("Top Window.")
label = Label(top, text="Helloworld").pack()
my_image = ImageTk.PhotoImage(Image.open("hopsin5.png"))
my_label = Label(top, image=my_image).pack()

root.mainloop()
