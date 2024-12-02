import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.deadlinkcity.com/")

alllinks=driver.find_elements(By.XPATH,"//a[@href]")

broken_links=0

for link in alllinks:
    url=link.get_attribute('href')
    try:
        res=requests.head(url)
        if res.status_code >= 400:
            print(f"Broken link: {url}")
            broken_links += 1
    except:
        None

    # if res.status_code>=400:
    #     print(url + " is broken link")

    else:
        print(url + "is Ok")

print(f"Total broken links: {broken_links}")


