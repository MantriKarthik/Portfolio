This program is a simple address book application that allows you to add and list contacts.

Programming Task and Specifications:
- Define and meaningfully use the Contact class to represent a contact in the address book.
- Use at least two meaningful functions besides the main function and the class methods.
- Input and output are done through files, with some user input and output to the screen if needed.
- Meaningfully use at least one list or one dictionary.
- The program should be well-documented with module documentation, function and class-level comments, and comments at appropriate places in the program.

Programming Design:
- The program defines a Contact class, representing a contact with a name and phone number.
- The add_contact function prompts the user to enter the contact's name and phone number, creates a Contact object, and appends the contact details to the "address_book.txt" file.
- The list_contacts function reads the contacts from the "address_book.txt" file, creates Contact objects, and displays the contacts' details on the screen.
- The main function handles the user's menu choices and calls the appropriate functions based on the input.

How to Run the Program:
1. Make sure you have Python installed on your system.
2. Download the Python script file (address_book.py) and the address book data file (address_book.txt) to the same directory.
3. Open a terminal or command prompt and navigate to the directory where the files are located.
4. Run the program by executing the following command: python address_book.py
5. Follow the on-screen prompts to add and list contacts in the address book.
6. The contacts will be stored in the "address_book.txt" file in the same directory.
