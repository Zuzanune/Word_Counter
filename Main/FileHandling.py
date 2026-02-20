def test_file(file_name):
    try:
        with open(file_name, 'r') as file:
            return True
    except FileNotFoundError:
        print ("File not found. Please check the path and try again.")
        return False
def count_words(file_name):
    import csv
    with open(file_name, 'r') as file:
        if not test_file(file_name):
            return None
        reader = csv.reader(file)
        text_parts = []
        for row in reader:
            # Skip rows that contain word count or timestamp stamps
            if not any('Word count:' in cell or 'Timestamp:' in cell for cell in row):
                text_parts.extend(row)
        # Join all cells and split into words
        text = ' '.join(text_parts)
        words = text.split()
        return len(words)

def update_stamp(file_name):
    import csv
    if not test_file(file_name):
        return
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
    rows = [row for row in rows if not any('Word count:' in cell or 'Timestamp:' in cell for cell in row)]
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        for row in rows:
            writer.writerow(row)
    stamp = Update(file_name)
    with open(file_name, 'a', newline='') as f:
        stamp_writer = csv.DictWriter(f, fieldnames=['wordcount', 'timestamp'])
        stamp_writer.writerow(stamp)

def info(file_name, yes=False):
    update_stamp(file_name)
    count = count_words(file_name)
    if not yes:
        if count == 0:
            print("File is empty")
        else:
            print ("The file has", count, "words in it.")
            print ("The Path to the file is:", file_name)
    else:
        return count
    
def Update(file_name):
    from TimeHandling import get_timestamp
    from FileHandling import info


    if not test_file(file_name):
        return None
    
    wordcount = count_words(file_name)
    timestamp = get_timestamp()
    
    with open(file_name, 'a', newline='') as base:
        stamp = {'wordcount': "Word count:  " + str(info(file_name, yes=True)), 'timestamp': "Timestamp:  " + str(timestamp)}
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

