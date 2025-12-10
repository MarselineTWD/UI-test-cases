from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demoqa.com/", timeout=30000)
    print("Страница открылась, url:", page.url)
    input("Нажми Enter, чтобы закрыть...")
    browser.close()
