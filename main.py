from lib2to3.pgen2 import driver
from optparse import Option
from sys import platform
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import os

class Bot():
    driver = None
    options = None
    sleep_time = 2
    
    def __init__(self,):
        self.options = Options()
        self.options.page_load_strategy = 'eager'
        self.options.add_argument("--start-maximized")
        prefs = {"download.default_directory" : f"{os.getcwd()}/downloads"}
        self.options.add_experimental_option("prefs",prefs)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
    
    def __del__(self):
        self.driver.close()

    def get_articles(self, name):
        self.driver.get("https://www.wikipedia.org/")
        sleep(self.sleep_time)
        
        search_bar = self.driver.find_element(By.ID, "searchInput")
        search_bar.send_keys(name)
        sleep(self.sleep_time)
        
        suggestion_links = self.driver.find_element(By.CLASS_NAME, "suggestion-link")
        suggestion_links.click()
        sleep(self.sleep_time)
        
        title = self.driver.find_element(By.CLASS_NAME, "firstHeading")
        body = self.driver.find_element(By.ID, "bodyContent")
        print(title.text)
        print(body.text)
        image = self.driver.find_element(By.CLASS_NAME, "thumbinner")
        link = image.find_element(By.TAG_NAME, "a")
        link.click()
        sleep(self.sleep_time)
        
        pre_download_button = self.driver.find_element(By.CLASS_NAME, "mw-mmv-download-button")
        pre_download_button.click()
        sleep(self.sleep_time)
        
        download_button = self.driver.find_element(By.CLASS_NAME, "mw-mmv-download-go-button")
        download_button.click()
        

bot = Bot()
# bot.get_articles("blockchain")
# bot.get_articles("energy")
# bot.get_articles("bb king")

while True:
    bot.get_articles(input("Cerca e scarica la prima immagine di un articolo: "))