import tkinter as tk
from tkinter import *
import datetime
import tkinter
from PIL import Image, ImageTk
import os
import pprint
from dotenv import load_dotenv
import sendgrid
from sendgrid.helpers.mail import * 


print("To start, please input your apartment preferences.")
#TNKTR USERINPUTS----------------------------------------------------------
#https://github.com/s2t2/shopping-cart-project/blob/master/shopping_cart.py
#!/usr/bin/python3
#https://www.python-course.eu/tkinter_entry_widgets.php
#https://www.python-course.eu/tkinter_text_widget.php
#https://stackoverflow.com/questions/41211060/how-to-add-scrollbar-to-tkinter
#https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/99ce7522557f0a9c8690e48ac95bcce0d528b380/notes/python/packages/tkinter.md

#App set-up----------------------------------------------------------------
#https://www.tutorialspoint.com/python/tk_scrollbar.htm

def apartment():
    apartment_value=[l4.get(i) for i in l4.curselection()]
    print("---------------------------------------")
    print("You have selected: ")
    print(apartment_value)
    
def bed():
    bed_value=[l1.get(i) for i in l1.curselection()]
    print(bed_value)

def bath():
    bath_value=[l2.get(i) for i in l2.curselection()]
    print(bath_value)
    
def notifications():
    notification_value=[l5.get(i) for i in l5.curselection()]
    print(notification_value)
    if 'One time' in notification_value:
        print("You will now receive an email to your inbox")
               
        load_dotenv()

        SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY", "OOPS, please set env var called 'SENDGRID_API_KEY'")
        MY_EMAIL_ADDRESS = os.environ.get("MY_EMAIL_ADDRESS", "OOPS, please set env var called 'MY_EMAIL_ADDRESS'")

        sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)

        from_email = Email(MY_EMAIL_ADDRESS)
        to_email = Email(MY_EMAIL_ADDRESS)
        subject = "Apartment Update!"
        message_text = "Hello, \n\nThe following email provides an update on your desired apartments: "
        content = Content("text/plain", message_text)
        mail = Mail(from_email, subject, to_email, content)

        response = sg.client.mail.send.post(request_body=mail.get())
        pp = pprint.PrettyPrinter(indent=4)

        print("----------------------")
        print("EMAIL")
        print("----------------------")
        print("RESPONSE: ", type(response))
        print("STATUS:", response.status_code) 
        print("HEADERS:")
        pp.pprint(dict(response.headers))
        print("BODY:")
        print(response.body)

       

    else:
        print("After pressing 'Done' you will be given instructions to heroku to configure your emails")

    

w1= Tk()
w1.title('Apartment Selection App')
frame = Frame(w1)

#Configuring Scrollbar

scrollbar = Scrollbar(w1)
scrollbar.pack( side = RIGHT, fill = Y )

mylist = Listbox(w1, yscrollcommand = scrollbar.set )
for line in range(100):
    line =  0 #to put info in this scrollable section


    l1= Listbox(w1, selectmode= MULTIPLE, width= 20, height=5)
    l2= Listbox(w1, selectmode= MULTIPLE, width= 20, height=5)
    l4= Listbox(w1, selectmode= MULTIPLE, width= 20, height=5)
    l5= Listbox(w1, selectmode= MULTIPLE, width= 20, height=5)

    #App Picture--------------------------------------------------------------

    #https://www.slideshare.net/r1chardj0n3s/tkinter-does-not-suck
    T = Text(w1, height=1, width=30)
    T.pack()
    T.insert(END, "Welcome to my application!")

    #image = ImageTk.PhotoImage(Image.open('pic.png')), 
    #tk.Label(w1, image=image).pack()
 
    #Apartment Selection-------------------------------------------------------
    T = Text(w1, height=1, width=30)
    T.pack()
    T.insert(END, "Please select your apartment: ")

    Apartment_Buildings = [
        {"id":1, "name": "avalon-ballston-square", "URL": "https://www.avaloncommunities.com/virginia/arlington-apartments/avalon-ballston-square/floor-plans"},
        {"id":2, "name": "ava-ballston", "URL": "https://www.avaloncommunities.com/virginia/arlington-apartments/ava-ballston/floor-plans"}
        #to add more apartments within Avalon family
    ]

    l = []
    for p in Apartment_Buildings:
        l.append(p["name"])

    Apartment_Buildings = list(set(l))
    Apartment_Buildings = sorted(Apartment_Buildings)

    Apartment= ['avalon-ballston-square','ava-ballston'] #to connect to name on different lines
    for val in Apartment:
        l4.insert(END, val)
    l4.pack()


    b5=Button(text= 'Select', command=apartment)
    b5.pack()

    #Bedroom Selection-------------------------------------------------------
    #T = Text(w1, height=2, width=30)
    #T.pack()
    #T.insert(END, "Please select your desired \n number of bedrooms: ")

    #bedroom= ['Studio', 'One Bedroom', 'Two Bedrooms','More than Two Bedrooms']
    #for val in bedroom:
        #l1.insert(END, val)
    #l1.pack()

    #b1=Button(text= 'Select', command=bed)
    #b1.pack()

    #Bathroom Selection-------------------------------------------------------
    T = Text(w1, height=2, width=30)
    T.pack()
    T.insert(END, "Please select your desired \n number of bathrooms: ")

    bathroom= ['One bathroom', 'Two Bathrooms', 'More than Two Bathrooms']
    for val in bathroom:
        l2.insert(END, val)
    l2.pack()

    b2=Button(text= 'Select', command=bath)
    b2.pack()

    #Budget Selection-------------------------------------------------------
    T = Text(w1, height=2, width=30)
    T.pack()
    T.insert(END, "Please input your \n monthly budget: ")

    budget_value = tkinter.StringVar()
    my_budget = tkinter.Entry(textvariable=budget_value)

    def budget():
        print(my_budget.get())

    my_button = tkinter.Button(text="Select", command=budget)
    my_budget.pack()
    my_button.pack()

    #Move-in Date Selection-------------------------------------------------------
    T = Text(w1, height=2, width=30)
    T.pack()
    T.insert(END, "Please input your move in date with \n the following format mm/dd/yyyy ")

    move_value = tkinter.StringVar()
    my_move = tkinter.Entry(textvariable=move_value)

    def movein():
        print(my_move.get())

    my_button_two = tkinter.Button(text="Select", command=movein)
    my_move.pack()
    my_button_two.pack()


    #Notification Selection------------------------------------------------
    T = Text(w1, height=2, width=30)
    T.pack()
    T.insert(END, "Please select your desired \n notification setting: ")

    emails= ['One time', 'Recurring']
    for val in emails:
        l5.insert(END, val)
    l5.pack()

    b6=Button(text= 'Select', command=notifications)
    b6.pack()

    #Quit Button-----------------------------------------------------------
    b4 = Button(w1, text='Done', command=w1.quit)
    b4.pack()

    w1.mainloop()

    print("---------------------------------------")
    user_input = input("Are these values correct? ")
    y = ["Yes","yes","YES"]
    if user_input in y:
        print ("Great, we will save your inputs!")
        t = datetime.datetime.now()
        print("Response recorded at: ", datetime.datetime.now().strftime("%Y-%m-%d %H:%m:%S")) 
        print("---------------------------------------")
        exit
    else:
        print("Please change your desired inputs and press 'Done'.")
        print("---------------------------------------")
        w1.mainloop()


    mylist.insert(END, (line))

mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )

breakpoint

    #User Inputs Collected------------------------------------------------





    #Scraping the Website--------------------------------------------------
# adapted from: https://selenium-python.readthedocs.io/waits.html

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

URL = "https://www.avaloncommunities.com/virginia/arlington-apartments/avalon-ballston-square/floor-plans"

driver = webdriver.Chrome("/usr/local/bin/chromedriver") 

driver.get(URL)

try:
    listings_appear = EC.presence_of_element_located((By.ID, "floor-plan-listing"))
    wait_duration = 3
    div = WebDriverWait(driver, wait_duration).until(listings_appear)
    print("PAGE LOADED!")
except TimeoutException:
    print("TIME OUT!")
finally:

    soup = BeautifulSoup(driver.page_source, "html.parser")
    one_br_layouts = soup.find("div", id="bedrooms-1").findAll("div", "row")
    
    print("One Bedroom Apartments:")
    print("Number      Move-in Date        Price")
    print("                                       ")

#Apartments listings--------------------------------------------------------------------
    for layout in one_br_layouts:
    
    #Apartment Information-------------------------------------------------------------
        one_br=(layout.find("table").find("tbody").text)
    
    #First Apartment Number, Move-in Date and Budget-----------------------------------------
        one_br_table=(layout.find("table").find("tbody").find("tr").text)
        one_br_number=(one_br_table[1:5])
        one_br_date=(one_br_table[5:15])
        one_br_price=(one_br_table[15:21])
        print((one_br_number) + "          " + str(one_br_date) +  "          "  + str(one_br_price))

     #Other Apartment Number, Move-in Date and Budget-----------------------------------------
        one_br_table=(layout.find("table").find("tbody").text)
        one_br_second_number=(one_br_table[34:38])
        one_br_second_date=(one_br_table[38:48])
        one_br_second_price=(one_br_table[48:54])
        print((one_br_second_number) + "          " + str(one_br_second_date) + "          "  + str(one_br_second_price))

    #Bed, Bath Count-------------------------------------------------------------------
        one_br_listing=(layout.find("h4").text)
        print(one_br_listing)
        number_of_bedrooms=(one_br_listing[0])
        number_of_bathrooms=(one_br_listing[11])
        print("--------------------------------------------")    

    #can manually do it but way to do it through with table?





    #todo:
    #connect avalon list to original list
    #validate tkinter inputs/make sure at least one is selected
    #have to set up a scrollbar
    #to resize image
