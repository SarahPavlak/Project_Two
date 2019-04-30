from dotenv import load_dotenv
import sendgrid
from sendgrid.helpers.mail import * 
import csv 
import os
import requests

#compiled emails 

#reading to see which apartment is selected
with open("apartment.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        apartment = (row['A'])
csvfile.close()
       
#sending the proper email if its ava-ballston
if apartment == "ava-ballston":
    applicable_apartments = []
    with open("ava_apartment.csv", 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            applicable_apartments.append(dict(row))
    csvfile.close()
else:
    pass

#sending the proper email if its both apartments
if apartment == 'ava-ballston,avalon-ballston-square':
    applicable_apartments = []
    with open("ava_avalon.csv", 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            applicable_apartments.append(dict(row))
    csvfile.close()
else:
    pass

#sending the right email if its avalon
if apartment == "avalon-ballston-square":
    applicable_apartments = []
    with open("avalon_apartment.csv", 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            applicable_apartments.append(dict(row))
            print("                              ")
    csvfile.close()
else:
    pass
    
breakpoint 

print("You will now receive an email to your inbox")

load_dotenv()

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY", "OOPS, please set env var called 'SENDGRID_API_KEY'")
MY_EMAIL_ADDRESS = os.environ.get("MY_EMAIL_ADDRESS", "OOPS, please set env var called 'MY_EMAIL_ADDRESS'")

# AUTHENTICATE

sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)

# COMPILE REQUEST PARAMETERS (PREPARE THE EMAIL)

from_email = Email(MY_EMAIL_ADDRESS)
to_email = Email(MY_EMAIL_ADDRESS)
subject = "Apartment Update!"
content = Content("text/plain", str(applicable_apartments)) #https://bytes.com/topic/python/answers/620147-how-execute-python-script-another-python-script)
mail = Mail(from_email, subject, to_email, content)

# ISSUE REQUEST (SEND EMAIL)

response = sg.client.mail.send.post(request_body=mail.get())

# PARSE RESPONSE

print(response.status_code)
print(response.body) 
print(response.headers)
