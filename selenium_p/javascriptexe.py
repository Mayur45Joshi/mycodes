from selenium import webdriver

#driver = webdriver.Chrome()
ch_options = webdriver.ChromeOptions()
#ch_options.add_argument("headless")

ch_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(options = ch_options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")

driver.get_screenshot_as_file("mj.png")