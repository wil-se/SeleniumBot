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

class Bot():
    driver = None
    options = None
    sleep_time = 4
    
    def __init__(self,):
        self.options = Options()
        self.options.page_load_strategy = 'eager'
        self.options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
    
    def __del__(self):
        self.driver.close()

    # bisogna mettere una sleep all'inizio di ogni funzione
    # perché il bot esegue le funzioni molto più rapidamente
    # di quanto non farebbe una persona rispetto al browser
    # quindi potrebbe succedere che il browser non fa in tempo a caricare la pagina
    # che il bot ha già eseguito la prossima funzione
    # risultando in un errore
    # per cui bisogna aspettare sempre un po'
    def accept_cookies_from_ansa(self):
        sleep(self.sleep_time)
        
        # se la funzione nel try va in errore
        # (perché magari abbiamo già accettato i cookies
        # e il driver non trova più l'elemento  da clickare nella pagina)
        # esegui la funzione dentro except
        
        # facendo ispeziona sulla pagina notiamo che
        # il bottone Accetta ha come classe "iubenda-cs-opt-group-consent"
        # per cui bisognerà prima aspettare
        # fino a che non è presente nella pagina
        # almeno un elemento di questa classe
        # poi selezionarlo e clickarlo
        #WebDriverWait(self.driver, 4).until(EC.presence_of_element_located((By.CLASS_NAME, 'iubenda-cs-opt-group-consent')))
        accept_button = self.driver.find_element(By.CLASS_NAME, "iubenda-cs-opt-group-consent")
        sleep(self.sleep_time)
        accept_button.click()
        


    def get_energy_articles_from_ansa(self):
        # se la funzione nel try va in errore
        # (perché magari abbiamo già accettato i cookies
        # e il driver non trova più l'elemento  da clickare nella pagina)
        # esegui la funzione dentro except
        self.driver.get("https://www.ansa.it/canale_ambiente/notizie/energia/index.shtml")
        self.accept_cookies_from_ansa()
        print("cookie accettati")
        sleep(self.sleep_time)
        # facendo ispeziona nella pagina notiamo che
        # tutti gli articoli sono contenuti in classi "news"
        # tranne il primo che è "pp-news"
        # quindi chiediamo al driver tutti gli oggetti nella pagina
        # che hanno come classe "news" o "pp-news"
        main_new = self.driver.find_element(By.CLASS_NAME, "pp-news")
        news = self.driver.find_elements(By.CLASS_NAME, "news")
        last_article = 0
        while last_article < len(news):
            print(f"getting article {last_article}")
            self.driver.get("https://www.ansa.it/canale_ambiente/notizie/energia/index.shtml")
            sleep(self.sleep_time)
            print("aaa")
            self.driver.execute_script("window.stop();")
            news = self.driver.find_elements(By.CLASS_NAME, "news")
            new = news[last_article].find_element(By.TAG_NAME, 'a')
            print("click")
            actions = ActionChains(self.driver)
            actions.move_to_element(new)
            actions.click(new)
            actions.perform()
            print("aaa")
            sleep(10)
            print("going back")
            last_article += 1


bot = Bot()
bot.get_energy_articles_from_ansa()


sleep(10)