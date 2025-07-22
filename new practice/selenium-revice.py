import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.XPATH,"//input[@value='radio1']").click()
driver.find_element(By.XPATH,"//input[@id='autocomplete']").send_keys("Mayur")
dropdwon=driver.find_element(By.ID,"dropdown-class-example")
dd=Select(dropdwon)
dd.select_by_visible_text('Option3')
# all_opt=dd.options
# print(all_opt)

checkboxs=driver.find_elements(By.XPATH,"//div[@id='checkbox-example']//input")
for checkbox in checkboxs:
    val=checkbox.get_attribute("value")
    if val == 'option2':
        checkbox.click()


#driver.find_element(By.ID,"openwindow").click()
windows=driver.window_handles
for window in windows:
    driver.find_element(By.ID, "openwindow").click()
    driver.switch_to.window(window)
    print(driver.title)
    #driver.find_element(By.ID, "openwindow").click()
    print(driver.title)
    time.sleep(5)
    driver.find_element(By.XPATH,"(//a[@class='main-btn'])[1]").click()
    #driver.find_element(By.LINK_TEXT,"Courses")
#(//div[@class='cont']//p)[1]

time.sleep(5)

