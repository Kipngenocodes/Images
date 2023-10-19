from tkinter import*
from tkinter import messagebox

root = Tk()
def check():
    sel = e.get()

    if not sel.isalpha():
        messagebox.showerror('Only letters', 'Only letters are allowed!')
e = Entry(root)
e.pack(pady=10)