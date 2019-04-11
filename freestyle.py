import tkinter as tk
from tkinter import *
import datetime


print("To start, please input your apartment preferences.")

#TNKTR USERINPUTS----------------------------------------------------------
#https://github.com/s2t2/shopping-cart-project/blob/master/shopping_cart.py
#!/usr/bin/python3
#https://www.python-course.eu/tkinter_entry_widgets.php
#https://www.python-course.eu/tkinter_text_widget.php
#https://stackoverflow.com/questions/41211060/how-to-add-scrollbar-to-tkinter


#App set-up----------------------------------------------------------------
def apartment():
    apartment_value=[l4.get(i) for i in l4.curselection()]
    print("--------------------------------------------")
    print("You have selected: ")
    print(apartment_value)
    
def bed():
    bed_value=[l1.get(i) for i in l1.curselection()]
    print(bed_value)

def bath():
    bath_value=[l2.get(i) for i in l2.curselection()]
    print(bath_value)
      
def budget():
    budget_value=[l3.get(i) for i in l3.curselection()]
    print(budget_value)
    
w1= Tk()
w1.title('Apartment Selection App')

l1= Listbox(w1, selectmode= MULTIPLE, width= 20, height=5)
l2= Listbox(w1, selectmode= MULTIPLE, width= 20, height=5)
l3= Entry(w1, width= 20)
l4= Listbox(w1, selectmode= MULTIPLE, width= 20, height=5)

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

Apartment= ['avalon-ballston-square','ava-ballston'] 
for val in Apartment:
    l4.insert(END, val)
l4.pack()


b5=Button(text= 'Select', command=apartment)
b5.pack()

#Bedroom Selection-------------------------------------------------------
T = Text(w1, height=2, width=30)
T.pack()
T.insert(END, "Please select your desired \n number of bedrooms: ")

bedroom= ['Studio', 'One Bedroom', 'Two Bedrooms','More than Two Bedrooms']
for val in bedroom:
    l1.insert(END, val)
l1.pack()

b1=Button(text= 'Select', command=bed)
b1.pack()

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

budget = [0]
for val in budget:
    l3.insert(END, val)
l3.pack()

b3=Button(text='Select', command=budget)
b3.pack()

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
else:
    print("Please change your desired inputs and press 'Done'.")
    w1.mainloop()
     
w1.mainloop()

#User Inputs Collected------------------------------------------------


#Scraping the Website--------------------------------------------------

