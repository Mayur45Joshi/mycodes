import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options = chrome_option)
#chrome_option.add_experimental_option("detach", True)

driver.implicitly_wait(10)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
#  xpath=  //a[contains(text(), 'Shop')]
products = driver.find_elements(By.XPATH,"//div[@class='card h-100']")

for product in products:
    product_name = driver.find_element(By.XPATH,"//div[@class='card h-100']/div/h4/a").text
    if product_name == "Blackberry":
        product.find_element(By.XPATH,"/div/button").click()

driver.find_element(By.CSS_SELECTOR,"a[class*= 'btn' ]").click()

driver.find_element(By.CSS_SELECTOR,"button[class*= 'btn-success' ]").click()
driver.find_element(By.XPATH,"//input[@id='country']").send_keys("Ind")

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()
successtest = driver.find_element(By.CSS_SELECTOR,"div[class*='alert-success']").text
assert "Success! Thank you!"  in  successtest

