# Vergel, Chean Bernard Villanueva
# Car Class

import pyfiglet

class Greeting:
    # Make a def for the welcome message
    def print_welcome_message(self):
        print("=" * 110)
        print("=" * 110)
        welcome = pyfiglet.figlet_format("Car Speed Indicator".center(55), font="digital")
        print(welcome)
        print("=" * 110)
        print("=" * 110)
        print("\n\033[33mHi, I am Chean Bernard V. Vergel a first year college student at Polytechnic University of the Philippines.\033[0m\n")
    
    # Print closing message
    def print_goodbye_message(self):
        print("\n\U0001F504\U0001F504 Closing Program... \U0001F504\U0001F504 Thank you!\n")
        goodbye = pyfiglet.figlet_format("Visit me again", font="puffy")
        print(goodbye)
        print("")