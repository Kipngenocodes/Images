from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Working with MessageBox")


def popup():
    messagebox.showinfo("This is my message", "Hello World!")


Button(root, text="Popup", command=popup).pack()

root.mainloop()
