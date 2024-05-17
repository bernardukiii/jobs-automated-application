def filter_text():
    keywords = []

    print('Enter keywords one at a time')

    while True:
        user_input = input("Next word: ")
        
        if user_input == 'exit':
            break
        else:
            keywords.append(user_input)
            print("Keywords: ", keywords)
    # job_description = input("Please enter the job description (copy/paste allowed): ")
