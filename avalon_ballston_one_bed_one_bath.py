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
                move_in = '06/07/2019'
                my_budget = '2700'

                num = listing_str[:5]
                date = listing_str[5: listing_str.find("$")]
                price = listing_str[listing_str.find("$"):]
                price_to_int = price[1] + price[3:5]
                price_int = int(price_to_int)

                str_date = listing_str[5: listing_str.find("$")]
                apt_move = datetime.datetime((int(str_date[-4:])),(int(str_date[:2])),(int(str_date[3:5])))
                move_in = datetime.datetime((int(str_date[-4:])),(int(str_date[:2])),(int(str_date[3:5])))
                timediff = (move_in) - (apt_move)


                if (str(price_int) < str(my_budget) and abs(timediff.days)<20):
                    print(listing_str[:5] + "        " + listing_str[5: listing_str.find("$")] +  "         " +  " "  + listing_str[listing_str.find("$"):])
                    one_br_listing=(layout.find("h4").text)

                    
                    csvData.append([num,date,price, one_br_listing])

                    budget = listing_str[listing_str.find("$"):]
                    move_date = listing_str[5: listing_str.find("$")] 
                else:
                    pass


                #to change to update for budget and move in date


                #https://www.youtube.com/watch?v=fc9buLUiqLE
            else:
                pass
        
    #Bed, Bath Count-------------------------------------------------------------------
        one_br_listing=(layout.find("h4").text)
        number_of_bedrooms=(one_br_listing[0])
        number_of_bathrooms=(one_br_listing[11])
        print("--------------------------------------------")    


        with open('apartment3.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(csvData)
        csvFile.close()
