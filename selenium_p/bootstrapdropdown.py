import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
#from flask import request


driver = webdriver.Chrome()
#driver.implicitly_wait(10)
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()
country_list = driver.find_elements(By.XPATH,"//ul[@id='select2-billing_country-results']/li")

print(len(country_list))

for country in country_list:
    if country.text =="India":
        country.click()
        time.sleep(5)
        break

#driver.save_screenshot("C:\\Users\\HP\\Desktop\\DESKTOP\\mj.png")
#driver.save_screenshot(os.getcwd()+"\\mj.png")
#driver.get_screenshot_as_file(os.getcwd()+"\\mj1.png")