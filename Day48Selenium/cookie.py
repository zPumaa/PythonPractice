from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import threading

def checkBal():
    # threading.Timer(5.0, checkBal).start()
    bal = money.text
    print(bal)
    return bal

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

website_link = "https://orteil.dashnet.org/experiments/cookie/"

driver = webdriver.Chrome(options=chrome_options)
driver.get(website_link)

cookie = driver.find_element(By.ID, value="cookie")
money = driver.find_element(By.ID, value="money")

def update_store():
    store = driver.find_element(By.ID, value="store")
    store_items = store.find_elements(By.CSS_SELECTOR, value="div b")

    items = []
    for item in range(len(store_items)):
        text = store_items[item].text
        text = text.split("-")
        items.append(text)
    items.pop()
    new_items = []
    for item in items:
        reward = item[0].strip()
        price = item[1].strip()
        array = [reward, price]
        new_items.append(array)
    new_items = new_items[::-1]
    return new_items

def purchase_reward(reward_items):
    bal = checkBal()
    for reward in reward_items:
        price = reward[1].replace(",", "")
        if int(bal) > int(price):
            idToSearch = "buy"+reward[0]
            purchase = driver.find_element(By.ID, value=idToSearch)
            purchase.click()
            print(f"{reward[0]} purchased.")
        else:  
            continue

click_cookie = True
def click_cookie_forever():
    while click_cookie:
        cookie.click()

def purchase_forever():
    while click_cookie:
        new_items = update_store()
        purchase_reward(new_items)
        time.sleep(5)

# Start the threads
threading.Thread(target=click_cookie_forever).start()
threading.Thread(target=purchase_forever).start()