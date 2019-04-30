import csv 
import os

with open("csv_files/apartment.csv", 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            apartment = (row['A'])

with open("csv_files/notification.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        notification = (row['N'])
       

#Avalon Ballston-------------------------------------------------------------------------------------------------------
if apartment == 'avalon-ballston-square':  
    os.system('python scraping.py')

else:
    pass
        
#Ava Ballston---------------------------------------------------------------------------------------------------------
if apartment == 'ava-ballston':
    os.system('python scraping.py')

else:
    pass

#Ava and Avlaon------------------------------------------------------------------
if apartment == 'ava-ballston,avalon-ballston-square':
    os.system('python avalon_ballston_one_bed_one_bath.py')
    os.system('python ava_ballston_one_bed_one_bath.py')
    
else:
    pass

if notification == 'One time,Recurring' or 'One time':
    os.system('python email_compiled.py')
else:
    pass

#makes the process independent of the user input part which is in freestyle so that I can run heroku 
