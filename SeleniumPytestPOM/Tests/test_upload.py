import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

class Test_Upload:
    def test_up(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/upload")
        time.sleep(2)

        browse = driver.find_element(By.XPATH, "//input[@id='file-upload']")
        browse.send_keys(r"C:\Users\lohit\OneDrive\Pictures\OG wallpaper.jpeg")
        time.sleep(2)
        upload = driver.find_element(By.XPATH, "//input[@id='file-submit']")

        upload.click()
        time.sleep(2)
        fileupload = driver.find_element(By.XPATH, "//h3[normalize-space()='File Uploaded!']")
        assert fileupload.text == "File Uploaded!"

        time.sleep(2)
        driver.close()