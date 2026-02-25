import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Test_WebElements:
    def test_webelements(self):
        driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")

        driver.find_element(By.ID, "autocomplete").send_keys("Ind")

        time.sleep(2)
        countries = driver.find_elements(By.CSS_SELECTOR, ".ui-menu-item div")
        for country in countries:
            if country.text == "India":
                country.click()
                break

        # switch window
        driver.find_element(By.ID, "openwindow").click()
        driver.find_element(By.ID, "opentab").click()
        time.sleep(2)

        # alert handling - simple
        driver.find_element(By.ID, "name").send_keys("Rahul")
        driver.find_element(By.ID, "alertbtn").click()

        alert = driver.switch_to.alert
        print(alert.text)
        alert.accept()
        # confirm alert
        driver.find_element(By.ID, "confirmbtn").click()

        alert = driver.switch_to.alert
        print(alert.text)
        alert.dismiss()
        time.sleep(2)

        # web table
        rows = driver.find_elements(By.XPATH, "//table[@id='product']/tbody/tr")

        for row in rows:
            print(row.text)

        cols = driver.find_elements(By.XPATH, "//table[@id='product']/tbody/tr[1]/td")

        for col in cols:
            print(col.text)

        time.sleep(4)

        # fixed header table
        rows = driver.find_elements(By.CSS_SELECTOR, ".tableFixHead table tbody tr")

        for row in rows:
            print(row.text)

        time.sleep(3)

        # show / hide textbox
        driver.find_element(By.ID, "hide-textbox").click()
        time.sleep(1)
        driver.find_element(By.ID, "show-textbox").click()
        time.sleep(3)

        # mouse hover
        hover = driver.find_element(By.ID, "mousehover")
        actions = ActionChains(driver)

        actions.move_to_element(hover).perform()

        driver.find_element(By.LINK_TEXT, "Top").click()
        time.sleep(3)

        # iframe handling
        driver.switch_to.frame("courses-iframe")

        driver.find_element(By.LINK_TEXT, "Courses").click()

        driver.switch_to.default_content()

        time.sleep(4)
        driver.close()
