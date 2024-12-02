import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

driver.find_element(By.ID,"dob").click()
sel_month = Select(driver.find_element(By.XPATH,"//select[@data-handler='selectMonth']"))
sel_month.select_by_visible_text("May")

sel_year = Select(driver.find_element(By.XPATH,"//select[@data-handler='selectYear']"))
sel_year.select_by_visible_text("1994")

all_date = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for date in all_date:
    if date.text == "19":
        date.click()
        break