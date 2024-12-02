from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
#from flask import request

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.facebook.com/")
driver.maximize_window()

#cookies capture
cookies=driver.get_cookies()
print(len(cookies))

#detail of cookie print

# for c in cookies:
#     print(c)
#     print(c.get('name'),":",c.get('value'))

# driver.add_cookie({"name":"Mycookie","value":"Mayur"})
# cookies=driver.get_cookies()
# print(len(cookies))

#delete cookies

# driver.delete_cookie("Mycookie")
# cookies=driver.get_cookies()
# print(len(cookies))