import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

class Test_Keyboard:
    def test_keyboard(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.maximize_window()
        driver.get("https://www.facebook.com/")
        time.sleep(2)

        actions = ActionChains(driver)
        email = driver.find_element(By.XPATH, "//input[@name = 'email']")
        seriesofactions = actions.move_to_element(email).key_down(Keys.SHIFT).send_keys("hello")
        seriesofactions.perform()

        driver.close()
