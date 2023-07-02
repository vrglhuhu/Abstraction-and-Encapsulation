# Vergel, Chean Bernard Villanueva
# Pet Class

import pyfiglet

class Greeting:
    # Make a def for the welcome message
    def print_welcome_message(self):
        print("=" * 110)
        print("=" * 110)
        welcome = pyfiglet.figlet_format("Pet Identification".center(55), font="digital")
        print(welcome)
        print("=" * 110)
        print("=" * 110)

    
    # Print closing message
    def print_goodbye_message(self):
        print("\n\U0001F504\U0001F504 Closing Program... \U0001F504\U0001F504 Thank you!\n")
        goodbye = pyfiglet.figlet_format("Visit me again", font="puffy")
        print(goodbye)
        print("")