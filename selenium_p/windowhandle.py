import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT,"Click Here").click()

windows = driver.window_handles
driver.switch_to.window(windows[1])



print(driver.find_element(By.TAG_NAME,"h3").text)
driver.switch_to.window(windows[0])

#assert "Opening a new window" == driver.find_element(By.TAG_NAME,"h3").text

print(driver.find_element(By.TAG_NAME,"h3").text)



#pytest annotations

# @pytest.mark.skip("Skipping this test")
# def test_example():
#     driver = webdriver.Chrome()
#     driver.get("https://www.google.co.in/")
#     #assert driver.title == "Expected Title"