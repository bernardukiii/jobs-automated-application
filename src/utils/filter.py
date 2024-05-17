import string

def filter_text():
    # PROMPT USER FOR KEYWORDS USER WOULD LIKE TO USE TO FILTER
    keywords = []

    print('Enter keywords one at a time')

    while True:
        user_input = input("Next word: ").lower()
        
        if user_input == 'exit':
            break
        elif user_input == 'nextjs':
            keywords.append(user_input)
            keywords.append('next.js')
            keywords.append('next js')
            print("Keywords: ", keywords)
        elif user_input == 'react':
            keywords.append(user_input)
            keywords.append('react.js')
            keywords.append('react js')
            print("Keywords: ", keywords)
        elif user_input == 'tailwind':
            keywords.append(user_input)
            keywords.append('tailwindcss')
            print("Keywords: ", keywords)
        elif user_input == 'chakra ui':
            keywords.append(user_input)
            keywords.append('chakraui')
            keywords.append('chakra')
            print("Keywords: ", keywords)
        else:
            keywords.append(user_input)
            print("Keywords: ", keywords)
    
    # PROMPT FOR THE DESCRIPTION USER WOULD LIKE TO FILTER THROUGH
    job_description_lines = []
    lowered_job_description = []

    print("Please enter the job description (copy/paste allowed). Type 'end' on a new line to finish:")
    # handle long descriptions as they have line spaces that cause the terminal to break out of app
    while True:
        line = input()
        if line.strip().lower() == 'end':
            break
        job_description_lines.append(line)
    
    job_description = "\n".join(job_description_lines)
    # Remove punctuation from the job description ## avoids edgecases like when the texts says 'react, tailwind and html' if we search for react, it will not find it due to the comma
    job_description = job_description.translate(str.maketrans('', '', string.punctuation))
        
    job_description_list = job_description.split()
    # Every word in job description to lowercase
    for word in job_description_list:
        lowercase_word = word.lower()
        lowered_job_description.append(lowercase_word)

    print('This should be a list of strings:', lowered_job_description)
