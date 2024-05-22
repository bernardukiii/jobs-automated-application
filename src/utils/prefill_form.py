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
        

# As different forms have different ways of handling elements, this will try a few options but might not coincide and fail

        # Try filling in the name
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
        
        # Try filling in the surname
        try:
            page.get_by_label("Last Name*").click()
            page.get_by_label("Last Name*").fill(user_info["surname"])

            if TimeoutError:
                page.locator("[id=\"applicant_lead_attributes\\[last_name\\]\"]").click()
                page.locator("[id=\"applicant_lead_attributes\\[last_name\\]\"]").fill(user_info["surname"])
            elif TimeoutError:
                page.get_by_label("Last Name *").click()
                page.get_by_label("Last Name *").fill(user_info["surname"])
            elif TimeoutError:
                page.get_by_placeholder("Apellidos").click()
                page.get_by_placeholder("Apellidos").fill(user_info["surname"])
            elif TimeoutError:
                page.get_by_placeholder("Last Name").click()
                page.get_by_placeholder("Last Name").fill(user_info["surname"])
        except TimeoutError:
            print("Could not fill in 'SURNAME'")

        # Try filling in the email
        try:
            page.get_by_placeholder("Email").click()
            page.get_by_placeholder("Email").fill(user_info["email"])

            if TimeoutError:
                page.get_by_label("Email✱").click()
                page.get_by_label("Email✱").fill(user_info["email"])
            elif TimeoutError:
                page.get_by_label("Email*").click()
                page.get_by_label("Email*").fill(user_info["email"])
            elif TimeoutError:
                page.get_by_label("Email *").click()
                page.get_by_label("Email *").fill(user_info["email"])
            elif TimeoutError:
                page.locator("[id=\"applicant_lead_attributes\\[email\\]\"]").click()
                page.locator("[id=\"applicant_lead_attributes\\[email\\]\"]").fill(user_info["email"])
            elif TimeoutError:
                page.get_by_placeholder("hello@example.com...").click()
                page.get_by_placeholder("hello@example.com...").fill(user_info["email"])
            elif TimeoutError:
                page.locator("input[name=\"personal_info\\.email\"]").click()
                page.locator("input[name=\"personal_info\\.email\"]").fill(user_info["email"])
        except TimeoutError:
            print("Could not fill in 'EMAIL'")
 

        # # Close the browser after the test
        # browser.close()
