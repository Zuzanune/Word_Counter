#ZC 2nd Word Counter project
from FileHandling import Update, addtofile
file_name = input("Enter the exact path to your file: ")
Update(file_name)
while True:
    print("Do you want to add, remove, or view your file?")
    choice = input("Enter your choice (add/remove/view): ").strip().lower()
    if choice == "add":
        addtofile(file_name)
    elif choice == "remove":
        pass
    elif choice == "view":
        pass
    else:
        print("Invalid choice. Please try again.")
