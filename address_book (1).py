"""
This module demonstrates a simple address book program.
"""

class Contact:
    """
    Class representing a contact in the address book.
    """

    def __init__(self, name, phone):
        """
        Initialize a contact with a name and phone number.
        """
        self.name = name
        self.phone = phone

def add_contact():
    """
    Function to add a new contact to the address book.
    """
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")

    contact = Contact(name, phone)

    with open("address_book.txt", "a") as file:
        file.write(f"{contact.name},{contact.phone}\n")

    print("Contact added successfully.")

def list_contacts():
    """
    Function to list all contacts in the address book.
    """
    contacts = []

    with open("address_book.txt", "r") as file:
        for line in file:
            name, phone = line.strip().split(",")
            contact = Contact(name, phone)
            contacts.append(contact)

    if contacts:
        print("Address Book:")
        for contact in contacts:
            print(f"Name: {contact.name} \nPhone: {contact.phone}\n")
    else:
        print("Address book is empty.")

def main():
    """
    Main function to handle user input and menu options.
    """
    while True:
        print("Address Book Program")
        print("1. Add Contact")
        print("2. List Contacts")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            list_contacts()
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

main()
