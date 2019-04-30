import csv 

def enlarge(i):
    with open("apartment.csv", 'r') as csvfile:
        reader = csv.DictReader(csvfile)
    for row in reader:
        apartment = (row['A'])
        return apartment

def notification(i):
    with open("notification.csv", 'r') as csvfile:
        reader = csv.DictReader(csvfile)
    for row in reader:
        notification = (row['N'])
        return notification
