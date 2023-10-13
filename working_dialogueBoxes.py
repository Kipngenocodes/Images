from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()
root.title("Working with DialogueBoxes")


def open_file():
    global image_view
    root.filename = filedialog.askopenfilename(initialdir="imagespy", title="Select File",
                                               filetypes=(("png files", "*.png"), ("all files", "*.*")))
    # mylabel = Label(root, text=root.filename, font=("Helvetica")).pack()
    image_view = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=image_view).pack()

top= Toplevel
opening_button = Button(root, text="click to open image", command=open_file).pack()



root.mainloop()
