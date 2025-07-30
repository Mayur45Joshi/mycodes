import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


options = Options()
options.add_experimental_option("prefs", {
    "download.default_directory": "/path/to/download/directory",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True
})
driver=webdriver.Chrome(options)
driver.get("https://pypi.org/project/selenium/#files")
driver.find_element(By.PARTIAL_LINK_TEXT,"selenium-4.34.2.tar.gz").click()
time.sleep(5)

