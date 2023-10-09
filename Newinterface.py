from tkinter import *

root = Tk()
root.geometry("600x600")
root.title("Webmaster Management Holdings")

# getting the label first
first_namelabel = Label(root, text="First Name")
last_namelabel = Label(root, text="Last Name")
email_label = Label(root, text="Email Address")
year_of_birthlabel = Label(root, text="Year of birth", )
county_label = Label(root, text="Your Country of Birth")
Contact_Label = Label(root, text="Contacts.")

# Creating Entry Boxes for the labels
first_name_entry = Entry(root, width=40, borderwidth=0)
last_name_entry = Entry(root, width=40, borderwidth=0)
email_label_entry = Entry(root, width=40, borderwidth=0)
year_of_birth_entry = Entry(root, width=40, borderwidth=0, show="# ")
county_entry = Entry(root, width=20, borderwidth=0)
Contact_entry = Entry(root, width=30, borderwidth=0)

status_bar= Label(root, text="Thank you for Visiting our Page",bd=2, relief=SUNKEN, anchor=W)

# Creating the grid for each label and entry boxes
first_namelabel.grid(row=0, column=0)
first_name_entry.grid(row=0, column=1)

last_namelabel.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

email_label.grid(row=2, column=0)
email_label_entry.grid(row=2, column=1)

year_of_birthlabel.grid(row=3, column=0)
year_of_birth_entry.grid(row=3, column=1)

county_label.grid(row=4, column=0)
county_entry.grid(row=4, column=1)

Contact_Label.grid(row=5, column=0)
Contact_entry.grid(row=5, column=1)

Welcoming_Label = Label(root, text="Welcome On Board.", padx= 100, pady=0)
company_label =Label(text="In case of of any problem kindly reach: www.webstersolution.com", padx= 100, pady=0)

Welcoming_Label.grid(row=20, column=1)
company_label.grid(row=21, column=1)
status_bar.grid(row=23, column =1, columnspan=4, sticky=W+E)

root.mainloop()
