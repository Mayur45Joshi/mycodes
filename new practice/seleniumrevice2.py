import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://testautomationpractice.blogspot.com/")
driver.find_element(By.XPATH,"//input[@id='datepicker']").click()
driver.find_element(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a[text()='19']").click()
time.sleep(3)

driver.find_element(By.XPATH,"//input[@id='txtDate']").click()
driver.find_element(By.XPATH,"//select[@aria-label='Select year']/option[text()='2024']").click()
driver.find_element(By.XPATH,"//select[@aria-label='Select month']/option[text()='Jan']").click()
driver.find_element(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a[text()='15']").click()
time.sleep(3)

#driver.find_element(By.XPATH,"//div[@class='date-picker-box']/input[@id='start-date']").click()
driver.find_element(By.XPATH,"//div[@class='date-picker-box']/input[@id='start-date']").send_keys("19-05-2024")
driver.find_element(By.XPATH,"//div[@class='date-picker-box']/input[@id='end-date']").send_keys("19-08-2025")
driver.find_element(By.XPATH,"(//button[text()='Submit' or @class='submit-btn'])[1]").click()
time.sleep(5)


#table dynamic data extract

table=driver.find_element(By.XPATH,"//table[@id='taskTable']")
headers=[h.text for h in table.find_elements(By.XPATH,"//thead/tr/th")]
rows=table.find_elements(By.XPATH,"//tbody/tr")

for row in rows:
    cells=row.find_elements(By.TAG_NAME,"td")
    for header , cell in zip(headers,cells):
        print(f"{header}:{cell.text}")
    print("-" * 30)