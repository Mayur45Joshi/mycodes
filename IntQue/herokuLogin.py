from selenium import webdriver
from selenium.webdriver.common.by import By

user_name=input("enter username")
pwd=input("enter password")

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")
driver.find_element(By.ID,"username").send_keys(user_name)
driver.find_element(By.ID,"password").send_keys(pwd)
driver.find_element(By.XPATH,"//button[@type='submit']").click()
succ_msg=driver.find_element(By.ID,"flash")
message=succ_msg.text.strip()
if "You logged into a secure area!" in message:
    print("login success " ,message)

elif "Your username is invalid!" in message:
    print("login failed" , message)

else:
    print("wrong message" , message)








