from playwright.sync_api import sync_playwright

user_name = input("Enter username: ")
pwd = input("Enter password: ")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # set headless=True if you don't want browser UI
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/login")

    # Assertion for URL
    assert page.url == "https://the-internet.herokuapp.com/login"

    # Enter username and password
    page.fill("#username", user_name)
    page.fill("#password", pwd)

    # Click login button
    page.click("button[type='submit']")

    # Get the flash message
    message = page.text_content("#flash").strip()

    if "You logged into a secure area!" in message:
        print("Login success:", message)
    elif "Your username is invalid!" in message:
        print("Login failed:", message)
    else:
        print("Wrong message:", message)

    browser.close()
