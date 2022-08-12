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
    sleep_time = 2
    
    def __init__(self,):
        options = Options()
        options.add_argument("--start-maximized")
        # cambiando questo parametro è possibile cambiare la cartella di download
        prefs = {"download.default_directory" : f"{os.getcwd()}/downloads"}
        options.add_experimental_option("prefs",prefs)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    def __del__(self):
        self.driver.close()

    def get_articles(self, name):
        # apri la pagina al seguente url
        self.driver.get("https://www.wikipedia.org/")
        sleep(self.sleep_time)
        
        # tasto destro sulla barra di ricerca -> ispeziona
        # il bottone ha come id "searchInput"
        # seleziona la barra di ricerca per id
        search_bar = self.driver.find_element(By.ID, "searchInput")
        # scrivi il valore di name nella barra di ricerca
        search_bar.send_keys(name)
        sleep(self.sleep_time)
        
        # si aprono diverse opzioni, di nuovo tasto destro -> ispeziona
        # le opzioni hanno class valorizzata a "suggestion-link"
        # seleziona e clicka il primo fra gli elementi di questa classe
        suggestion_links = self.driver.find_elements(By.CLASS_NAME, "suggestion-link")[0]
        suggestion_links.click()
        sleep(self.sleep_time)
        
        # si apre la pagina dell'articolo
        # seleziona elemento per classe/id (che trovi facendo ispeziona sopra l'oggetto sulla pagina)
        title = self.driver.find_elements(By.CLASS_NAME, "firstHeading")[0]
        body = self.driver.find_element(By.ID, "bodyContent")
        # stampa testo contenuto nell'elemento selezionato
        print(title.text)
        print(body.text)
        image = self.driver.find_elements(By.CLASS_NAME, "thumbinner")[0]
        link = image.find_element(By.TAG_NAME, "a")
        # all'interno dell'elemento selezionato trova il primo elemento con tag "a"
        # quindi il primo <a>...</a> che incontri a partire scendendo da image
        # (image è il primo elemento con classe "thumbinner")
        link.click()
        sleep(self.sleep_time)
        
        # ripeti il ragionamento clickando fino ad arrivare al download
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