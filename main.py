import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "YOUR CHROME DRIVER PATH"
TWITTER_USERNAME = "YOUR USERNAME/EMAIL"
TWITTER_PASSWORD = "YOUR PASSWORD"


class InternetSpeedTwitterBot():


    def __init__(self, driver_path):
        self.counter = 0
        self.service = Service(driver_path)
        self.driver = webdriver.Chrome(service=self.service)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.maximize_window()
        self.driver.get("https://www.speedtest.net/")
        self.go_btn = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]")
        self.go_btn.click()

        time.sleep(50)
        self.down = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span").text
        self.up = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span").text

    def tweet_at_provider(self):
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://twitter.com/login")
        time.sleep(2)
        username = self.driver.find_element(By.TAG_NAME, 'div input')
        username.send_keys(TWITTER_USERNAME)
        username.send_keys(Keys.ENTER)
        time.sleep(2)
        password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)
        compose_tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div') 
        compose_tweet.send_keys(f"Hey Internet Provider, why's my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")
        time.sleep(2)
        tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        tweet.click()


my_bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)

my_bot.get_internet_speed()
my_bot.tweet_at_provider()