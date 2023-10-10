from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Working with MessageBox")


# messagebox.showinfo()
# messagebox.askyesno()
# messagebox.askquestion()
# messagebox.showerror()
# messagebox.showinfo()
# messagebox.askokcancel()
def popup():
    messagebox.showerror("An error occured", "Hello World!")


Button(root, text="Popup", command=popup).pack()

root.mainloop()
