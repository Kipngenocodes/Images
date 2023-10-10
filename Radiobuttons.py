# Creation of radio buttion where you can choose the answers presented with
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Working With Radio Buttons")
r = IntVar()


# r.set("2")
def Clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()

Capital_cities =[
    ("Kenya","Nairobi"),
    ("Uganda", "Kampala"),
    ("Tanzania","Dar Es Salam"),
    ("Rwanda", "Kigali"),
    ("Burundi", "Bujumbura"),
]

capital =StringVar()
capital.set("Nairobi")

for country, city in Capital_cities:
    Radiobutton(root, text=country, variable=capital, value=city).pack()

# Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: Clicked(r.get())).pack()
# Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: Clicked(r.get())).pack()

myLabel = Label(root, text=capital.get())
myLabel.pack()

mybutton = Button(root, text="Clicked here", command=lambda: Clicked(capital.get()))
mybutton.pack()

root.mainloop()
