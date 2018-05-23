import os
import sys

def title_screen():
    os.system('clear')
    print("""
    #####################################
    ###   Welcome to Elduwin Forest   ###

                ,@@@@@@@,
        ,,,.   ,@@@@@@/@@,  .oo8888o.
        ,&%%&%&&%,@@@@@/@@@@@@,8888\88/8o
    ,%&\%&&%&&%,@@@\@@@/@@@88\88888/88'
    %&&%&%&/%&&%@@\@@/ /@@@88888\88888'
    %&&%/ %&%%&&@@\ V /@@' `88\8 `/88'
    `&%\ ` /%&'    |.|        \ '|8'
        |o|        | |         | |
        |.|        | |         | |
     \\/ ._\//_/__/  ,\_//__\\/.  \_//__/_
    #####################################
                    - Play -
                    - Help -
                    - Quit -
        - Copyright 2018 imcooley -
    """)
    title_screen_selections()

def title_screen_selections():
    counter = 0
    max_attempts = 5
    while True:
        if counter != None and counter > max_attempts:
            sys.exit()
        option = input(">> ").lower()
        if option == ("play"):
            break
        elif option ==("help"):
            help_menu()
        elif option == ("quit"):
            sys.exit()
        else:
            print(f"Please select a vaild choice {max_attempts - counter} attempts left before exiting.")
            counter += 1
            

def help_menu():
    print("HEY YOU NEED TO CODE THIS!")