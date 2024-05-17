import re
from playwright.sync_api import sync_playwright, Page


def prefill_form(url: str):    
    with sync_playwright() as p:
        # Launch Chromium browser with headless set to False
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Now navigate to the URL
        page.goto(url)
                
        # Close the browser after the test
        browser.close()
