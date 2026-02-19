#selectfile is the file being opened to be edited here.
def Update(file_name):
    from TimeHandling import get_timestamp
    import csv

    with open('P:\Carter, Zane\Word_Counter\ACfile.csv', 'r') as base:
        writer = csv.DictWriter(base, fieldnames=['wordcount', 'timestamp'])

    with open(file_name, 'r') as file:
        data = file.read()
        wordcount = len(data.split())
        timestamp = get_timestamp()
        writer.writerow({'wordcount': wordcount, 'timestamp': timestamp})
def addtofile(file_name):

    import csv

    with open(file_name, 'a', newline='') as base:
        writer = csv.writer(base)
        written = input("please type what you want to add to the file")
        writer.writerow(written)

def removefromfile(file_name):
    import csv

    with open(file_name, 'r') as base:
        reader = csv.reader(base)
        rows = list(reader)

    with open(file_name, 'w', newline='') as base:
        writer = csv.writer(base)
        for row in rows:
            if row != "":
                writer.writerow(row)
