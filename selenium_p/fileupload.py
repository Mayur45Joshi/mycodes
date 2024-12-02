import os

from selenium import webdriver
from selenium.webdriver.common.by import By
#from flask import request


driver = webdriver.Chrome()
#driver.implicitly_wait(10)
driver.get("https://ps.uci.edu/~franklin/doc/file_upload.html")
file_input = driver.find_element(By.NAME,"userfile")
file_path = "D:\\STUDY AUTO\\Selenium with python\\Delottie interview Question.rtf"
file_input.send_keys(file_path)
print(file_path)
# flask framework to check file upload success

# if request.files['file_input']:
#     print("file uploaded")
# else:
#     print("no file upload")

def check_file_uploaded(file_path):
    if os.path.isfile(file_path):
        print("File uploaded")
    else:
        print("No file uploaded")

check_file_uploaded(file_path)