import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver =webdriver.Chrome(service = Service(ChromeDriverManager().install()))
driver.get("https://rsuitejs.com/components/date-picker/")
driver.maximize_window()

cal=driver.find_element(By.XPATH,"(//*[name()='svg'][@aria-label='calender simple'])[1]")
cal.click()
time.sleep(3)
date=driver.find_element(By.XPATH,"(//span[normalize-space()='24'])[1]")
date.click()
time.sleep(3)
click_ok=driver.find_element(By.XPATH,"//button[normalize-space()='OK']")
click_ok.click()
time.sleep(5)
driver.close()