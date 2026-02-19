#selectfile is the file being opened to be edited here.
def test_file(file_name):
    try:
        with open(file_name, 'r') as file:
            return True
    except FileNotFoundError:
        print("File not found. Please check the path and try again.")
        return False
def Update(file_name):
    from TimeHandling import get_timestamp
    import csv

    if not test_file(file_name):
        print ("File not found. Please check the path and try again.")
        return
    
    with open(file_name, 'r') as file:
        data = file.read()
        wordcount = len(data.split())
        timestamp = get_timestamp()
    
    with open('ACfile.csv', 'a', newline='') as base:
        writer = csv.DictWriter(base, fieldnames=['wordcount', 'timestamp'])
        writer.writerow({'wordcount': wordcount, 'timestamp': timestamp})
def addtofile(file_name):

    import csv

    with open(file_name, 'a', newline='') as base:
        if not test_file(file_name):
            print ("File not found. Please check the path and try again.")
            return
        writer = csv.writer(base)
        written = input("please type what you want to add to the file")
        writer.writerow([written])
        Update(file_name)

def removefromfile(file_name):
    import csv

    with open(file_name, 'r') as base:
        
        if not test_file(file_name):
            print ("File not found. Please check the path and try again.")
            return
        reader = csv.reader(base)
        rows = list(reader)
        if not rows:
            print("File is empty.")
            return
        print ("how many rows do you want to remove? (There are", len(rows), " in the file)")
        try:
            num = int(input("Enter number of lines to remove: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return
        for removal in range(num):
            if removal < len(rows):
                print("Removing row:", rows[removal])
                rows.pop(removal)
            else:
                print("No more rows to remove.")
                break

    with open(file_name, 'w', newline='') as base:
        if not test_file(file_name):
            print ("File not found. Please check the path and try again.")
            return
        writer = csv.writer(base)
        for i, row in enumerate(rows):
            if i >= num:
                writer.writerow(row)
        
    Update(file_name)
def viewfile(file_name):
    with open(file_name, 'r') as file:
        if not test_file(file_name):
            print ("File not found. Please check the path and try again.")
            return
        print(file.read())

