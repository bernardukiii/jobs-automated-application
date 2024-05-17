import os

def clear_console():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux
    else: 
        os.system('clear')