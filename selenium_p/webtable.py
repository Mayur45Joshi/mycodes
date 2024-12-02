import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(5)
time.sleep(5)
driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//a[@class='oxd-main-menu-item active']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//ul[@class='oxd-main-menu']/li[1]").click()
time.sleep(5)
driver.find_element(By.XPATH,"//span[contains(text(),'User Management')]").click()
time.sleep(5)
driver.find_element(By.LINK_TEXT,"Users").click()
time.sleep(10)

rows=len(driver.find_elements(By.XPATH,"//div[@class='oxd-table-body']/div"))
print("total no of rows : ", rows)

count=0
for r in range(1,rows+1):
    status = driver.find_element(By.XPATH,"//div[@class='oxd-table-body']/div["+str(r)+"]//div[5]").text
    if status=="Enabled":
        count=count+1

print("total no of rows : ",rows)
print("total no of enabled :", count)
print("total no of disabled : ",(rows-count))

