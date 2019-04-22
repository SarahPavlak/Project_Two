# adapted from: https://selenium-python.readthedocs.io/waits.html
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import datetime
import csv


URL = "https://www.avaloncommunities.com/virginia/arlington-apartments/avalon-ballston-square/floor-plans"
driver = webdriver.Chrome("/usr/local/bin/chromedriver") 
driver.get(URL)

csvData =  [['Apartment Number ', 'Move-In ','Budget ']] #to link output to this


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
    print("                                       ")
    print("Number      Move-in Date        Price")

#Apartments listings--------------------------------------------------------------------
    for layout in one_br_layouts:
    
    #Apartment Information-------------------------------------------------------------
        one_br=(layout.find("table").find("tbody").text)
        one_br_str= str(one_br)
        one_br_list = one_br_str.split("View Details")

        

        for listing_str in one_br_list:
            if listing_str != " ":
                #budget validation:
                price = listing_str[listing_str.find("$"):]
                price_to_int = price[1:6]
                new_price = price_to_int.replace(',', "")
                new_new_price = (int(new_price))
                #print(new_price)
                monthly_budget = 2200
                
                p = []
                if monthly_budget > new_new_price:
                    p.append(new_new_price)
                    #print(p) 
                    print(listing_str[:5] + "        " + listing_str[5: listing_str.find("$")] +  "         " +  " "  + str(p))
                    woo_budget = (listing_str[:5] + "        " + listing_str[5: listing_str.find("$")] +  "         " +  " "  + str(p))

                    csvData.append([woo_budget])
                    with open('apartment3.csv', 'a+') as csvFile:
                        writer = csv.writer(csvFile)
                        writer.writerows(csvData)
                    csvFile.close()
                
                
                else: 
                    pass

        
            else:
                pass
