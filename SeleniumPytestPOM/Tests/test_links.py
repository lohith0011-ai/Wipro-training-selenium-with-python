import os.path
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

DOWNLOAD_DIR = r"C:\Users\lohit\Downloads"
class Test_download:
    def test_dw(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/download")
        time.sleep(2)

        links = driver.find_elements(By.TAG_NAME, "a")
        count = len(links)
        print(count)

        for link in links:
            print(link.text)

        time.sleep(2)
        driver.close()
