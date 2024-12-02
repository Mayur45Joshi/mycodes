from selenium import webdriver

chrome_option = webdriver.ChromeOptions()
#driver = webdriver.Chrome(options = chrome_option)

chrome_option.add_argument("--start-maximized")
chrome_option.add_argument('--headless')
chrome_option.add_argument('--disable-gpu')
#chrome_option.add_argument("headless")
chrome_option.add_argument("--ignore-certificate-errors")
chrome_option.add_argument("--disable-notifications")
driver = webdriver.Chrome(options = chrome_option)

driver.get("https://www.amazon.in/ref=nav_logo")
print(driver.title)


#webdriver.ChromeOptions().add_argument("")