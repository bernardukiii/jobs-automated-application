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
        
        # Sample one
        page.get_by_label("Name").click()
        page.get_by_label("Name").fill("name")
        page.get_by_placeholder("hello@example.com...").click()
        page.get_by_placeholder("hello@example.com...").fill("email")
        page.get_by_label("LinkedIn URL").click()
        page.get_by_label("LinkedIn URL").fill("linkedinlink")
        # Sample two
        page.get_by_placeholder("Type here...").click()
        page.get_by_placeholder("Type here...").fill("ber")
        page.get_by_placeholder("hello@example.com...").click()
        page.get_by_placeholder("hello@example.com...").fill("ber")
        # Sample three
        page.get_by_label("Full name✱").click()
        page.get_by_label("Full name✱").fill("ber")
        page.get_by_label("Email✱").click()
        page.get_by_label("Email✱").fill("ber")
        page.get_by_label("Phone").click()
        page.get_by_label("Phone").fill("234")
        page.get_by_label("LinkedIn (Keep in mind that a").click()
        page.get_by_label("LinkedIn (Keep in mind that a").fill("linkedin")
        page.get_by_label("GitHub (If you are not a").click()
        page.get_by_label("GitHub (If you are not a").fill("github")
        page.get_by_label("Portfolio (If you are not a").click()
        page.get_by_label("Portfolio (If you are not a").fill("portfolio")
        # Sample four
        page.get_by_label("First Name*").click()
        page.get_by_label("First Name*").fill("ber")
        page.get_by_label("Last Name*").click()
        page.get_by_label("Last Name*").fill("ferr")
        page.get_by_label("Email*").click()
        page.get_by_label("Email*").fill("ema")
        page.get_by_role("textbox", name="City*").fill("b")
        page.get_by_role("textbox", name="City*").click()
        page.get_by_role("textbox", name="City*").fill("bsas")
        # Sample five
        page.locator("[id=\"applicant_lead_attributes\\[first_name\\]\"]").click()
        page.locator("[id=\"applicant_lead_attributes\\[first_name\\]\"]").fill("ber")
        page.locator("[id=\"applicant_lead_attributes\\[last_name\\]\"]").click()
        page.locator("[id=\"applicant_lead_attributes\\[last_name\\]\"]").fill("ferr")
        page.locator("[id=\"applicant_lead_attributes\\[email\\]\"]").click()
        page.locator("[id=\"applicant_lead_attributes\\[email\\]\"]").fill("ema")
        page.locator("[id=\"applicant_lead_attributes\\[phone\\]\"]").click()
        page.locator("[id=\"applicant_lead_attributes\\[phone\\]\"]").fill("123")
        page.get_by_placeholder("Hyperlink").click()
        page.get_by_placeholder("Hyperlink").fill("links")
        # Sample six
        



        # # Close the browser after the test
        # browser.close()
