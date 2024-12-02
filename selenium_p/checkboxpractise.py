import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes=driver.find_elements(By.XPATH, "//input[contains(text(),' Option2 ')]")

print(len(checkboxes))

time.sleep(2)

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()

        break


radiobuttones = driver.find_elements(By.XPATH, "//input[@name='radioButton']")

time.sleep(2)

for radiobutton in radiobuttones:
    if radiobutton.get_attribute("value") == "radio1":
        radiobutton.click()

        assert radiobutton.is_selected()

        break



assert driver.find_element(By.ID, "displayed-text").is_displayed()

driver.find_element(By.ID, "hide-textbox").click()

#assert driver.find_element(By.ID, "displayed-text").is_displayed()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()
