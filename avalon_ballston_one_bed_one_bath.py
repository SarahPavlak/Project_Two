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
        one_br_str= str(one_br)
        one_br_list = one_br_str.split("View Details")

        for listing_str in one_br_list:
            if listing_str != " ":
                print(listing_str[:5] + "        " + listing_str[5: listing_str.find("$")] +  "         " +  "     "  + listing_str[listing_str.find("$"):])
                #https://www.youtube.com/watch?v=fc9buLUiqLE
            else:
                pass
          
    #Bed, Bath Count-------------------------------------------------------------------
        one_br_listing=(layout.find("h4").text)
        print(one_br_listing)
        number_of_bedrooms=(one_br_listing[0])
        number_of_bathrooms=(one_br_listing[11])
        print("--------------------------------------------")    

