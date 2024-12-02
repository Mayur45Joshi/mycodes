import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
#from flask import request


driver = webdriver.Chrome()
driver.implicitly_wait(10)
#driver.get("https://signup.com/")
driver.maximize_window()

# reglink = Keys.CONTROL+Keys.RETURN
# driver.find_element(By.LINK_TEXT,"Register").send_keys(reglink)
# time.sleep(10)

driver.get("https://www.facebook.com/")
#driver.switch_to.new_window('tab')
driver.switch_to.new_window('window')
driver.get("https://www.maxfashion.in/in/en/offers")

