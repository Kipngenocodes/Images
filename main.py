from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Using Images with the Word")
root.iconbitmap("image.ico")

image_one = ImageTk.PhotoImage(Image.open("image.png"))
image_two = ImageTk.PhotoImage(Image.open("hopsin1.png"))
image_three = ImageTk.PhotoImage(Image.open("Hopsin2.png"))
image_four = ImageTk.PhotoImage(Image.open("hopsin3.png"))
image_five = ImageTk.PhotoImage(Image.open("hopsin4.png"))
image_six = ImageTk.PhotoImage(Image.open("hopsin5.png"))

image_list = [image_one, image_two, image_three, image_four, image_five, image_six]

mylabel = Label(image=image_one)
mylabel.grid(row=0, column=0, columnspan=3)


def forward(image_number):
    global mylabel
    global button_back
    global button_forward

    mylabel.grid_forget()
    mylabel = Label(Image=image_list[image_number - 1])
    mylabel.grid(row=0, column=0, columnspan=3)


def back():
    global mylabel
    global button_back
    global button_forward


button_back = Button(root, text="<<", command=back)
button_quit = Button(root, text="Exit the program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()
