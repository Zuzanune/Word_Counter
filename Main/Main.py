#ZC 2nd Word Counter project
from FileHandling import Update, addtofile, removefromfile, viewfile, info, test_file
while True:
    file_name = input("Enter the exact path to your file: ")
    if not test_file(file_name):
        continue
    break
while 'True':
    print("Do you want to add, remove, view, or view info about your file?")
    choice = input("Enter your choice (add/remove/view/info/quit): ").strip().lower()
    if choice == "add":
        addtofile(file_name)
    elif choice == "remove":
        removefromfile(file_name)
    elif choice == "view":
        viewfile(file_name)
    elif choice == "info":
        info(file_name)
    elif choice == "quit":
        break
    else:
        print("Invalid choice. Please try again.")