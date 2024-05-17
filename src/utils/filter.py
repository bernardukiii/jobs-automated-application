def filter_text():
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
    # job_description = input("Please enter the job description (copy/paste allowed): ")
