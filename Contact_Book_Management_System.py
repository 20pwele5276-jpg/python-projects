# Contact Book Management System

# Function to add a contact
def add_contact():
    name = input("Enter contact name: ")
    number = input("Enter contact number: ")
    with open("contacts.txt", "a") as file:  # open file in append mode
        file.write(f"{name},{number}\n")
    print("Contact added successfully.\n")

# Function to view all contacts
def view_contacts():
    print("All Contacts:")
    try:
        with open("contacts.txt", "r") as file:
            lines = file.readlines()
            if not lines:
                print("No contacts found.\n")
                return
            for line in lines:
                name, number = line.strip().split(",")
                print(f"Name: {name}, Number: {number}")
        print()
    except FileNotFoundError:
        print("No contacts found.\n")

# Function to update a contact
def update_contact():
    target_name = input("Enter the name of the contact to update: ")
    try:
        with open("contacts.txt", "r") as file:
            lines = file.readlines()
        updated = False
        for i in range(len(lines)):
            name, number = lines[i].strip().split(",")
            if name.lower() == target_name.lower():
                new_name = input("Enter new name: ")
                new_number = input("Enter new number: ")
                lines[i] = f"{new_name},{new_number}\n"
                updated = True
                break
        if updated:
            with open("contacts.txt", "w") as file:
                file.writelines(lines)
            print("Contact updated successfully.\n")
        else:
            print("Contact not found.\n")
    except FileNotFoundError:
        print("No contacts found.\n")

# Function to delete a contact
def delete_contact():
    target_name = input("Enter the name of the contact to delete: ")
    try:
        with open("contacts.txt", "r") as file:
            lines = file.readlines()
        new_lines = []
        deleted = False
        for line in lines:
            name, number = line.strip().split(",")
            if name.lower() != target_name.lower():
                new_lines.append(line)
            else:
                deleted = True
        if deleted:
            with open("contacts.txt", "w") as file:
                file.writelines(new_lines)
            print("Contact deleted successfully.\n")
        else:
            print("Contact not found.\n")
    except FileNotFoundError:
        print("No contacts found.\n")

# Main program loop
def main():
    while True:
        print("=== Contact Book Menu ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

# Run the program
main()