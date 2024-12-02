from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.CLASS_NAME,"blinkingText").click()

Windows = driver.window_handles
driver.switch_to.window(Windows[1])

#print(driver.find_element(By.CLASS_NAME,"im-para red").text)
msg = driver.find_element(By.LINK_TEXT,"mentor@rahulshettyacademy.com").text

driver.switch_to.window(Windows[0])

driver.find_element(By.ID,"username").send_keys(msg)
driver.find_element(By.XPATH,"//input[@id='username']").send_keys("L23456")

driver.find_element(By.ID,"terms").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[@class= 'alert alert-danger col-md-12' ]")))

print(driver.find_element(By.XPATH,"//div[@class= 'alert alert-danger col-md-12' ]").text)