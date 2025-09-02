import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc


driver=webdriver.Chrome()
#driver = uc.Chrome()
driver.get("https://www.makemytrip.com/")
driver.maximize_window()
driver.implicitly_wait(5)
#time.sleep(2)
#popup cclose
driver.find_element(By.XPATH,"//span[@data-cy='closeModal']").click()
#time.sleep(2)
driver.find_element(By.XPATH,"//span[@data-testid='travel-card-close']").click()
#clicking from
driver.find_element(By.ID,"fromCity").click()
#time.sleep(2)
#entering city name
driver.find_element(By.XPATH,"//input[@placeholder='From']").send_keys("Indore")
#time.sleep(2)
#Selecting from city
driver.find_element(By.XPATH,"//p[text()='Devi Ahilyabai Holkar International Airport']").click()
#time.sleep(2)

#clicking to city
driver.find_element(By.XPATH,"//input[@data-cy='toCity']").click()
#entereing to city name
driver.find_element(By.XPATH,"//input[@placeholder='To']").send_keys("Mumbai")
#selecting to city
driver.find_element(By.XPATH,"//p[text()='Chhatrapati Shivaji International Airport']").click()
#time.sleep(5)
#getting all elemts from calaneder
prices_ele=driver.find_elements(By.XPATH,"(//div[@class='DayPicker-Body'])[2]/div/div//p[@class=' todayPrice']")
pricedict={}
for el in prices_ele:
    price_txt=el.text.strip().replace(",","")
    if price_txt.isdigit():
        pricedict[int(price_txt)]=el

if pricedict:
    max_price=max(pricedict.keys())
    print(f"Clicking element with max price: {max_price}")
    driver.execute_script("window.scrollBy(0, 300);")
    time.sleep(5)
    pricedict[max_price].click()
else:
    print("No price found to click")

#time.sleep(5)
#clicking search button
driver.find_element(By.XPATH,"//a[text()='Search']").click()
#time.sleep(3)
