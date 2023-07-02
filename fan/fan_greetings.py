# Vergel, Chean Bernard Villanueva
# Fan Class

import pyfiglet

class Greeting:
    # Make a def for the welcome message
    def print_welcome_message(self):
        print("=" * 110)
        print("=" * 110)
        welcome = pyfiglet.figlet_format("Fan Status Indicator".center(55), font="digital")
        print(welcome)
        print("=" * 110)
        print("=" * 110)
        print("\n\033[40m\033[33mWhich fan you want to see?.\033[0m")
        print("\U0001F6D1 \033[31mPress A: \033[0m Fan 1")
        print("\U0001F6D1 \033[32mPress B: \033[0m Fan 2")
    
    # Print closing message
    def print_goodbye_message(self):
        print("\n\U0001F504\U0001F504 Closing Program... \U0001F504\U0001F504 Thank you!\n")
        goodbye = pyfiglet.figlet_format("Visit me again", font="puffy")
        print(goodbye)
        print("")