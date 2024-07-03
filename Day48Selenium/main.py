from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# product_link = "https://www.amazon.co.uk/WD_BLACK-SN850X-2280-Gaming-speed/dp/B0B7CKVCCV/"
# product_price = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
# product_price_fraction = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
# print(f"The price is £{product_price}.{product_price_fraction}")

website_link = "https://www.python.org/"

driver = webdriver.Chrome(options=chrome_options)
driver.get(website_link)

events_dict = {}
events = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
dates = events.find_elements(By.CSS_SELECTOR, value="li time")
names = events.find_elements(By.CSS_SELECTOR, value="li a")

for date in range(len(dates)):
    event_date = dates[date].text
    event_name = names[date].text
    events_dict[date] = {
        "time": event_date,
        "name": event_name
    }

print(events_dict)

