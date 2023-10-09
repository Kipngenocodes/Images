# Creation of radio buttion where you can choose the answers presented with
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
  
r = IntVar()

root.title("Working With Radio Buttons")
Radiobutton(root, text="Option 1", variable=r, value=1).pack()
Radiobutton(root, text="Option 2", variable=r, value=2).pack()

root.mainloop()
