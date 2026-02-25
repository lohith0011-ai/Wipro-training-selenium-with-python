import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Test_MultiSelectRadio:
    def test_multiradio(self):
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )
        driver.maximize_window()
        driver.get("https://testautomationpractice.blogspot.com/")

        # find all checkboxes (BEST PRACTICE)
        checkbox_list = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
        print("Total checkboxes:", len(checkbox_list))

        # iterate and click each checkbox
        for checkbox in checkbox_list:
            time.sleep(5)
            if not checkbox.is_selected():
                checkbox.click()

        # verification (optional but good)
        for checkbox in checkbox_list:
            assert checkbox.is_selected()

        driver.quit()