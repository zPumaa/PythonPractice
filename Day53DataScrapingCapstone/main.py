from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import requests, time

PROPERTY_URL = "https://appbrewery.github.io/Zillow-Clone/"
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSe0KG8r1LFnajRi9BrjlW0A3wVjB0U-XwwqQIsJE_-JHPw19A/viewform?usp=sf_link"
EDIT_FORM_URL = "https://docs.google.com/forms/d/17-w_uAbMAIjuKDfjLARdz7EmicSA7YIewHi0RypehkE/edit#responses"

class Rent:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)  # Option to keep Chrome open

        self.driver = webdriver.Chrome(options=options)


    def get_listings(self):
        response = requests.get(PROPERTY_URL)
        soup = BeautifulSoup(response.text, "html.parser")
        properties = soup.find_all(class_="StyledPropertyCardDataWrapper")
        listings = []

        for property in properties:
            link = property.find("a")["href"]
            address = property.find("address").get_text().strip()
            price = property.find(class_="PropertyCardWrapper__StyledPriceLine").get_text()
            price = price.split("+")[0].split("/")[0]
            
            listing = {}
            listing["link"] = link
            listing["address"] = address
            listing["price"] = price
            listings.append(listing)

        return listings

    def populate_form(self, listing):
        self.driver.get(FORM_URL)
        time.sleep(1)

        address_box = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        address_box.send_keys(listing["address"])
        time.sleep(1)

        price_box = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price_box.send_keys(listing["price"])
        time.sleep(1)

        link_box = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link_box.send_keys(listing["link"])
        time.sleep(1)

        submit_btn = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
        submit_btn.click()

    def make_sheet(self):
        self.driver.get(EDIT_FORM_URL)
        time.sleep(1)

rent = Rent()
listings = rent.get_listings()
for listing in listings:
    rent.populate_form(listing)
