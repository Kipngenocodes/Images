from tkinter import *

root = Tk()
root.configure(background="Gray")
root.geometry("800x800")

label = Label(root, text="Hello, Welcome to projects Veratis")

# Creation of Labels
first_label = Label(root, text="First Name")
first_label.grid(row=0)

Lastname_label = Label(root, text="Last Name")
Lastname_label.grid(row=1)

Age_label = Label(root, text="Your Age", )
Age_label.grid(row=2)

CountryLabel = Label(root, text="Birth Country")
CountryLabel.grid(row=3)

choose_your_payment_label = Label(root, text="Your Payment")
choose_your_payment_label.grid(row=4)

Credit_label = Label(root, text="Credit Card")
Credit_label.grid(row=6)

Amount_Label = Label(root, text="Contribution Amount")
Amount_Label.grid(row=5)

# creation of entry Boxes
firstname_entry = Entry(root, background="yellow")
firstname_entry.grid(row=0, column=2)

lastname_entry = Entry(root, background="yellow")
lastname_entry.grid(row=1, column=2)

Age_entry = Entry(root, background="yellow")
Age_entry.grid(row=2, column=2)

Country_entry = Entry(root, background="yellow")
Country_entry.grid(row=3, column=2)

Payment_option_entry = Entry(root, background="yellow")
Payment_option_entry.grid(row=4, column=2)

"""Creation of the a function which upon pressing yes or no,
it will lead to opening the new window and clicking to enter credit card
details"""

Amount_entry = Entry(root, background="yellow")
Amount_entry.grid(row=5, column=2)
def yes_button_clicked():

    buttonclicked = Toplevel()
    buttonclicked.title("Credit Card")
    buttonclicked.geometry("400x400")


# Binding the Yes Button in Credit Button with new page to enter information
Credit_entry_button_yes = Button(root, text="Yes", bg="yellow", command=yes_button_clicked)
Credit_entry_button_yes.grid(row=6, column=2)

Credit_entry_button_no = Button(root, text="no", bg="yellow")
Credit_entry_button_no.grid(row=6, column=3)




root.mainloop()
