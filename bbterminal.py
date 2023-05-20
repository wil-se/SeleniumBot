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
from pprint import PrettyPrinter
pp = PrettyPrinter()


class Bot():
    driver = None
    sleep_time = 2
    
    def __init__(self,):
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--headless")
        # prefs = {"download.default_directory" : f"{os.getcwd()}/downloads"}
        # options.add_experimental_option("prefs",prefs)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    def __del__(self):
        self.driver.close()

    def get_tiles_content(self, url):
        self.driver.get(url)
        sleep(self.sleep_time)
        # that's the only list with a p tag inside
        tiles_list = self.driver.find_elements(By.CLASS_NAME, 'rounded')
        tiles = []
        for el in tiles_list:
            try:
                content = el.find_elements(By.TAG_NAME, 'p')
                title = content[0]
                description = content[1]
                tiles.append(title.text.strip())
            except Exception as e:
                print(el.text)
                # print(e)
        return tiles

    def get_reference(self, reference):
        url = f'https://docs.openbb.co/sdk/reference/{reference}'
        tiles = self.get_tiles_content(url)
        return tiles
    
    def get_all_references(self):
        url = 'https://docs.openbb.co/sdk/reference'
        references = self.get_tiles_content(url)
        result = {}
        for reference in references:
            res = self.get_reference(reference)
            result[reference] = res
        return result


instance = Bot()
references = instance.get_all_references()
pp.pprint(references)