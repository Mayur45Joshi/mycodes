import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.switch_to.frame(0)
time.sleep(5)
#method 1  directly send the date

#driver.find_element(By.ID,"datepicker").send_keys("05/30/2024")

#method 2

year="2025"
month="May"
date="20"

driver.find_element(By.ID,"datepicker").click()

while True:
    mon=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yea=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text
    if mon == month and yea == year:
        break;

    else:
        driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[2]").click()  #next arroe
        time.sleep(2)

dates=driver.find_elements(By.XPATH,"//div[@id='ui-datepicker-div']//tbody/tr/td/a")
for ele in dates:
    if ele.text==date:
        time.sleep(2)
        ele.click()
        print(ele)
        break
