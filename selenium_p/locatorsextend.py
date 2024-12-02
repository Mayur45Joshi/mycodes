import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# driver.get("https://rahulshettyacademy.com/client")
# driver.find_element(By.LINK_TEXT, "Forgot password?").click()
# driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
# driver.find_element(By.XPATH, "//form/div[2]/input").send_keys("mj@1234")
# driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("mj@1234")
# driver.find_element(By.XPATH, "//button[text()= 'Save New Password']").click()


# Dynamic dropdowns

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID, "autosuggest").send_keys("Ind")

time.sleep(2)

countries =driver.find_elements(By.XPATH, "//li[@class= 'ui-menu-item']/a")
print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break

#print(driver.find_element(By.ID, "autosuggest").text)
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"

time.sleep(2)


