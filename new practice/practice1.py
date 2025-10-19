# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
# driver.get("https://cosmocode.io/automation-practice-webtable/")
# countries=driver.find_elements(By.XPATH,"//table[@id='countries']//tr/td/strong")
# for country in countries:
#     print(country.text)
#
#
#

#
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def get_capital_and_language(driver, country_name):
    """
    Given a webdriver and a country name,
    returns (capital, primary_language) or (None, None) if not found.
    """
    # We assume table rows are in <tr> elements under a <table> or container
    # Inspecting the page, the table has country, capital(s), currency, primary language(s) columns. :contentReference[oaicite:1]{index=1}

    # Find all table rows (skip header)
    rows = driver.find_elements(By.XPATH, "//table[@id='countries']/tbody/tr")  # adjust XPath as per actual table in page

    for row in rows:  # skip header row
        # Get the country cell text (first column)
        country_cell = row.find_element(By.XPATH, "./td[2]").text.strip()
        if country_cell.lower() == country_name.lower():
            # Found the correct row
            capital = row.find_element(By.XPATH, "./td[3]").text.strip()
            primary_lang = row.find_element(By.XPATH, "./td[5]").text.strip()
            return capital, primary_lang

    # If not found
    return None, None


def test_country():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://cosmocode.io/automation-practice-webtable/")
    time.sleep(5)  # wait for table to load (better use WebDriverWait in real tests)

    # Test for country “India”
    country = "India"
    capital, lang = get_capital_and_language(driver, country)
    if capital and lang:
        print(f"The Capital of {country} is {capital} and the primary language(s) is {lang}")
    else:
        print(f"{country} not found in the table.")

    # Test for another country
    country2 = "Australia"
    capital2, lang2 = get_capital_and_language(driver, country2)
    if capital2 and lang2:
        print(f"The Capital of {country2} is {capital2} and the primary language(s) is {lang2}")
    else:
        print(f"{country2} not found in the table.")

    driver.quit()


if __name__ == "__main__":
    test_country()



#getting UN and PWD from properties file
#
# [credentials]
# username = admin_user
# password = secure_pass123

# import configparser
#
# def get_credentials(file_path):
#     config = configparser.ConfigParser()
#     config.read(file_path)
#     username = config.get("credentials", "username")
#     password = config.get("credentials", "password")
#     return username, password
#
# # Example usage
# u, p = get_credentials("config.properties")
# print("Username:", u)
# print("Password:", p)
