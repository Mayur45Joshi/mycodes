import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

name = "Mayur"
driver.find_element(By.ID, "name").send_keys(name)

driver.find_element(By.ID, "alertbtn").click()
alerts = driver.switch_to.alert
alerttext = alerts.text

#driver.get("http://admin:admin@facebook.com")    #for authenticated popups and alerts

#alerts.send_keys("MJ")
#alerts.accept()
#alerts.dismiss()

print(alerttext)
assert name in alerttext
alerts.accept()

