def test_file(file_name):
    try:
        with open(file_name, 'r') as file:
            return True
    except FileNotFoundError:
        print ("File not found. Please check the path and try again.")
        return False
    #this is not completely accurate in short messages, but works well in long ones.
def count_words(file_name):
    if not test_file(file_name):
        return None
    try:
        with open(file_name, 'r') as file:
            data = file.read()
    except FileNotFoundError:
        return None
    words = data.split(" ")
    return len(words) + 1

def info(file_name):
    count = count_words(file_name)
    if count is None:
        print("File is empty")
    else:
        print ("The file has", count, "words in it.")
    print ("The Path to the file is:", file_name)
    
def Update(file_name):
    from TimeHandling import get_timestamp
    import csv

    if not test_file(file_name):
        return None
    
    wordcount = count_words(file_name)
    timestamp = get_timestamp()
    
    with open(file_name, 'a', newline='') as base:
        stamp = {'wordcount': "Word count:  " + str(wordcount), 'timestamp': "Timestamp:  " + str(timestamp)}
    return stamp
def addtofile(file_name):

    import csv
    if not test_file(file_name):
        return
    #YES! code for removing timestamp.
    with open(file_name, 'r') as base:
        reader = csv.reader(base)
        rows = list(reader)
    rows = [row for row in rows if not any('Word count:' in cell or 'Timestamp:' in cell for cell in row)]
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            writer.writerow(row)
        written = input("please type what you want to add to the file. add *** for line split.\n")
        to_write = list(written.split("***"))
        for line in to_write:
            writer.writerow([line])
        # code for adding new timestamp!
        stamp = Update(file_name)
        stamp_writer = csv.DictWriter(file, fieldnames=['wordcount', 'timestamp'])
        stamp_writer.writerow(stamp)

def removefromfile(file_name):
    import csv
    with open(file_name, 'r') as base:
        if not test_file(file_name):
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
            return
        writer = csv.writer(base)
        for i, row in enumerate(rows):
            if i >= num:
                writer.writerow(row)
        
    Update(file_name)
def viewfile(file_name):
    with open(file_name, 'r') as file:
        if not test_file(file_name):
            return
        text = file.read()
        if not text:
            print("File is empty.")
            return
        print(text)

