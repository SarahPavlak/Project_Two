import csv 
import os

with open("apartment.csv", 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            apartment = (row['A'])

#Avalon Ballston-------------------------------------------------------------------------------------------------------
if apartment == 'avalon-ballston-square':  
    os.system('python scraping.py')
    os.system('python email_compiled.py')
        
#Ava Ballston---------------------------------------------------------------------------------------------------------
if apartment == 'ava-ballston':
    os.system('python scraping.py')
    os.system('python email_compiled.py')

#Ava and Avlaon------------------------------------------------------------------
if apartment == 'ava-ballston,avalon-ballston-square':
    os.system('python avalon_ballston_one_bed_one_bath.py')
    os.system('python ava_ballston_one_bed_one_bath.py')
    os.system('python email_compiled.py') 
else:
    pass


#makes the process independent of the user input part which is in freestyle so that I can run heroku 
