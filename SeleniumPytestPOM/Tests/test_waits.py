import time

from selenium import webdriver
from selenium.common import ElementNotInteractableException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager

class Test_Waits:
    def test_waits(self, revealed=None):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.maximize_window()
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        driver.implicitly_wait(2)

        # explict wait
        radio_btn = driver.find_element(By.XPATH, "(//input[@value='radio2'])[1]")
        wait = WebDriverWait(driver, timeout=2)
        wait.until(lambda _: radio_btn.is_dispalayed())

        # custom wait or fluent wait

        errors = [NoSuchElementException, ElementNotInteractableException]
        wait = WebDriverWait(driver, timeout=2, poll_frequency=.2, ignored_exceptions=errors)
        wait.until(lambda _: revealed.send_keys("Displayed") or True)

        driver.close()