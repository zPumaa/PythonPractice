import os, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

PROMISED_DOWN = 500
PROMISED_UP = 50
TWITTER_USERNAME = os.getenv('TWITTER_USER')
TWITTER_PASSWORD = os.getenv('TWITTER_PASSWORD')
SPEED_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://www.x.com/"
TWITTER_TARGET = "EE"

class InternetSpeedTwitterBot:
    def __init__(self):
        self.up = 0
        self.down = 0

        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)  # Option to keep Chrome open

        self.driver = webdriver.Chrome(options=options)
        self.driver2 = webdriver.Chrome(options=options)

    def get_internet_speed(self):
        self.driver.get(SPEED_URL)
        time.sleep(1)
        reject = self.driver.find_element(By.ID, value="onetrust-reject-all-handler")
        reject.click()

        time.sleep(1)
        go = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go.click()

        time.sleep(60)
        try:
            close_window = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/a')
            close_window.click()
        except NoSuchElementException:
            pass
        self.down = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

    def tweet_at_provider(self):
        self.driver2.get(TWITTER_URL)
        time.sleep(1)
        sign_in = self.driver2.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[3]/a/div')
        sign_in.click()

        time.sleep(2)
        user_entry = self.driver2.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
        user_entry.click()
        user_entry.send_keys(TWITTER_USERNAME + Keys.ENTER)

        time.sleep(1)
        password_entry = self.driver2.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password_entry.send_keys(TWITTER_PASSWORD + Keys.ENTER)

        time.sleep(2)
        self.driver2.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[1]/button/div/svg').click()
        self.driver2.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div').click()

        time.sleep(1)
        tweet_entry = self.driver2.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div')
        tweet_entry.click()
        tweet = (f"Hello @{TWITTER_TARGET}, My download speed is {speedBot.down} Mbps "
                f"and my upload speed is {speedBot.up} Mbps. These are not the promised speeds "
                f"of {PROMISED_DOWN} and {PROMISED_UP}. This is just a twitter bot, do not reply to this message.")
        tweet_entry.send_keys(tweet + Keys.ENTER)


speedBot = InternetSpeedTwitterBot()
speedBot.get_internet_speed()
# print(f"Download speed is {speedBot.down} Mbps.")
# print(f"Upload speed is {speedBot.up} Mbps.")
if (float(speedBot.down) < PROMISED_DOWN) or (float(speedBot.up) < PROMISED_UP):
    speedBot.tweet_at_provider()
