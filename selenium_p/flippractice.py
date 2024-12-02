# import time
#
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.flipkart.com/?redirectFrom=logout")
# time.sleep(10)
# actions = ActionChains(driver)
# #mouse hover over login
# ele=driver.find_element(By.XPATH,"//div[@class='H6-NpN _3N4_BX']/a")
# actions.move_to_element(ele).perform()
# time.sleep(10)

#my_pro=driver.find_element(By.XPATH,"//a[@title='My Profile']").click()
#print(my_pro)


# #hovering and getting text from link
# ele2 = driver.find_element(By.XPATH,"(//span[.='Electronics'])[1]")
# actions.move_to_element(ele2).perform()
# txt=driver.find_element(By.XPATH,"//a[.='Electronics GST Store']").get_attribute("text")
# print(txt)
# time.sleep(5)

# #getting all elements from particular ssection
# ele2 = driver.find_element(By.XPATH,"(//span[.='Electronics'])[1]")
# actions.move_to_element(ele2).perform()
# elems = driver.find_elements(By.XPATH,"//div[@class='_16rZTH']//a")
# for ele in elems:
#     ele_txt=ele.get_attribute("text")
#     print(ele_txt)



# #getting all elements from hower to another hower list
# ele2 = driver.find_element(By.XPATH,"(//span[.='Electronics'])[1]")
# actions.move_to_element(ele2).perform()
# ele3 = driver.find_element(By.XPATH,"//a[.='Audio']")
# actions.move_to_element(ele3).perform()
# time.sleep(5)
# audio_ele = driver.find_elements(By.XPATH,"//div[@class='_31z7R_']//a")
# for ele in audio_ele:
#     txt=ele.get_attribute("text")
#     print(txt)























