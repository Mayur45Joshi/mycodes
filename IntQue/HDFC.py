from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.hdfcbank.com/personal/useful-links/security")
langs=driver.find_elements(By.XPATH,"(//div[@class='be-ex-content'])[1]/p/a")
for lang in langs:
    print(lang.text.strip())