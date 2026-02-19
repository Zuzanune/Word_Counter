#ZC 2nd Word Counter project
from FileHandling import Update, addtofile, removefromfile, viewfile
file_name = input("Enter the exact path to your file: ")
Update(file_name)
while True:
    print("Do you want to add, remove, or view your file?")
    choice = input("Enter your choice (add/remove/view/quit): ").strip().lower()
    if choice == "add":
        addtofile(file_name)
    elif choice == "remove":
        removefromfile(file_name)
    elif choice == "view":
        viewfile(file_name)
    elif choice == "quit":
        break
    else:
        print("Invalid choice. Please try again.")
