import flag
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

# sliders >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
# driver.maximize_window()
#
# min_slider = driver.find_element(By.XPATH,"//span[1]")
# max_slider = driver.find_element(By.XPATH,"//span[2]")
#
# print("location of slider before moving........")
#
# print(min_slider.location)
# print(max_slider.location)
#
# act = ActionChains(driver)
# act.drag_and_drop_by_offset(min_slider,100,0).perform()
#
# act.drag_and_drop_by_offset(max_slider,-39,0).perform()
#
# print("location of slider after moving .......")
#
# print(min_slider.location)
# print(max_slider.location)



#>>>>>>>>>>>>>>>>>SCROLL>>>>>>>>>>>>>>>>>>>>>

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

#>>>>>scroll down by pixel  way  1

# driver.execute_script("window.scrollBy(0,3000)","")
# value = driver.execute_script("return window.pageYOffset;")
# print("Number of pixel moved:",value)

#>>>>>>scroll down the page till the page visible   way 2   >>>>>>>>>>>>>>>

# Flag = driver.find_element(By.XPATH,"//img[@alt='Flag of India']")
# driver.execute_script("arguments[0].scrollIntoView();",flag)
# value=driver.execute_script("return window.pageYOffset;")
# print("Number of pixels moved:",value)


# scroll down page till height

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:",value)


# scroll upto stating position >>>>>>>>>>>>>>>>>>

driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:",value)
