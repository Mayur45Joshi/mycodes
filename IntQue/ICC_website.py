import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://www.icc-cricket.com/")
time.sleep(5)
rows=len(driver.find_elements(By.XPATH,"(//div[@class='si-table-head odi'])[1]/following::div[1]/div[@class='si-table-row']"))
cols=len(driver.find_elements(By.XPATH,"(//div[@class='si-table-head odi'])[1]/following::div[1]/div[@class='si-table-row'][1]/div//span[@class='si-text' or @class='si-country']"))
print(rows)
print(cols)

for r in range(1,rows+1):
    for c in range(1,cols+1):
        values=driver.find_element(By.XPATH,"(//div[@class='si-table-head odi'])[1]/following::div[1]/div[@class='si-table-row']["+str(r)+"]//div//span[@class='si-text' or @class='si-country']["+str(c)+"]").text
        print(values)






