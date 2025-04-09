import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
print(driver.current_url)
print(driver.title)


#driver.find_element(By.CSS_SELECTOR, "input[class='form-control ng-pristine ng-invalid ng-touched']").send_keys("khargone")

driver.find_element(By.NAME, "email").send_keys("mj@email.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("mj124")
driver.find_element(By.ID, "exampleCheck1").click()

driver.find_element(By.CSS_SELECTOR , "#inlineRadio1").click()
#driver.find_element(By.CSS_SELECTOR, "input[class='form-control ng-pristine ng-invalid ng-touched']").send_keys("khargone")

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("heelo")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()

#static dropwon by using Select class methods

dropdown =Select(driver.find_element(By.CSS_SELECTOR, "#exampleFormControlSelect1"))
dropdown.select_by_index(1)
#dropdown.select_by_value()
all_options=dropdown.options
print("all option ", len(all_options))
# for opt in all_options:
#     print(opt.text)

#selecting option from dropdown without ussing builtin methds
for opt in all_options:
    if opt.text == "Male":
        opt.click()

time.sleep(2)
dropdown.select_by_visible_text("Male")




driver.find_element(By.XPATH, "//input[@type= 'submit' ]") .click()

#to print any message available on UI
msg = driver.find_element(By.CLASS_NAME, "alert").text
print(msg)

assert "Success" in msg

time.sleep(2)