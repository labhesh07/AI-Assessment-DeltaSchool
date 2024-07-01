def display_menu():
    print("Phone Book Application")
    print("1. Add Contact")
    print("2. Search Contact By Name")
    print("3. Delete Contact")
    print("4. Exit")

def add_contact(phone_book):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    phone_book[name] = phone
    print(f"Contact {name} added.")

def search_contact(phone_book):
    name = input("Enter name to search: ")
    if name in phone_book:
        print(f"{name}: {phone_book[name]}")
    else:
        print("Contact not found.")

def delete_contact(phone_book):
    name = input("Enter name to delete: ")
    if name in phone_book:
        del phone_book[name]
        print(f"Contact {name} deleted.")
    else:
        print("Contact not found.")

def phone_book_app():
    phone_book = {}
    while True:
        display_menu()
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_contact(phone_book)
        elif choice == '2':
            search_contact(phone_book)
        elif choice == '3':
            delete_contact(phone_book)
        elif choice == '4':
            print("Exiting phone book application.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the phone book application
phone_book_app()



