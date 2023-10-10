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
    messagebox.askquestion("Are you Okay", "Be okay!")


Button(root, text="Popup", command=popup).pack()

root.mainloop()
