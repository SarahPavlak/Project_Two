import tkinter as tk
from tkinter import *
import datetime
import tkinter
from PIL import Image, ImageTk

print("To start, please input your apartment preferences.")
#TNKTR USERINPUTS----------------------------------------------------------
#https://github.com/s2t2/shopping-cart-project/blob/master/shopping_cart.py
#!/usr/bin/python3
#https://www.python-course.eu/tkinter_entry_widgets.php
#https://www.python-course.eu/tkinter_text_widget.php
#https://stackoverflow.com/questions/41211060/how-to-add-scrollbar-to-tkinter
#https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/99ce7522557f0a9c8690e48ac95bcce0d528b380/notes/python/packages/tkinter.md

#App set-up----------------------------------------------------------------
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
    notification_value=[e2.get(i) for i in e2.curselection()]
    print(notification_value)

w1= Tk()
w1.title('Apartment Selection App')
frame = Frame(w1)


l1= Listbox(w1, selectmode= MULTIPLE, width= 20, height=5)
l2= Listbox(w1, selectmode= MULTIPLE, width= 20, height=5)
l4= Listbox(w1, selectmode= MULTIPLE, width= 20, height=5)
l5= Listbox(w1, selectmode= MULTIPLE, width= 20, height=5)

#App Picture--------------------------------------------------------------
#https://www.slideshare.net/r1chardj0n3s/tkinter-does-not-suck
T = Text(w1, height=1, width=30)
T.pack()
T.insert(END, "Welcome to my application!")

image = ImageTk.PhotoImage(Image.open('pic.png')), 
tk.Label(w1, image=image).pack()

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

budget_value = tkinter.StringVar()
my_budget = tkinter.Entry(textvariable=budget_value)

def budget():
    print(my_budget.get())

my_button = tkinter.Button(text="Select", command=budget)
my_budget.pack()
my_button.pack()

#Move-in Date Selection-------------------------------------------------------
T = Text(w1, height=3, width=30)
T.pack()
T.insert(END, "Please input your \n move in date with \n the following format mm/dd/yyyy ")

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


breakpoint

#User Inputs Collected------------------------------------------------





#Scraping the Website--------------------------------------------------




#todo:
#connect avalon list to original list
#validate tkinter inputs/make sure at least one is selected
