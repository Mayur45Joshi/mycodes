from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch Chromium browser
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com")

    # Get page title
    print("Playwright Title:", page.title())

    browser.close()
