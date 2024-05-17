from utils.filter import filter_text

print("Welcome to Jobs Automated")
print("We provide jobs descriptions filtering to see if it matches what you're looking for and we take care of automating the application form with repetitive information.")
print("Navigation commands:")
print("'done' => breaks out of loops")

requested_tool = input("Please select either filtering (DF) or automation (FA): ").lower()

if requested_tool == 'df':
    print("Let's filter that description!")
    filter_text()
elif requested_tool == 'fa':
    print("Let's automate that form!")
