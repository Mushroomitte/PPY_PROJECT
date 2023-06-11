# PPY PROJECT
Project for PPY subject in PJATK. The following text is only a part of documentation, 
if you want to familiarize yourself with full documentation, please open "Project Documentation.docx"
	


# Purpose
The purpose of this program is to provide a graphical user interface (GUI) for managing contacts in a contact book. 
The program allows users to add, edit, delete, import, and export contacts in various formats such as JSON and CSV. 
It uses the Tkinter library for creating the GUI and SQLite for storing the contacts in a database.

# Functionality
The program provides the following functionality:
1.	Add Contact: Allows users to add a new contact by entering their name and phone number. The program validates the phone number to ensure it is a valid Poland phone number.
2.	Edit Contact: Allows users to edit an existing contact by selecting it from the contacts list and modifying the name and phone number.
3.	Delete Contact: Allows users to delete a contact by selecting it from the contacts list.
4.	Import Contacts: Allows users to import contacts from a JSON file or a CSV file. The program reads the file, parses the contacts data, and adds them to the contact book.
5.	Export Contacts: Allows users to export contacts from the contact book to a JSON file or a CSV file. The program retrieves the contacts data, converts it to the desired format, and saves it to the specified file.
6.	Toggle Menu: Provides a toggle menu bar on the left side of the window, allowing users to easily access import and export functionality.
7.	Clock: Provides functionality of a clock inside application
8.	Hotkeys Functionality:
Hotkeys are keyboard shortcuts that allow users to perform actions or navigate through a program quickly and efficiently without using the mouse. They provide a convenient way to access frequently used features or commands. In the context of a contact management system, hotkeys can offer users a faster and more streamlined experience. Here are some examples of hotkeys that could be implemented:
  1.	Ctrl + N: Create a new contact.
  2.	Ctrl + E: Edit the selected contact.
  3.	Ctrl + D: Delete the selected contact.
  4.	Ctrl + S: Save changes to the contact book.
  5.	Ctrl + F: Open the search bar to quickly find a contact.
  6.	Ctrl + H: Return to the home screen or contact list	.
  7.	Using search bar press „Return” to search and “Backspace” to return home
  By utilizing hotkeys, users can perform common tasks with a few keystrokes, reducing the need to navigate through menus or use the mouse. This can greatly improve productivity and efficiency when working with a contact management system.
  9.	Search Bar: A search bar is a text input field typically placed at the top of the user interface, allowing users to search for specific information within a system or application. In the context of a contact management system, a search bar enables users to quickly locate a contact based on various search criteria.

  10.	Home Button: It serves as a visual anchor and provides users with a quick way to return to the main screen or starting point of an application

# Instructions
To run the program, follow these steps:
  1.	Install the required dependencies:
  o	Tkinter (usually comes pre-installed with Python)
  o	SQLite3 (usually comes pre-installed with Python)
  2.	Save the program code in a file with a .py extension, e.g., contactBookApp.py.
  3.	Open a terminal or command prompt and navigate to the directory where the program file is saved.
  4.	Run the program using the command: python contactBookApp.py. Also you should run: DataBaseCreate.py
  o	Note: Make sure you have Python installed and added to the system's PATH variable.
  5.	The program window will appear, displaying the contact book.
  6.	You can perform various operations such as adding, editing, deleting, importing, and exporting contacts using the provided buttons and menus.

# Dependencies
The program requires the following dependencies:
  •	Python 3.x (usually comes pre-installed on most systems)
  •	Tkinter library (usually comes pre-installed with Python)
  •	SQLite3 library (usually comes pre-installed with Python)

