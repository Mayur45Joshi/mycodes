import time

import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from selenium_p import excelUtil


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.moneycontrol.com/fixed-income/calculator/hsbc/fixed-deposit-calculator-ZZZ-BHS001.html?classic=true")
driver.maximize_window()
file="D:\STUDY AUTO\Book1.xlsx"

rows=excelUtil.getRowCount(file,"Sheet1")

for r in range(2,rows+1):
    prin = excelUtil.readData(file,"Sheet1",r,1)
    roi = excelUtil.readData(file,"Sheet1",r,2)
    per1 = excelUtil.readData(file,"Sheet1",r,3)
    per2 = excelUtil.readData(file, "Sheet1", r, 4)
    fre = excelUtil.readData(file,"Sheet1",r,5)
    exp_mval = excelUtil.readData(file,"Sheet1",r,6)

    #passing data in application

    driver.find_element(By.XPATH,"//input[@id='principal']").send_keys(prin)
    driver.find_element(By.XPATH,"//input[@id='interest']").send_keys(roi)
    driver.find_element(By.XPATH,"//input[@id='tenure']").send_keys(per1)
    perioddrop = Select(driver.find_element(By.XPATH,"//select[@id='tenurePeriod']"))
    perioddrop.select_by_visible_text(per2)

    fredrop = Select(driver.find_element(By.XPATH,"//select[@id='frequency']"))
    fredrop.select_by_visible_text(fre)

    driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[1]/img").click()

    Act_value = driver.find_element(By.XPATH,"//span[@id='resp_matval']/strong").text

    #validation

    if float(Act_value) == float(exp_mval):
        print("test passed")
        excelUtil.writeData(file,"Sheet1",r,8,"Pass")
        excelUtil.fillGreenColor(file,"Sheet1",r,8)


    else:
        print("test failed")
        excelUtil.writeData(file,"Sheet1",r,8,"Failed")
        excelUtil.fillRedColor(file,"Sheet1",r,8)

    driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[2]/img").click()
    time.sleep(10)

driver.close()

