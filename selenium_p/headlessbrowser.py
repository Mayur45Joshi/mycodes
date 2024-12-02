# from selenium_p import webdriver
#
#
# def headless_chrome():
#     #driver = webdriver.Chrome()
#     ops = webdriver.ChromeOptions()
#     ops.headless = True
#     print(ops)
#     driver = webdriver.Chrome(options=ops)
#     return driver
#
# driver = headless_chrome()
# driver.get("https://www.facebook.com/")
# print(driver.title)
# print(driver.current_url)
# driver.close()




#############################################################

from selenium.webdriver import Chrome, ChromeOptions

def headless_chrome():
    ops = ChromeOptions()
    ops.add_argument('--headless')
    ops.add_argument('--disable-gpu')
    driver = Chrome(options=ops)
    return driver

driver = headless_chrome()
driver.get("https://www.facebook.com/")
print(driver.title)
print(driver.current_url)
driver.close()