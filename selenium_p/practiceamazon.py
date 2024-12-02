from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://www.amazon.in/ref=nav_logo")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']").send_keys("iphone 15")
driver.find_element(By.XPATH,"//input[@id='nav-search-submit-button']").click()
driver.find_element(By.XPATH,"//span[contains(text(), 'Apple iPhone 15 (128 GB) - Black')]").click()

openwin = driver.window_handles
driver.switch_to.window(openwin[1])
#driver.find_element(By.XPATH,"//div[@id='itembox-Partner']").click()

#driver.find_element(By.XPATH,"//div/span/a[@xpath='1']").click()

#driver.find_element(By.XPATH,"//p[text()='256 GB']").click()
#driver.find_element(By.XPATH,"//span[@id='submit.add-to-cart']").click()




wait = WebDriverWait(driver,30)
wait.until(expected_conditions.presence_of_element_located((By.ID,"submit.add-to-cart-announce")))
#wait.until(expected_conditions.presence_of_element_located((By.NAME,"submit.add-to-cart")))
# driver.find_element(By.XPATH,"(//span[@id='submit.add-to-cart-announce'])[2]").click()

driver.find_element(By.CSS_SELECTOR,"#add-to-cart-button").click()





