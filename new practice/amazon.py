import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
# driver.get("https://www.amazon.in/ref=nav_logo")
# links=driver.find_elements(By.XPATH,"//div[@id='nav-xshop']//li//a")
# for link in links:
#     print(link.text)

# for i in range(len(links)):
#     driver.get("https://www.amazon.in/ref=nav_logo")
#     nav_link=driver.find_elements(By.XPATH,"//div[@id='nav-xshop']//li//a")
#     nav_link[i].click()
#     time.sleep(5)


driver.get("https://www.amazon.in/ref=nav_logo")
driver.find_element(By.XPATH,"//input[@role='searchbox']").send_keys("Iphone 15")
wait=WebDriverWait(driver,10)
items=wait.until(EC.visibility_of_all_elements_located((By.XPATH,"//div[@class='left-pane-results-container']/div/div/div[@aria-label]")))
for item in items:
    res=item.get_attribute("aria-label")
    if res and res.lower()=="iphone 15 128+gb":
        item.click()
        break
time.sleep(5)

driver.maximize_window()

# rat=driver.find_element(By.XPATH,"//span[contains(text(),'Apple iPhone 15 (128 GB) - Blue')]/following::div[1]//i[@data-cy='reviews-ratings-slot']")
# #driver.execute_script("arguments[0].scrollIntoView(true);", rat)
# wait.until(EC.presence_of_element_located((By.XPATH,"//span[contains(text(),'Apple iPhone 15 (128 GB) - Blue')]/following::div[1]//i[@data-cy='reviews-ratings-slot']")))
# action=ActionChains(driver)
# action.move_to_element(rat).perform()
# time.sleep(5)


action=ActionChains(driver)
stars=driver.find_elements(By.XPATH,"//i[contains(@class,'a-icon-star')]")
for index,star in enumerate(stars[:3]):             #first 3 mobiles
    print(f"\n Mobile {index+1} rating breakdown:")
    action.move_to_element(star).perform()
    star.click()

    try:
        wait=WebDriverWait(driver,10)
        breakdown=wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class,'a-popover-content')]")))
        print(breakdown.text.strip())

    except:
        print("No breakdown")
    time.sleep(5)

