import time

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.XPATH, "//input[@type='search']").send_keys("ca")
time.sleep(5)
counts = driver.find_elements(By.XPATH, "//div[@class='products']/div")

print(len(counts))

for count in counts:
    driver.find_element(By.XPATH, "//button[contains(text(), 'ADD TO CART')]").click()
    #count.find_element(By.XPATH,"div/button")
    #count.click()
    #break

driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH, "//button[contains(text(),'PROCEED TO CHECKOUT')]").click()
#time.sleep(2)

#sum validation'

prices = driver.find_elements(By.XPATH,"//tr //td[5] //p ")
sum=0
for price in prices:
    sum= sum + int(price.text)

print(sum)

totalamount =int(driver.find_element(By.CLASS_NAME,"totAmt").text)

discountamount = int(driver.find_element(By.CLASS_NAME,"discountAmt").text)

assert totalamount == sum

driver.find_element(By.CLASS_NAME,"promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()

#explicit wait

wait = WebDriverWait(driver,10)
#wait = WebDriverWait(driver,10, ignored_exceptions=[NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException,Exception])
#wait = WebDriverWait(driver,10, poll_frequency=2, ignored_exceptions=[NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException,Exception])

wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"promoInfo")))

print(driver.find_element(By.CLASS_NAME,"promoInfo").text)

assert sum > discountamount

