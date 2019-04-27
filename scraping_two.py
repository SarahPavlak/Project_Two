# adapted from: https://selenium-python.readthedocs.io/waits.html
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import datetime
import csv
import time
from datetime import timedelta
import os 



#reading to see which apartment is selected
with open("apartment.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        apartment = (row['A'])
        print(apartment)

#
with open("budget.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        budget = (row['B'])
        your_budget = int(budget)

URL = "https://www.avaloncommunities.com/virginia/arlington-apartments/avalon-ballston-square/floor-plans"
driver = webdriver.Chrome("/usr/local/bin/chromedriver") 
driver.get(URL)

csvData =  [] 

try:
    listings_appear = EC.presence_of_element_located((By.ID, "floor-plan-listing"))
    wait_duration = 10
    div = WebDriverWait(driver, wait_duration).until(listings_appear)
    print("PAGE LOADED!")
except TimeoutException:
    print("TIME OUT!")
finally:
    soup = BeautifulSoup(driver.page_source, "html.parser")
    one_br_layouts = soup.find("div", id="bedrooms-1").findAll("div", "row")
    
    print("One Bedroom Apartments:")
    print("                                       ")
    print("Apt      Number        Move-in Date        Price      Additional Details")

#Apartments listings--------------------------------------------------------------------
    for layout in one_br_layouts:
    
    #Apartment Information-------------------------------------------------------------
        one_br=(layout.find("table").find("tbody").text)
        one_br_str= str(one_br)
        one_br_list = one_br_str.split("View Details")

        for listing_str in one_br_list:
            if listing_str != " ":
                one_br_listing=(layout.find("h4").text)
                #budget validation:
                move_date = listing_str[5: listing_str.find("$")]
                price = listing_str[listing_str.find("$"):]
                price_to_int = price[1:6]
                new_price = price_to_int.replace(',', "")
                new_new_price = (int(new_price))
                monthly_budget = your_budget
                
                p = []
                if monthly_budget > new_new_price:
                    p.append(new_new_price) 
                    print("Avalon" +  "   " + listing_str[:5] + "          " + move_date +  "         " +  str(p) + "    " + str(one_br_listing))
                    woo_budget = ("Avalon" +  "   " + listing_str[:5] + "          " + move_date +  "         " +  str(p) + "    " + str(one_br_listing))

                    csvData.append([woo_budget]) #https://www.youtube.com/watch?v=XynRRjG_k4I
                    with open('ava_avalon.csv', 'a+') as csvFile:
                        writer = csv.writer(csvFile)
                        writer.writerows(csvData)
                    csvFile.close()

                    with open ('ava_avalon.csv') as csvFile:
                        data = list(csv.reader(csvFile))
                        new_data = [a for i, a in enumerate (data) if a not in data [:i]]
                        with open ('ava_avalon.csv', 'w') as t:
                            write = csv.writer(t)
                            write.writerows(new_data) #http://lancerous.com/detail/48853461/48853527 gets rid of duplicates, before was having a long list duplicates


     
            
                
                else: 
                    pass



                
                #https://www.youtube.com/watch?v=fc9buLUiqLE
          
        


        


