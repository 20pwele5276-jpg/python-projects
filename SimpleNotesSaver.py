# Simple Notes Saver
def add_note():
    note = input("Enter your note: ")
    with open("notes.txt", "a") as file:  # append mode
        file.write(note + "\n")
    print("Note saved successfully.\n")

def view_notes():
    print("\nYour Notes:")
    try:
        with open("notes.txt", "r") as file:
            lines = file.readlines()
            if not lines:
                print("No notes found.\n")
                return
            for i, line in enumerate(lines, start=1):
                print(f"{i}. {line.strip()}")
        print()
    except FileNotFoundError:
        print("No notes found.\n")

def main():
    while True:
        print("=== Notes Saver Menu ===")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            print("Exiting Notes Saver. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

main()