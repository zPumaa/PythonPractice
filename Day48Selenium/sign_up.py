from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

website_link = "https://secure-retreat-92358.herokuapp.com/"

driver = webdriver.Chrome(options=chrome_options)
driver.get(website_link)

first_name = driver.find_element(By.NAME, value="fName")
last_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")

first_name.send_keys("Lewis")
last_name.send_keys("Hamilton")
email.send_keys("lewishamilton@gmail.com")

submit_btn = driver.find_element(By.XPATH, value='/html/body/form/button')
submit_btn.click()