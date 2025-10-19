from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import time

# Initialize driver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://example.com/mobilenumbers")  # replace with actual webpage
time.sleep(3)

# Step 1: Fetch all numbers (assuming they are inside <td> or <span> tags)
numbers = driver.find_elements(By.XPATH, "//td[@class='mobile']")  # adjust locator

# Step 2: Define validation pattern
pattern = re.compile(r"^[6-9]\d{9}$")
#pattern = re.compile(r"^(\+91[-\s]?)?[6-9]\d{9}$")

valid_count = 0
invalid_count = 0

# Step 3: Validate each number
for num_element in numbers:
    number = num_element.text.strip()

    if pattern.match(number):
        print(f"✅ Valid: {number}")
        valid_count += 1
    else:
        print(f"❌ Invalid: {number}")
        invalid_count += 1

# Step 4: Print summary
print(f"\nTotal Valid Numbers: {valid_count}")
print(f"Total Invalid Numbers: {invalid_count}")

driver.quit()



#without using regex
def is_valid_mobile(number):
    # Step 1: Remove spaces
    number = number.strip()

    # Step 2: Check if it contains only digits
    if not number.isdigit():
        return False

    # Step 3: Check length = 10
    if len(number) != 10:
        return False

    # Step 4: Check first digit
    if number[0] not in ['6', '7', '8', '9']:
        return False

    # ✅ If all checks passed
    return True
# Test
numbers = ["9876543210", "1234567890", "6789012345", "98765abc10", "987654321"]
for n in numbers:
    if is_valid_mobile(n):
        print(f"✅ Valid: {n}")
    else:
        print(f"❌ Invalid: {n}")

