import os.path
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.maximize_window()

# navigate to url
driver.get("https://trytestingthis.netlify.app/")

time.sleep(2)

# browser interactions
title = driver.title
print(title)

url = driver.current_url
print(url)

time.sleep(2)

# navigational commands

driver.back()
time.sleep(2)

driver.forward()
time.sleep(2)

driver.refresh()

driver.quit()