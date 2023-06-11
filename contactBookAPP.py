import tkinter as tk
from tkinter import messagebox
import re
import datetime
import sqlite3
import json
import csv
from tkinter import filedialog, PhotoImage, Scrollbar


class Contact:
    def __init__(self, name, phone_number):
        """
        Initialize a Contact object.

        Args:
            name (str): The name of the contact.
            phone_number (str): The phone number of the contact.
        """
        self.name = name
        self.phone_number = phone_number

    def get_name(self):
        """
        Get the name of the contact.

        Returns:
            str: The name of the contact.
        """
        return self.name

    def set_name(self, name):
        """
        Set the name of the contact.

        Args:
            name (str): The new name for the contact.
        """
        self.name = name

    def get_phone_number(self):
        """
        Get the phone number of the contact.

        Returns:
            str: The phone number of the contact.
        """
        return self.phone_number

    def set_phone_number(self, phone_number):
        """
        Set the phone number of the contact.

        Args:
            phone_number (str): The new phone number for the contact.
        """
        self.phone_number = phone_number

    def __str__(self):
        """
        Get a string representation of the contact.

        Returns:
            str: A string representation of the contact.
        """
        return f"Name: {self.name}, Phone Number: {self.phone_number}"

class EditContactWindow(tk.Toplevel):
    """
        Initialize the EditContactWindow.

        A class representing editor of contacts in the "Contact Book"

        Args:
            main_window (tk.Tk): The main window instance.
            contact (Contact): The contact object to be edited.

    """
    def __init__(self, main_window, contact):
        super().__init__()
        self.title("Edit Contact")

        self.main_window = main_window
        self.contact = contact

        self.LabelName = tk.Label(self, text='Name:')
        self.LabelName.grid(row=0, column=0, sticky=tk.W)

        self.LabelPhone = tk.Label(self, text='Phone:')
        self.LabelPhone.grid(row=1, column=0, sticky=tk.W)

        self.EntryName = tk.Entry(self)
        self.EntryName.grid(row=0, column=1)
        self.EntryName.insert(tk.END, contact.name)

        self.EntryPhone = tk.Entry(self)
        self.EntryPhone.grid(row=1, column=1)
        self.EntryPhone.insert(tk.END, contact.phone_number)

        self.ButtonSave = tk.Button(self, text='Save', command=self.save_contact)
        self.ButtonSave.grid(row=2, column=0, columnspan=2, pady=10)

    def save_contact(self):
        """
        Save the edited contact.

        Retrieves the new name and phone number from the entry fields.
        Updates the contact object with the new information.
        Updates the contact in the main window.
        Displays a success message and closes the EditContactWindow.

        """
        new_name = self.EntryName.get()
        new_phone = self.EntryPhone.get()

        # Update the contact attributes
        self.contact.name = new_name
        self.contact.phone_number = new_phone

        # Update the contact in the main window
        self.main_window.update_contact(self.contact)

        messagebox.showinfo("Success", "Contact updated successfully.")
        self.destroy()   

class AuthorPage(tk.Toplevel):
    """
    A class representing the author information page.
    """

    def __init__(self, parent):
        """
        Initialize the AuthorPage object.
        """
        super().__init__(parent)
        self.geometry("400x300")
        self.title("Author Information")
        self.configure(background="#FFFFF5")

        self.LabelAuthor = tk.Label(self)
        self.LabelAuthor.place(relx=0.2, rely=0.2, height=21, width=120)
        self.LabelAuthor.configure(anchor='w')
        self.LabelAuthor.configure(background="#FFFFF5")
        self.LabelAuthor.configure(compound='left')
        self.LabelAuthor.configure(disabledforeground="#a3a3a3")
        self.LabelAuthor.configure(foreground="#000000")
        self.LabelAuthor.configure(text='''Author: John Doe''')

        self.ButtonClose = tk.Button(self, command=self.destroy)
        self.ButtonClose.place(relx=0.4, rely=0.6, height=24, width=93)
        self.ButtonClose.configure(activebackground="#ececec")
        self.ButtonClose.configure(activeforeground="#000000")
        self.ButtonClose.configure(background="#FFFFF5")
        self.ButtonClose.configure(disabledforeground="#a3a3a3")
        self.ButtonClose.configure(foreground="#000000")
        self.ButtonClose.configure(highlightbackground="#d9d9d9")
        self.ButtonClose.configure(highlightcolor="black")
        self.ButtonClose.configure(pady="0")
        self.ButtonClose.configure(text='''Close''')

        self.transient(parent)
        self.grab_set()
        self.parent = parent

    def show(self):
        """
        Show the author information page.
        """
        self.parent.withdraw()
        self.lift()

class Toplevel1:
    """
    A class representing a contact book.

    Attributes:
        contacts (list): A list of contacts stored in the contact book.
    """

    def __init__(self, top=None):
        """
        Initialize the ContactBook object.
        """

        # Setting basic parameters of GUI window
        top.geometry("800x450+468+138")
        top.resizable(0, 0)
        top.title("Contact Book")
        top.configure(background="#FFFFF5")

        # contacts list to store all data from file
        self.contacts = []
        self.top = top

        # Create a connection to the SQLite database
        self.connection = sqlite3.connect("contacts.db")
        self.cursor = self.connection.cursor()

        # Create the contacts table if it doesn't exist
        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS contacts
            (name TEXT, phone_number TEXT)'''
        )
        self.connection.commit()

        
        #"Hamburger" toggle menu
        self.head_frame = tk.Frame(root, background="#EEEED2", highlightbackground="cornsilk1")
        self.toggle_button = tk.Button(self.head_frame, text = "M", background="#D8D8BF", foreground="cornsilk1", font=('Bold', 14), command=self.toggle_menu)
        self.toggle_button.pack(side=tk.LEFT)
        self.head_frame.pack(side=tk.TOP, fill=tk.X)
        self.head_frame.pack_propagate(False)
        self.head_frame.configure(height=20)  

        
        # Welcome Label
        self.Label1 = tk.Label(self.head_frame)
        self.Label1.place(relx=0.433, rely=0.030, height=21, width=99)
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#EEEED2")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Contact Book''')


        # Name label
        self.Label2 = tk.Label(self.top)
        self.Label2.place(relx=0.1, rely=0.2, height=21, width=70)
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#FFFFF5")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Name:''')

        # Phone Label
        self.Label2_1 = tk.Label(self.top)
        self.Label2_1.place(relx=0.1, rely=0.289, height=11, width=54)
        self.Label2_1.configure(activebackground="#f9f9f9")
        self.Label2_1.configure(activeforeground="black")
        self.Label2_1.configure(anchor='w')
        self.Label2_1.configure(background="#FFFFF5")
        self.Label2_1.configure(compound='left')
        self.Label2_1.configure(disabledforeground="#a3a3a3")
        self.Label2_1.configure(foreground="#000000")
        self.Label2_1.configure(highlightbackground="#FFFFF5")
        self.Label2_1.configure(highlightcolor="black")
        self.Label2_1.configure(text='''Phone:''')

        # Entry Field for Name
        self.EntryName = tk.Entry(self.top)
        self.EntryName.bind("<Return>", lambda event: self.add_contact())
        self.EntryName.place(relx=0.217, rely=0.2, height=20, relwidth=0.223)
        self.EntryName.configure(background="white")
        self.EntryName.configure(disabledforeground="#a3a3a3")
        self.EntryName.configure(font="TkFixedFont")
        self.EntryName.configure(foreground="#000000")
        self.EntryName.configure(insertbackground="black")

        # Entry Field for Phone
        self.EntryPhone = tk.Entry(self.top)
        self.EntryPhone.bind("<Return>", lambda event: self.add_contact())
        self.EntryPhone.place(relx=0.217, rely=0.289, height=20, relwidth=0.223)
        self.EntryPhone.configure(background="white")
        self.EntryPhone.configure(disabledforeground="#a3a3a3")
        self.EntryPhone.configure(font="TkFixedFont")
        self.EntryPhone.configure(foreground="#000000")
        self.EntryPhone.configure(highlightbackground="#FFFFF5")
        self.EntryPhone.configure(highlightcolor="black")
        self.EntryPhone.configure(insertbackground="black")
        self.EntryPhone.configure(selectbackground="blue")
        self.EntryPhone.configure(selectforeground="white")

        # ListBox to show contact list
        self.contacts_listbox = tk.Listbox(self.top)
        self.contacts_listbox.bind("<Double-Button-1>", self.edit_selected_contact)
        self.contacts_listbox.place(relx=0.6, rely=0.178, relheight=0.76
                                    , relwidth=0.36)
        self.contacts_listbox.configure(background="white")
        self.contacts_listbox.configure(disabledforeground="#a3a3a3")   
        self.contacts_listbox.configure(font="TkFixedFont")
        self.contacts_listbox.configure(foreground="#000000")


        # Button to add contacts
        self.ButtonAdd = tk.Button(self.top, command=self.add_contact)
        self.ButtonAdd.place(relx=0.233, rely=0.378, height=34, width=107)
        self.ButtonAdd.configure(activebackground="#ececec")
        self.ButtonAdd.configure(activeforeground="#000000")
        self.ButtonAdd.configure(background="#FFFFF5")
        self.ButtonAdd.configure(compound='left')
        self.ButtonAdd.configure(disabledforeground="#a3a3a3")
        self.ButtonAdd.configure(foreground="#000000")
        self.ButtonAdd.configure(highlightbackground="#FFFFF5")
        self.ButtonAdd.configure(highlightcolor="black")
        self.ButtonAdd.configure(pady="0")
        self.ButtonAdd.configure(text='''Add Contact''')

        # Button to delete contacts
        self.ButtonDeleteContact = tk.Button(self.top, command=self.delete_contact)
        self.ButtonDeleteContact.place(relx=0.233, rely=0.867, height=34
                                       , width=87)
        self.ButtonDeleteContact.configure(activebackground="#ececec")
        self.ButtonDeleteContact.configure(activeforeground="#000000")
        self.ButtonDeleteContact.configure(background="#FFFFF5")
        self.ButtonDeleteContact.configure(compound='left')
        self.ButtonDeleteContact.configure(disabledforeground="#a3a3a3")
        self.ButtonDeleteContact.configure(foreground="#000000")
        self.ButtonDeleteContact.configure(highlightbackground="#FFFFF5")
        self.ButtonDeleteContact.configure(highlightcolor="black")
        self.ButtonDeleteContact.configure(pady="0")
        self.ButtonDeleteContact.configure(text='''Delete Contact''')

        # Field for search name
        self.EntrySearch = tk.Entry(self.top)
        self.EntrySearch.place(relx=0.61, rely=0.120, height=20, relwidth=0.223)
        self.EntrySearch.bind("<Return>", lambda event: self.search_contacts())
        self.EntrySearch.bind("<BackSpace>", lambda event: self.load_contacts())
        self.EntrySearch.configure(background="white")
        self.EntrySearch.configure(disabledforeground="#a3a3a3")
        self.EntrySearch.configure(font="TkFixedFont")
        self.EntrySearch.configure(foreground="#000000")
        self.EntrySearch.configure(highlightbackground="#FFFFF5")
        self.EntrySearch.configure(highlightcolor="black")
        self.EntrySearch.configure(insertbackground="black")
        self.EntrySearch.configure(selectbackground="blue")
        self.EntrySearch.configure(selectforeground="white")

        #Button to return to Contacts Home
        home_button = PhotoImage(file="icon\home_16x16.png")
        
        self.HomeButton = tk.Button(self.top, command=self.load_contacts)
        self.HomeButton.place(relx=0.58, rely=0.125, height=20, width=20)
        self.HomeButton.configure(activebackground="#ececec")
        self.HomeButton.configure(activeforeground="#000000")
        self.HomeButton.configure(background="#FFFFF5")
        self.HomeButton.configure(compound='left')
        self.HomeButton.configure(disabledforeground="#a3a3a3")
        self.HomeButton.configure(foreground="#000000")
        self.HomeButton.configure(highlightbackground="#FFFFF5")
        self.HomeButton.configure(highlightcolor="black")
        self.HomeButton.configure(pady="0")
        self.HomeButton.configure(text='''H''')

        #Button for txt contacts backup
        self.backup_button = tk.Button(self.top, text="Backup Contacts", command=self.backup_contacts)
        self.backup_button.place(x=650, y=425, height=20)

        # Button to search contacts
        self.ButtonSearch = tk.Button(self.top, command=self.search_contacts)
        self.ButtonSearch.place(relx=0.84, rely=0.125, height=18, width=80)
        self.ButtonSearch.configure(activebackground="#ececec")
        self.ButtonSearch.configure(activeforeground="#000000")
        self.ButtonSearch.configure(background="#FFFFF5")
        self.ButtonSearch.configure(compound='left')
        self.ButtonSearch.configure(disabledforeground="#a3a3a3")
        self.ButtonSearch.configure(foreground="#000000")
        self.ButtonSearch.configure(highlightbackground="#FFFFF5")
        self.ButtonSearch.configure(highlightcolor="black")
        self.ButtonSearch.configure(pady="0")
        self.ButtonSearch.configure(text='''Search''')

        #Label for Time
        self.timeLabel = tk.Label(self.top)
        self.timeLabel.place(relx=0.04, rely=0, height=20, width=94)
        self.timeLabel.configure(anchor='w')
        self.timeLabel.configure(background="#EEEED2")
        self.timeLabel.configure(compound='left')
        self.timeLabel.configure(disabledforeground="#a3a3a3")
        self.timeLabel.configure(foreground="#000000")
        self.timeLabel.configure(text='''Label''')

        self.load_contacts()

        #Author Page

    def toggle_menu(self):
        """
        Create a toggle menu bar.

        This function creates a toggle menu bar on the left side of the root window. It includes several buttons for importing and exporting contacts in different formats. The toggle menu can be collapsed by clicking the toggle button.

        Note:
            This function is a method of a class and assumes the existence of a root window and a toggle button in the GUI.

        """
            
        def collapse_toggle_menu():
            """
            Collapse the toggle menu.

            This nested function is called when the toggle button is clicked. It destroys the toggle menu frame, changes the toggle button text to 'M', and updates its command to call `self.toggle_menu` again.

            """
            toggle_menu.destroy()
            self.toggle_button.config(text='M')
            self.toggle_button.config(command=self.toggle_menu)
        
        toggle_menu = tk.Frame(root, bg="#8B8B69", highlightthickness=0.5, highlightcolor="black", highlightbackground="#CDCD9B")
        window_height = root.winfo_height()
        toggle_menu.place(x=0,y=20, height=window_height, width=200)
        self.toggle_button.config(text='X')
        self.toggle_button.config(command=collapse_toggle_menu) 


        #Button to load contacts(from JSON)
        ButtonLoadJSONContact = tk.Button(toggle_menu, foreground="lavenderblush1", command=self.import_contacts)
        ButtonLoadJSONContact.configure(background="#8B8B69")
        ButtonLoadJSONContact.configure(font=('BOLD',20))
        ButtonLoadJSONContact.configure(bd=0, bg='#8B8B69', activebackground='beige', highlightbackground='blanchedalmond')
        ButtonLoadJSONContact.configure(text='''Import JSON''')
        ButtonLoadJSONContact.place(x=12,y=20)

        #Button to load contacts(from CSV)
        ButtonLoadCSVContact = tk.Button(toggle_menu, foreground="lavenderblush1", command=self.import_contacts_from_csv)
        ButtonLoadCSVContact.configure(background="#8B8B69")
        ButtonLoadCSVContact.configure(font=('BOLD',20))
        ButtonLoadCSVContact.configure(bd=0, bg='#8B8B69', activebackground='beige', highlightbackground='blanchedalmond')
        ButtonLoadCSVContact.configure(text='''Import CSV''')
        ButtonLoadCSVContact.place(x=12,y=80)

        # Button to export contacts(json)
        ButtonSaveContactJSON = tk.Button(toggle_menu,  foreground="lavenderblush1", command=self.export_contacts)
        ButtonSaveContactJSON.configure(background="#8B8B69")
        ButtonSaveContactJSON.configure(font=('BOLD',20))
        ButtonSaveContactJSON.configure(bd=0, bg='#8B8B69', activebackground='beige', highlightbackground='blanchedalmond')
        ButtonSaveContactJSON.configure(text='''Export JSON''')
        ButtonSaveContactJSON.place(x=12,y=140)
        
        # Button to export contacts(csv)
        ButtonSaveContactCSV = tk.Button(toggle_menu, foreground="lavenderblush1", command=self.export_contacts_to_csv)
        ButtonSaveContactCSV.configure(background="#8B8B69")
        ButtonSaveContactCSV.configure(font=('BOLD',20))
        ButtonSaveContactCSV.configure(bd=0, bg='#8B8B69', activebackground='beige', highlightbackground='blanchedalmond')
        ButtonSaveContactCSV.configure(text='''Export CSV''')
        ButtonSaveContactCSV.place(x=12,y=200)
        

    def edit_selected_contact(self, event):
        """
        Edit the selected contact.

        This function is triggered when an event (e.g., double-clicking) occurs on the contacts_listbox. It retrieves the index of the selected contact, creates an EditContactWindow instance to edit the contact, and waits for the editing window to close.

        Args:
            event (tkinter.Event): The event triggered by the user.

        """
        selected_index = self.contacts_listbox.curselection()

        if selected_index:
            contact = self.contacts[selected_index[0]]
            edit_window = EditContactWindow(self, contact)
            edit_window.mainloop()

    def update_contact(self, contact):
        """
        Update the contact in the GUI.

        This function updates the contact details in the contacts listbox and the internal contacts list. It retrieves the index of the selected contact, replaces the corresponding entry in the listbox, and updates the contact in the contacts list.

        Args:
            contact (Contact): The updated contact object.

        """
        index = self.contacts_listbox.curselection()[0]

        # Update the contact in the listbox
        self.contacts_listbox.delete(index)
        self.contacts_listbox.insert(index, f"{contact.name} - {contact.phone_number}")

        # Update the contact in the contacts list
        self.contacts[index] = contact


    def load_contacts(self):
        """
        Load contacts from the database and populate the contacts listbox.

        This method clears the contacts listbox and the contacts list,
        then retrieves the contacts from the database table and adds them
        to the contacts listbox and the contacts list.

        Note:
            The method assumes that the database connection and cursor are already set up.

        """
        self.contacts_listbox.delete(0, tk.END)
        self.contacts = []

        # Retrieve contacts from the database
        self.cursor.execute("SELECT * FROM contacts")
        rows = self.cursor.fetchall()

        for row in rows:
            name, phone = row
            c = Contact(name, phone)
            self.contacts.append(c)
            self.contacts_listbox.insert(tk.END, f"{name}: {phone}")

    def add_contact(self):
        """
        Add a new contact to the contacts list and database.

        This method retrieves the name and phone number entered by the user from
        the Entry widgets. It validates the phone number to ensure it is a valid
        Poland phone number. If the name and phone number are provided and the phone
        number is valid, a new Contact object is created, added to the contacts list,
        and inserted into the database. The contact's name and phone number are also
        added to the contacts listbox. If the phone number is not valid or the name
        and phone number are not provided, appropriate error messages are displayed.

        Note:
            The method assumes that the database connection, cursor, EntryName, EntryPhone,
            contacts_listbox, and contacts list are already set up.

        """
        name = self.EntryName.get()
        phone = self.EntryPhone.get()

        if name and phone:
            if self.validate_poland_number(phone):
                c = Contact(name, phone)
                self.contacts.append(c)
                self.contacts_listbox.insert(tk.END, f"{name}: {phone}")

                # Insert the contact into the database
                self.cursor.execute(
                    "INSERT INTO contacts (name, phone_number) VALUES (?, ?)",
                    (name, phone)
                )
                self.connection.commit()

                self.EntryName.delete(0, tk.END)
                self.EntryPhone.delete(0, tk.END)
            else:
                messagebox.showwarning("Error", "Invalid Poland phone number.")
        else:
            messagebox.showwarning("Error", "Please enter name and phone number.")

    def validate_poland_number(self, phone):
        '''
        Validate a phone number for Poland.

        This method takes a phone number as input and validates it against the pattern for Poland numbers.
        The pattern allows the following formats:
        - 9-digit number: e.g., 123456789
        - 2-digit-3-digit-2-digit-2-digit format: e.g., 12-345-67-89
        - 3-digit-3-digit-3-digit format: e.g., 123-456-789
        - The phone number may have an optional prefix of '+48'.

        Args:
            phone (str): The phone number to validate.

        Returns:
            bool: True if the phone number is valid for Poland, False otherwise.
        '''
        pattern = r"^(?:\+?48)?(?:\d{9}|\d{2}-\d{3}-\d{2}-\d{2}|\d{3}-\d{3}-\d{3})$"
        # Validate the phone number against the pattern
        return re.match(pattern, phone) is not None

    def delete_contact(self):
        """
        Delete a selected contact from the contacts list and database.

        This method retrieves the index of the selected contact from the contacts_listbox.
        If a contact is selected, it is removed from the contacts list and the contacts_listbox.
        The corresponding entry is also deleted from the database. If no contact is selected,
        an error message is displayed.

        Note:
            The method assumes that the database connection, cursor, contacts_listbox, and
            contacts list are already set up.

        """
        selected_index = self.contacts_listbox.curselection()

        if selected_index:
            selected_contact = self.contacts[selected_index[0]]
            self.contacts.pop(selected_index[0])
            self.contacts_listbox.delete(selected_index)

            # Delete the contact from the database
            self.cursor.execute(
                "DELETE FROM contacts WHERE name=? AND phone_number=?",
                (selected_contact.name, selected_contact.phone_number)
            )
            self.connection.commit()

            messagebox.showinfo("Success", "Contact deleted.")
        else:
            messagebox.showwarning("Error", "No contact selected.")

    
    def backup_contacts(self):
        """
        Backup the contacts to a text file.

        This method prompts the user to select the location and filename for the backup text file.
        Each contact is written as a separate line in the format "Name: Phone Number".
        If the user cancels the file selection, the method returns without saving the file.
        If the file path is provided, the contact data is written to the text file.
        If any error occurs during the backup process, an error message is displayed.

        Note:
            The method assumes that the contacts list is already populated with contact information.

        """
        # Prompt the user to select the location and filename for the backup text file
        filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])

        if not filename:
            # User canceled the file selection
            return

        try:
            # Open the text file in write mode
            with open(filename, "w") as file:
                for contact in self.contacts:
                    name = contact.name
                    phone_number = contact.phone_number
                    file.write(f"{name}: {phone_number}\n")

            messagebox.showinfo("Success", "Contacts backed up successfully!")
        except Exception as e:
            messagebox.showerror("Backup error occured", str(e))

    

    def export_contacts_to_csv(self):
        """
        Export the contacts as a CSV file.

        This method creates a list of contact dictionaries from the contacts list.
        Each contact dictionary contains the name and phone number of a contact.
        The user is prompted to select the location and filename for the CSV file.
        If the user cancels the file selection, the method returns without saving the file.
        If the file path is provided, the contact data is written to the CSV file.
        If any error occurs during the export process, an error message is displayed.

        Note:
            The method assumes that the contacts list is already populated with contact information.

        """
        # Create a list of contact dictionaries
        contacts_data = []
        for contact in self.contacts:
            contact_data = {
                "name": contact.name,
                "phone_number": contact.phone_number
            }
            contacts_data.append(contact_data)

        # Prompt the user to select the location and filename for the CSV file
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])

        if not file_path:
            # User canceled the file selection
            return

        try:
            # Write the contact data to the CSV file
            with open(file_path, "w", newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Phone Number"])  # Writing header row
                for contact_data in contacts_data:
                    name = contact_data["name"]
                    phone_number = contact_data["phone_number"]
                    writer.writerow([name, phone_number])

            messagebox.showinfo("Success", "Contacts saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))


    def export_contacts(self):
        """
        Export the contacts as a JSON file.

        This method creates a list of contact dictionaries from the contacts list.
        Each contact dictionary contains the name and phone number of a contact.
        The user is prompted to select the location and filename for the JSON file.
        If the user cancels the file selection, the method returns without saving the file.
        If the file path is provided, the contact data is written to the JSON file.
        If any error occurs during the export process, an error message is displayed.

        Note:
            The method assumes that the contacts list is already populated with contact information.

        """
        # Create a list of contact dictionaries
        contacts_data = []
        for contact in self.contacts:
            contact_data = {
                "name": contact.name,
                "phone_number": contact.phone_number
            }
            contacts_data.append(contact_data)

        # Prompt the user to select the location and filename for the JSON file
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])

        if not file_path:
            # User canceled the file selection
            return

        try:
            # Write the contact data to the JSON file
            with open(file_path, "w") as file:
                json.dump(contacts_data, file, indent=4)

            messagebox.showinfo("Success", "Contacts saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))


    def search_contacts(self):
        """
        Search for contacts based on a query.

        This method retrieves the search query from the EntrySearch widget.
        It performs a case-insensitive search in the SQLite database for contacts matching the query in either name or phone number.
        If contacts are found, their names and phone numbers are displayed in the contacts_listbox.
        If no contacts match the query, a message box is shown with the title "No Results" and the message "No contacts found matching the search query".
        If no query is provided, the method reloads all the contacts using the load_contacts method and displays an error message.

        Note:
            - The method assumes that the SQLite database named "contacts.db" is already created and populated with contact information.
            - The method assumes the presence of the EntrySearch and contacts_listbox widgets.

        """
        query = self.EntrySearch.get().lower()
        self.contacts_listbox.delete(0, tk.END)

        if query:
            # Open a connection to the SQLite database
            connection = sqlite3.connect("contacts.db")
            cursor = connection.cursor()

            # Perform a case-insensitive search for contacts matching the query in name or phone number
            cursor.execute("SELECT * FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(phone_number) LIKE ?", ('%' + query + '%', '%' + query + '%'))
            results = cursor.fetchall()

            if results:
                for result in results:
                    name = result[0]
                    phone_number = result[1]
                    self.contacts_listbox.insert(tk.END, f"{name}: {phone_number}")
            else:
                messagebox.showinfo("No Results", "No contacts found matching the search query.")

            connection.close()
            self.EntrySearch.delete(0, tk.END)
        else:
            self.load_contacts()
            messagebox.showwarning("Error", "Please enter a search query.")



    def import_contacts_from_csv(self):
        """
        Import contacts from a CSV file.

        This method prompts the user to select a CSV file containing contact information.
        If a file is selected, it reads the CSV data and inserts the contacts into the SQLite database.
        After importing the contacts, the method retrieves them from the database and updates the contacts list and contacts_listbox.
        If the CSV file format is invalid, an error message is displayed.

        Note:
            - The method assumes that the SQLite database named "contacts.db" is already created.
            - The method assumes the presence of the contacts_listbox widget.
        """
        # Prompt the user to select a CSV file
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

        if not file_path:
            # User canceled the file selection
            return

        try:
            # Read the CSV data from the file
            with open(file_path, "r") as file:
                reader = csv.reader(file)
                contacts_data = list(reader)

            # Open a connection to the SQLite database
            connection = sqlite3.connect("contacts.db")
            cursor = connection.cursor()

            # Clear the existing contacts table
            cursor.execute("DROP TABLE IF EXISTS contacts")
            cursor.execute("CREATE TABLE contacts (name TEXT, phone_number TEXT)")

            # Insert the contacts from the CSV data into the database
            for contact_data in contacts_data:
                name = contact_data[0]
                phone_number = contact_data[1]
                if name and phone_number:
                    cursor.execute("INSERT INTO contacts VALUES (?, ?)", (name, phone_number))

            connection.commit()
            connection.close()
            self.contacts_listbox.delete(0, tk.END)
            self.contacts = []

            # Retrieve contacts from the database
            self.cursor.execute("SELECT * FROM contacts")
            rows = self.cursor.fetchall()

            for row in rows:
                name, phone = row
                c = Contact(name, phone)
                self.contacts.append(c)
                self.contacts_listbox.insert(tk.END, f"{name}: {phone}")

            messagebox.showinfo("Success", "Contacts imported successfully!")
        except csv.Error:
            messagebox.showerror("Error", "Invalid CSV file format!")


    def import_contacts(self):
        """
        Import contacts from a JSON file.

        This method prompts the user to select a JSON file containing contact information.
        If a file is selected, it reads the JSON data and inserts the contacts into the SQLite database.
        After importing the contacts, the method retrieves them from the database and updates the contacts list and contacts_listbox.
        If the JSON file format is invalid, an error message is displayed.

        Note:
            - The method assumes that the SQLite database named "contacts.db" is already created.
            - The method assumes the presence of the contacts_listbox widget.
        """
        # Prompt the user to select a JSON file
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])

        if not file_path:
            # User canceled the file selection
            return

        try:
            # Read the JSON data from the file
            with open(file_path, "r") as file:
                contacts_data = json.load(file)

            # Open a connection to the SQLite database
            connection = sqlite3.connect("contacts.db")
            cursor = connection.cursor()

            # Clear the existing contacts table
            cursor.execute("DROP TABLE IF EXISTS contacts")
            cursor.execute("CREATE TABLE contacts (name TEXT, phone_number TEXT)")

            # Insert the contacts from the JSON data into the database
            for contact_data in contacts_data:
                name = contact_data.get("name")
                phone_number = contact_data.get("phone_number")
                if name and phone_number:
                    cursor.execute("INSERT INTO contacts VALUES (?, ?)", (name, phone_number))

            connection.commit()
            connection.close()
            self.contacts_listbox.delete(0, tk.END)
            self.contacts = []

            # Retrieve contacts from the database
            self.cursor.execute("SELECT * FROM contacts")
            rows = self.cursor.fetchall()

            for row in rows:
                name, phone = row
                c = Contact(name, phone)
                self.contacts.append(c)
                self.contacts_listbox.insert(tk.END, f"{name}: {phone}")

            messagebox.showinfo("Success", "Contacts imported successfully!")
        except json.JSONDecodeError:
            messagebox.showerror("Error", "Invalid JSON file format!")

    def update_time(self):
        '''
        Update the time label with the current time.

        This method retrieves the current time using the `datetime` module and formats it as "Time: HH:MM:SS".
        The formatted time is then set as the text for the `timeLabel` widget.
        The method schedules itself to be called again after 1000 milliseconds (1 second) using the `after` method.

        Note: Make sure to call this method once to start the continuous time update.

        '''
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.timeLabel.configure(text="Time: " + current_time)
        self.timeLabel.after(1000, self.update_time)


def start_up():
    """Initialize the Tkinter GUI application.

    This function creates a root window, sets the protocol for window close event,
    creates a Toplevel1 object, and starts the main event loop.

    The root window is stored in the global variable `root`, and the Toplevel1 object
    is stored in the global variables `_top1` and `_w1`.
    """
    global root
    root = tk.Tk()
    root.protocol('WM_DELETE_WINDOW', root.destroy)
    global _top1, _w1
    _top1 = root
    _w1 = Toplevel1(_top1)
    root.bind("<Control-n>", lambda event: _w1.add_contact())  # Bind Ctrl + N to add_contact() method
    root.bind("<Delete>", lambda event: _w1.delete_contact())  # Bind Delete key to delete_contact() method
    root.bind("<Control-s>", lambda event: _w1.export_contacts())  # Bind Ctrl + S to export_contacts() method
    root.bind("<Control-f>", lambda event: _w1.search_contacts())  # Bind Ctrl + F to search_contacts() method
    root.bind("<Control-i>", lambda event: _w1.import_contacts())  # Bind Ctrl + I to import_contacts() method
    root.bind("<Control-q>", lambda event: root.destroy())  # Bind Ctrl + Q to exit the application
    _w1.update_time()  # Call update_time() method to start updating the time display

    root.mainloop()


if __name__ == '__main__':
    start_up()
