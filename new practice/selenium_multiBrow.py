# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# # Driver 1
# driver1 = webdriver.Chrome()
# driver1.get("https://example.com")
# time.sleep(1)
# print("Driver1 title:", driver1.title)
#
# # Driver 2
# driver2 = webdriver.Chrome()
# driver2.get("https://example.org")
# time.sleep(1)
# print("Driver2 title:", driver2.title)
#
# # Interact with each independently
# driver1.find_element(By.TAG_NAME, "h1")
# driver2.find_element(By.TAG_NAME, "h1")
#
# # cleanup
# driver1.quit()
# driver2.quit()
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# from concurrent.futures import ThreadPoolExecutor, as_completed
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# def worker_task(url):
#     driver = webdriver.Chrome()
#     try:
#         driver.get(url)
#         title = driver.title
#         return (url, title)
#     finally:
#         driver.quit()
#
# urls = ["https://example.com", "https://example.org", "https://python.org"]
#
# with ThreadPoolExecutor(max_workers=3) as ex:
#     futures = [ex.submit(worker_task, u) for u in urls]
#     for f in as_completed(futures):
#         print(f.result())


# driver=webdriver.Chrome()
# driver.get("https://www.amazon.in/")
# time.sleep(5)
# action=ActionChains(driver)
# signin=driver.find_element(By.XPATH,"//a[@data-nav-role='signin']")
# action.move_to_element(signin).perform()
# time.sleep(10)
# driver.find_element(By.XPATH,"//span[text()='Your Orders']").click()



