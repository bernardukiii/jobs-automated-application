from utils.filter import filter_text
from utils.prefill_form import prefill_form
from utils.handle_data import HandleData

fields = ["name", "surname", "email", "number", "linkedin", "github", "portfolio", "city"] 
user_info = {}
data_handler = HandleData()

print("Welcome to Jobs Automated \n")
print("We provide jobs descriptions filtering to see if it matches what you're looking for and we take care of automating the application form with repetitive information. \n")
print("Navigation commands:")
print("'done' => breaks out of loops \n")

requested_tool = input("Please select either filtering (DF) or automation (FA): ").lower()

if requested_tool == 'df':
    print("Let's filter that description!")
    filter_text()
elif requested_tool == 'fa':
    print("Let's automate that form!")
    print("Let's start by providing the information for me to prefill the form with: ")
    
    first_time = input('Is this your first time using the app? (y/n) ').lower()

    if first_time == "y":
        for field in fields:
            user_info[field] = input(f"Please enter your {field}: ")
            if field == '':
                print('Sorry, this field is required...')
                field = input(f"Please enter your {field}: ")

        formURL = input('Please enter the form URL/link: ')        
        data_handler.save_data(user_info)
        prefill_form(user_info, formURL)
    elif first_time == "n":
        search_by_name = input("Please enter your name: ").lower()
        if search_by_name != '':
            existing_data = data_handler.check_data(search_by_name)
            print('This is your saved information:')
            for field, value in existing_data.items():
                print(f"\t{field.upper()}: {value}")
        else: 
            print("No name was provided.")  
        
        edit = input("Would you like to modify your information? (y/n) ").lower()
        if edit == 'y':
            for field in fields:
                user_info[field] = input(f"Please enter your {field}: ")
                if field == '':
                    print('Sorry, this field is required...')
                    field = input(f"Please enter your {field}: ")
            formURL = input('Please enter the form URL/link: ')
            prefill_form(user_info, formURL)

        elif edit == 'n':
            user_info = data_handler.check_data(search_by_name)
            formURL = input('Please enter the form URL/link: ')
            prefill_form(user_info, formURL)


