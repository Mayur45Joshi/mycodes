from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup Chrome options
options = Options()
options.add_argument('--headless')  # Comment this out to see the browser
driver = webdriver.Chrome(options=options)

# Step 1: Go to ICC Homepage
driver.get("https://www.icc-cricket.com/")

# Step 2: Navigate directly to the ODI team rankings page
driver.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi")

# Step 3: Wait for table to load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "si-table-row"))
)

# Step 4: Extract all rows
rows = driver.find_elements(By.CSS_SELECTOR, "div.si-table-row")

print("Rank | Team | Matches | Points | Rating")
for row in rows:
    try:
        cols = row.find_elements(By.CSS_SELECTOR, "div")
        if len(cols) >= 5:
            rank = cols[0].text
            team = cols[1].text
            matches = cols[2].text
            points = cols[3].text
            rating = cols[4].text
            print(f"{rank} | {team} | {matches} | {points} | {rating}")
    except Exception as e:
        print("Error reading row:", e)

driver.quit()