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
 
        # Try filling in the number
        try:
            page.get_by_label("Phone").click()
            page.get_by_label("Phone").fill(user_info["number"])

            if TimeoutError:
                page.get_by_label("Phone ✱").click()
                page.get_by_label("Phone ✱").fill(user_info["number"])
            elif TimeoutError:
                page.get_by_placeholder("Teléfono").click()
                page.get_by_placeholder("Teléfono").fill(user_info["number"])
            elif TimeoutError:
                page.locator("[id=\"applicant_lead_attributes\\[phone\\]\"]").click()
                page.locator("[id=\"applicant_lead_attributes\\[phone\\]\"]").fill(user_info["number"])  
        except TimeoutError:
            print("Could not fill in 'PHONE NUMBER'")

        # Try filling in the Linkedin url
        try:
            page.get_by_label("LinkedIn URL").click()
            page.get_by_label("LinkedIn URL").fill(user_info["linkedin"])

            if TimeoutError:
                page.get_by_label("LinkedIn").click()
                page.get_by_label("LinkedIn").fill(user_info["linkedin"])
            elif TimeoutError:
                page.get_by_label("Linkedin").click()
                page.get_by_label("Linkedin").fill(user_info["linkedin"])
            elif TimeoutError:
                page.get_by_label("LinkedIn Profile").click()
                page.get_by_label("LinkedIn Profile").fill(user_info["linkedin"])
            elif TimeoutError:
                page.get_by_placeholder("Perfil de Linkedin").click()
                page.get_by_placeholder("Perfil de Linkedin").fill(user_info["linkedin"])
            elif TimeoutError:
                page.locator("input[name=\"personal_info\\.linkedin_profile\"]").click()
                page.locator("input[name=\"personal_info\\.linkedin_profile\"]").fill(user_info["linkedin"])
        except TimeoutError:
            print("Could not fill in 'EMAIL'")
 
        # Try filling in the Github url
        try:
            page.get_by_label("Github").click()
            page.get_by_label("Github").fill(user_info["github"])

            if TimeoutError:
                page.get_by_label("Github URL").click()
                page.get_by_label("Github URL").fill(user_info["github"])
            elif TimeoutError:
                page.get_by_label("Github Link").click()
                page.get_by_label("Github Link").fill(user_info["github"])
        except TimeoutError:
            print("Could not fill in 'EMAIL'")

        # Try filling in the portfolio url
        try:
            page.get_by_label("Portfolio").click()
            page.get_by_label("Portfolio").fill(user_info["portfolio"])

            if TimeoutError:
                page.get_by_label("Portfolio URL").click()
                page.get_by_label("Portfolio URL").fill(user_info["portfolio"])
            elif TimeoutError:
                page.get_by_label("Portfolio Link").click()
                page.get_by_label("Portfolio Link").fill(user_info["portfolio"])
            elif TimeoutError:
                page.get_by_label("Website").click()
                page.get_by_label("Website").fill(user_info["portfolio"])
            elif TimeoutError:
                page.get_by_label("Other website").click()
                page.get_by_label("Other website").fill(user_info["portfolio"])
        except TimeoutError:
            print("Could not fill in 'EMAIL'")
