from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/iframe")

driver.switch_to.frame("mce_0_ifr")
#driver.find_element(By.ID,"tinymce").clear()
driver.execute_script("document.getElementById('tinymce')")
driver.find_element(By.ID,"tinymce").send_keys("Mayur JOshi")
driver.switch_to.default_content()
print(driver.find_element(By.XPATH,"//h3").text)

