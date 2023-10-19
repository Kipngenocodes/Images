from tkinter import *
from tkinter import messagebox

# import checkingforalphabates 


root = Tk()
root.configure(background="Gray")
root.geometry("800x800")

label = Label(root, text="Hello, Welcome to projects Veritas")

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
firstname_entry = Entry(root, background="yellow", )
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


def credit_card(do_validation=None, do_validations_date=None, do_validations_cvv_entry=None):
    top = Toplevel()
    top.title("Credit Card")
    top.geometry("500x500")

    # Creation of credit card input details
    credit_card_num = Label(top, text="Credit Card Number:")
    credit_card_num.grid(row=0, column=0)

    credit_card_num_entry = Entry(top, width=40, validatecommand=do_validation)
    credit_card_num_entry.grid(row=0, column=1)
    credit_card_num_entry.insert(0, "Enter Credit Card Number")

    def do_validations():
        value = credit_card_num_entry.get()
        if value.isdigit():
            return value
        else:
            messagebox.showerror("Error", "Invalid Credit Card")

    credit_card_Names = Label(top, text="Card Names:")
    credit_card_Names.grid(row=1, column=0)

    credit_card_Names_entry = Entry(top, width=40)
    credit_card_Names_entry.grid(row=1, column=1)
    credit_card_Names_entry.insert(0, "Enter Your Names")

    credit_card_expiration_date = Label(top, text="Expiration")
    credit_card_expiration_date.grid(row=3, column=0)

    credit_card_expiration_date_entry = Entry(top, width=15, validatecommand=do_validations_date)
    credit_card_expiration_date_entry.grid(row=3, column=1)
    credit_card_expiration_date_entry.insert(0, "MM/YYYY")

    def do_validations_date():
        value = credit_card_expiration_date_entry.get()
        if value.isdigit():
            return value
        else:
            messagebox.showerror("Error", "Invalid data entered")

    credit_card_Security_CVV = Label(top, text="CVV Number:")
    credit_card_Security_CVV.grid(row=4, column=0)

    credit_card_Security_CVV_entry = Entry(top, width=15, validatecommand=do_validations_cvv_entry)
    credit_card_Security_CVV_entry.grid(row=4, column=1)
    credit_card_Security_CVV_entry.insert(0, "CVV Number")
    '''Creating functions which will allow Names to be is alpha while cvv and card number is
    numeric.'''

    def do_validations_CVV_entry():
        value = credit_card_Security_CVV_entry.get()
        if value.isdigit():
            return value
        else:
            messagebox.showerror("Error", "Invalid CVV entered, numbers only")

    enter_button = Button(top, text="Enter")
    enter_button.grid(row=5, column=3)



# Binding the Yes Button in Credit Button with new page to enter information
credit_entry_button_yes = Button(root, text="Yes", bg="yellow", command=credit_card)
credit_entry_button_yes.grid(row=6, column=2)

credit_entry_button_no = Button(root, text="no", bg="yellow", )
credit_entry_button_no.grid(row=6, column=3)





root.mainloop()
