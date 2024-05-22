import re
from playwright.sync_api import sync_playwright, Page


def prefill_form(user_info: dict):
    print('inside play', user_info)  
    with sync_playwright() as p:
        # Launch Chromium browser with headless set to False
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Now navigate to the URL
        page.goto(user_info["formURL"])
        
        # Try filling in the name
        # As different forms have different ways of handling elements, this will try a few options but might not coincide and fail
        try:
            page.get_by_label("Name").click()
            page.get_by_label("Name").fill(user_info["name"])

            if TimeoutError:
                page.get_by_label("First Name*").click()
                page.get_by_label("First Name*").fill(user_info["name"])
            elif TimeoutError:
                page.get_by_label("First Name *").click()
                page.get_by_label("First Name *").fill(user_info["name"])
            elif TimeoutError:
                page.get_by_label("Full name✱").click()
                page.get_by_label("Full name✱").fill(user_info["name"])
            elif TimeoutError:
                page.get_by_placeholder("Nombre").click()
                page.get_by_placeholder("Nombre").fill(user_info["name"])
            elif TimeoutError:
                page.get_by_placeholder("First Name").click()
                page.get_by_placeholder("First Name").fill(user_info["name"])    
        except TimeoutError:
            print("Could not fill in 'NAME'")
        


        # # Close the browser after the test
        # browser.close()
