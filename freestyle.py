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
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import csv 


print("To start, please input your apartment preferences.")
#TNKTR USERINPUTS----------------------------------------------------------
#https://github.com/s2t2/shopping-cart-project/blob/master/shopping_cart.py
#!/usr/bin/python3
#https://www.python-course.eu/tkinter_entry_widgets.php
#https://www.python-course.eu/tkinter_text_widget.php
#https://stackoverflow.com/questions/41211060/how-to-add-scrollbar-to-tkinter
#https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/99ce7522557f0a9c8690e48ac95bcce0d528b380/notes/python/packages/tkinter.md
#https://www.tutorialspoint.com/python/tk_scrollbar.htm
#https://stackoverflow.com/questions/7974849/how-can-i-make-one-python-file-run-another

#Tkinter Button Commands Have to Be Defined First---------------------------------------------------
selections = []

def apartment():
    apartment_value=[l4.get(i) for i in l4.curselection()]
    if len(apartment_value)> 0:
        print("---------------------------------------")
        print("You have selected: ")
        print(apartment_value)
        selections.append(apartment_value)
    else:
        print("Oh no, please make a selection!")

    csvData =  ['A']
    csvData.append(apartment_value)
    with open('apartment.csv', 'w') as csvFile: #budget kept clearing over this so made 2 CSVs
        csvFile.truncate()
        writer = csv.writer(csvFile)
        writer.writerows(csvData)
    csvFile.close()


def budget():
    bueno = int(my_budget.get())
    if bueno < 0: #was unable to find a way to validate that user inputted numbers with tkinter because it just kept giving me an error when I tried to do it with an if statement
        print ("Oh no, please ensure you are printing a positive value!")
    else:
        print(my_budget.get())
        selections.append(my_budget.get())
        #http://net-informations.com/python/iq/global.htm
        #https://stackoverflow.com/questions/12277864/python-clear-csv-file

    csvData =  ['B']
    csvData.append([bueno])
    with open('budget.csv', 'w') as csvFile: 
        csvFile.truncate()
        writer = csv.writer(csvFile)
        writer.writerows(csvData)
    csvFile.close()

def notifications():
    notification_value=[l5.get(i) for i in l5.curselection()]
    if len(notification_value)> 0:
        print(notification_value)
        selections.append(notification_value)
    else:
        print("Oh no, please make a selection!")

def select():
    print("Your final selections are:")
    
    print(selections)
    budget = (my_budget.get())
    new_budget = int(budget)
    

    print("---------------------------------------")
    user_input = input("Are these values correct? If so, please type 'Yes'")
    y = ["Yes","yes","YES"]
    if user_input in y:
        print ("Great, we will save your inputs!")
        t = datetime.datetime.now()
        print("Response recorded at: ", datetime.datetime.now().strftime("%Y-%m-%d %H:%m:%S")) 
        print("To exit the program, please click the application x in the top left corner")
        os.system('python app/logic.py')
        print("---------------------------------------")

        if len(selections) < 3: #user input validation, making sure that everything is selected
            print("Please make sure everything is selected. Reselect each of your preferences and press 'Done' when complete.")
            selections.clear() #https://www.geeksforgeeks.org/list-methods-in-python-set-2-del-remove-sort-insert-pop-extend/
        else:
            pass

    else:
        print("Please change your desired inputs and press 'Done'.")
        selections.clear() #https://www.geeksforgeeks.org/list-methods-in-python-set-2-del-remove-sort-insert-pop-extend/
        print("---------------------------------------")



#Tkiner Interface---------------------------------------------------------------------------------
w1= Tk()
w1.title('Apartment Selection App')
frame = Frame(w1)

l1= Listbox(w1, selectmode= MULTIPLE, width= 20, height=5)
l2= Listbox(w1, selectmode= MULTIPLE, width= 20, height=5)
l4= Listbox(w1, selectmode= MULTIPLE, width= 20, height=5)
l5= Listbox(w1, selectmode= MULTIPLE, width= 20, height=5)

#App Picture--------------------------------------------------------------

#https://www.slideshare.net/r1chardj0n3s/tkinter-does-not-suck

image = ImageTk.PhotoImage(Image.open('pic.png')), 
tk.Label(w1, image=image).pack()

T = Text(w1, height=3, width=30)
T.pack()
T.insert(END, "Welcome to my application! \n This has been configured for \n One Bed, One Baths")

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

Apartment= [Apartment_Buildings[0],Apartment_Buildings[1]] #to connect to name on different lines
for val in Apartment:
    l4.insert(END, val)
l4.pack()


b5=Button(text= 'Select', command=apartment)
b5.pack()

#Budget Selection-------------------------------------------------------
T = Text(w1, height=2, width=30)
T.pack()
T.insert(END, "Please input your \n monthly budget: ")

budget_value = tkinter.StringVar()
my_budget = tkinter.Entry(textvariable=budget_value)

my_button = tkinter.Button(text="Select", command=budget)
my_budget.pack()
my_button.pack()

#Notification Selection------------------------------------------------
T = Text(w1, height=2, width=30)
T.pack()
T.insert(END, "Please select your desired \n notification setting: ")

mails= ['One time'] #to add in heroku notifications
for val in mails:
    l5.insert(END, val)
l5.pack()

b6=Button(text= 'Select', command=notifications)
b6.pack()

#Selections Button-----------------------------------------------------------
b4 = Button(w1, text='Done', command=select)
b4.pack()

w1.mainloop()
mylist.insert(END, (line))

