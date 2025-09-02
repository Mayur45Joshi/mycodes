# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# # Create Chrome options
# options = Options()
#
# # Example: run in headless mode if needed
# # options.add_argument("--headless")
#
# # Connect to Selenium Grid
# driver = webdriver.Remote(
#     command_executor="http://localhost:4444/wd/hub",
#     options=options
# )
#
# # Run a simple test
# driver.get("https://www.google.com")
# print("Page Title is:", driver.title)
#
# driver.quit()




from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Create Chrome Options
options = Options()
options.add_argument("--start-maximized")

# Connect to Selenium Grid Hub
driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub",
    options=options
)

# Test Case: Open Google and Search
driver.get("https://www.google.com")
print("Title is:", driver.title)

search_box = driver.find_element("name", "q")
search_box.send_keys("Selenium Grid Python")
search_box.submit()

time.sleep(3)  # just to see the result

print("New Title is:", driver.title)
driver.quit()
