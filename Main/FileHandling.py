
def test_file(file_name):
    try:
        with open(file_name, 'r') as file:
            return True
    except FileNotFoundError:
        print ("File not found. Please check the path and try again.")
        return False
def count_words(file_name):
    if not test_file(file_name):
        return None
    try:
        with open(file_name, 'r') as file:
            data = file.read()
    except FileNotFoundError:
        return None
    words = data.split(" ")
    return len(words)

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
    with open(file_name, 'a', newline='') as file:
        writer = csv.writer(file)
        with open(file_name, 'r') as base:
            reader = csv.reader(base)
            rows = list(reader)
            nums = -1
            #code to make sure the word count and timestamp ONLY EXIST ONCE AT THE END OF THE FILE!!!!!
            while True:
                if 'Word count:' in rows[nums] and 'Timestamp:' in rows[nums]:
                    rows.pop(nums)
                else:
                    nums -= 1
        written = input("please type what you want to add to the file.\n")
        writer.writerow([written])
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

