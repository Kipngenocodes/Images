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
    response= messagebox.askyesno("Question", "Are clicking unsafe Links!")
    # mylabel=Label(root, text=response).pack()
    if response==1:
        Label(root, text="You Clicked Yes!").pack()
    else:
        Label(root, text="You Clicked a No!").pack()



Button(root, text="Popup", command=popup).pack()

root.mainloop()
