from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
source=driver.find_element(By.ID,"draggable")
dest=driver.find_element(By.ID,"droppable")

action=ActionChains(driver)
action.drag_and_drop(source,dest).perform()
dest_text=dest.text
print(dest_text)