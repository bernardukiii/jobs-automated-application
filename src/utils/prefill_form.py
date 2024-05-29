from playwright.sync_api import sync_playwright

def prefill_form(user_info: dict, formURL):
    print('inside play', user_info)  
    with sync_playwright() as p:
        # Launch Chromium browser with headless set to False
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Now navigate to the URL
        if formURL != '':
            try:
                page.goto(formURL)
            except Exception as e:
                print('URL not found (404)')
                # print(f"Error details: {e}")
        

# As different forms have different ways of handling elements, this will try a few options but might not coincide and fail

        def try_fill(methods):
            for method in methods:
                try:
                    method()
                    return
                except TimeoutError:
                    continue
            print(f"Could not fill in '{methods[0].__name__}'")

        # Methods for filling in the name
        Name_Methods = [
            lambda: page.get_by_label("Name").fill(user_info['name']),
            lambda: page.get_by_label("First Name*").fill(user_info['name']),
            lambda: page.get_by_label("First Name *").fill(user_info['name']),
            lambda: page.get_by_label("Full name✱").fill(user_info['name']),
            lambda: page.get_by_placeholder("Nombre").fill(user_info['name']),
            lambda: page.get_by_placeholder("First Name").fill(user_info['name']),
        ]
        try_fill(Name_Methods)

        # Methods for filling in the surname
        Surname_Methods = [
            lambda: page.get_by_label("Last Name*").fill(user_info['surname']),
            lambda: page.locator("[id=\"applicant_lead_attributes\\[last_name\\]\"]").fill(user_info['surname']),
            lambda: page.get_by_label("Last Name *").fill(user_info['surname']),
            lambda: page.get_by_placeholder("Apellidos").fill(user_info['surname']),
            lambda: page.get_by_placeholder("Last Name").fill(user_info['surname']),
        ]
        try_fill(Surname_Methods)

        # Methods for filling in the email
        Email_Methods = [
            lambda: page.get_by_placeholder("Email").fill(user_info['email']),
            lambda: page.get_by_label("Email✱").fill(user_info['email']),
            lambda: page.get_by_label("Email*").fill(user_info['email']),
            lambda: page.get_by_label("Email *").fill(user_info['email']),
            lambda: page.locator("[id=\"applicant_lead_attributes\\[email\\]\"]").fill(user_info['email']),
            lambda: page.get_by_placeholder("hello@example.com...").fill(user_info['email']),
            lambda: page.locator("input[name=\"personal_info\\.email\"]").fill(user_info['email']),
        ]
        try_fill(Email_Methods)

        # Methods for filling in the phone number
        Number_Methods = [
            lambda: page.get_by_label("Phone").fill(user_info['number']),
            lambda: page.get_by_label("Phone ✱").fill(user_info['number']),
            lambda: page.get_by_placeholder("Teléfono").fill(user_info['number']),
            lambda: page.locator("[id=\"applicant_lead_attributes\\[phone\\]\"]").fill(user_info['number']),
        ]
        try_fill(Number_Methods)

        # Methods for filling in the LinkedIn URL
        LinkedIn_Methods = [
            lambda: page.get_by_label("LinkedIn URL").fill(user_info['linkedin']),
            lambda: page.get_by_label("LinkedIn").fill(user_info['linkedin']),
            lambda: page.get_by_label("Linkedin").fill(user_info['linkedin']),
            lambda: page.get_by_label("LinkedIn Profile").fill(user_info['linkedin']),
            lambda: page.get_by_placeholder("Perfil de Linkedin").fill(user_info['linkedin']),
            lambda: page.locator("input[name=\"personal_info\\.linkedin_profile\"]").fill(user_info['linkedin']),
        ]
        try_fill(LinkedIn_Methods)

        # Methods for filling in the GitHub URL
        GitHub_Methods = [
            lambda: page.get_by_label("Github").fill(user_info['github']),
            lambda: page.get_by_label("Github URL").fill(user_info['github']),
            lambda: page.get_by_label("Github Link").fill(user_info['github']),
        ]
        try_fill(GitHub_Methods)

        # Methods for filling in the portfolio URL
        Portfolio_Methods = [
            lambda: page.get_by_label("Portfolio").fill(user_info['portfolio']),
            lambda: page.get_by_label("Portfolio URL").fill(user_info['portfolio']),
            lambda: page.get_by_label("Portfolio Link").fill(user_info['portfolio']),
            lambda: page.get_by_label("Website").fill(user_info['portfolio']),
            lambda: page.get_by_label("Other website").fill(user_info['portfolio']),
        ]
        try_fill(Portfolio_Methods)

        # Methods for filling in the city
        City_Methods = [
            lambda: page.get_by_role("textbox", name="City*").fill(user_info['city']),
        ]
        try_fill(City_Methods)
