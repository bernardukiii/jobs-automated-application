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
        page.get_by_label("First Name *").click()
        page.get_by_label("First Name *").fill("ber")
        page.get_by_label("Last Name *").click()
        page.get_by_label("Last Name *").fill("ferr")
        page.get_by_label("Email *").click()
        page.get_by_label("Email *").fill("email")
        page.get_by_label("Phone").click()
        page.get_by_label("Phone").fill("123")
        page.get_by_label("Website").click()
        page.get_by_label("Website").fill("portfolio")
        page.get_by_label("LinkedIn Profile").click()
        page.get_by_label("LinkedIn Profile").fill("linkedin")
        page.get_by_label("Github").click()
        page.get_by_label("Github").fill("github")
        # Sample seven
        page.get_by_label("Full name✱").click()
        page.get_by_label("Full name✱").fill("ber")
        page.get_by_label("Email✱").click()
        page.get_by_label("Email✱").fill("ber")
        page.get_by_label("Phone ✱").click()
        page.get_by_label("Phone ✱").fill("123")
        page.get_by_label("LinkedIn URL").click()
        page.get_by_label("LinkedIn URL").fill("link")
        page.get_by_label("Portfolio URL").click()
        page.get_by_label("Portfolio URL").fill("link")
        page.get_by_label("Other website").click()
        page.get_by_label("Other website").fill("link")
        # Sample eight
        page.frame_locator("iframe[title=\"Greenhouse Job Board\"]").get_by_label("First Name *").click()
        page.frame_locator("iframe[title=\"Greenhouse Job Board\"]").get_by_label("Last Name *").click()
        page.frame_locator("iframe[title=\"Greenhouse Job Board\"]").get_by_label("Email *").click()
        page.frame_locator("iframe[title=\"Greenhouse Job Board\"]").get_by_label("Phone").click()
        page.frame_locator("iframe[title=\"Greenhouse Job Board\"]").get_by_label("LinkedIn Profile").click()
        page.frame_locator("iframe[title=\"Greenhouse Job Board\"]").get_by_label("Website").click()
        page.frame_locator("iframe[title=\"Greenhouse Job Board\"]").get_by_label("LinkedIn Profile").fill("g")
        # Sample nine
        page.get_by_placeholder("Nombre").click()
        page.get_by_placeholder("Nombre").fill("name")
        page.get_by_placeholder("Apellidos").click()
        page.get_by_placeholder("Apellidos").fill("be")
        page.get_by_placeholder("Email").click()
        page.get_by_placeholder("Email").fill("em")
        page.get_by_placeholder("Teléfono").click()
        page.get_by_placeholder("Teléfono").fill("123")
        page.get_by_placeholder("Perfil de Linkedin").click()
        page.get_by_placeholder("Perfil de Linkedin").fill("link")
        # Sample ten
        page.get_by_placeholder("First Name").click()
        page.get_by_placeholder("First Name").fill("dfg")
        page.get_by_placeholder("Last Name").click()
        page.get_by_placeholder("Last Name").fill("fg")
        page.locator("input[name=\"personal_info\\.email\"]").click()
        page.locator("input[name=\"personal_info\\.email\"]").fill("fg")
        page.locator("input[name=\"personal_info\\.linkedin_profile\"]").click()
        page.locator("input[name=\"personal_info\\.linkedin_profile\"]").fill("fg")


        # # Close the browser after the test
        # browser.close()
