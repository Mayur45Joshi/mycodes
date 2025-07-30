import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")

#provide upload file path

# file_path=os.path.abspath("D:\\STUDY AUTO\\files\\new 2.txt")
# driver.find_element(By.ID,"singleFileInput").send_keys(file_path)
# driver.find_element(By.XPATH,"//button[@type='submit']").click()
# status=driver.find_element(By.XPATH,"//p[@id='singleFileStatus']").text
# print(status)


#multiple file upload

file1=os.path.abspath(r"D:\STUDY AUTO\files\new 2.txt")
file2=os.path.abspath(r"D:\STUDY AUTO\files\POM.txt")
combined_file=file1 + "\n" + file2
driver.find_element(By.ID,"multipleFilesInput").send_keys(combined_file)
time.sleep(5)
driver.find_element(By.XPATH,"//button[@type='submit']").click()
status=driver.find_element(By.XPATH,"//p[@id='multipleFilesStatus']").text
print(status)

