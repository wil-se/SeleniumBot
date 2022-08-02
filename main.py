from sys import platform
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



driver = webdriver.Chrome(executable_path=f'chromedrivers/{"linux" if "linux" in platform else "mac"}_chromedriver')
driver.get("http://www.python.org")
elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
driver.close()