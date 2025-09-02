from selenium import webdriver

driver = webdriver.Chrome()

# Open any page (needed to access window object)
driver.get("https://www.google.com")

# Get screen resolution using JavaScript
width = driver.execute_script("return screen.width;")
height = driver.execute_script("return screen.height;")

print(f"Screen resolution: {width}x{height}")
window_size = driver.get_window_size()
print(window_size)  # {'width': ..., 'height': ...}

driver.quit()
