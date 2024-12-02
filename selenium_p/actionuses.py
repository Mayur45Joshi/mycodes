#from selenium_p import webdriver
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
#from selenium_p.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#driver = webdriver.Chrome("C:\\Users\\DELL\\Downloads\\chromedriver.exe")
#servie_obj = Service("C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python312\\Scripts\\chromedriver.exe")
#driver = webdriver.Chrome(Service=servie_obj)


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()

#action.move_to_element(driver.find_element(By.LINK_TEXT,"Top")).click().perform()

time.sleep(5)

action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()

action.move_to_element(driver.find_element(By.LINK_TEXT,"Top")).click().perform()
