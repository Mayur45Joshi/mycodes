import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc

# options = Options()
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)

driver = uc.Chrome

driver.get("https://www.makemytrip.com/")
driver.maximize_window()
time.sleep(5)

try:
    driver.find_element(By.XPATH, "//span[@class='commonModal__close']").click()
except:
    pass

driver.find_element(By.ID, "fromCity").click()
from_input = driver.find_element(By.XPATH, "//input[@placeholder='From']")
from_input.send_keys("Mumbai")
driver.find_element(By.XPATH,"//ul[@role='listbox']/li[1]").click()
time.sleep(5)

driver.find_element(By.XPATH,"//input[@id='toCity']").click()
driver.find_element(By.XPATH, "//input[@placeholder='To' and @type='text']").send_keys("New Delhi")
time.sleep(5)
driver.find_element(By.XPATH,"//span[contains(text(),'New Delhi')]").click()
time.sleep(5)
driver.find_element(By.XPATH,"(//div[contains(@class,'dateInnerCell')])[29]").click()
time.sleep(5)
driver.find_element(By.XPATH, "//a[text()='Search']").click()
#time.sleep(10)
wait = WebDriverWait(driver, 20)

msg = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[contains(@class,'journey-title')]/span")))
#driver.execute_script("arguments[0].click();", search_btn)
#msg=driver.find_element(By.XPATH,"//p[contains(@class,'journey-title')]/span").text
print(msg.text)