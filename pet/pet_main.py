# Vergel, Chean Bernard Villanueva
# Pet Class

from pet import Pet
from pet_greetings import Greeting
from pet_test import Test

# Make def main
def main():
    test = Test()
    greet = Greeting()

    # Print the welcome message 
    greet.print_welcome_message()

    while True:
        test.user_prompts()
        test.pet_info()

        choice = input("\U0001F4CC \033[40m\033[33mDo you want to identify another pet? \033[40m\033[34mYES\033[0m or \033[40m\033[34mNO:\033[0m : ")
        if choice.upper() != "YES":
            print("\033[35mThank you for using this Pet Identification.💡\033[0m")
            print()
            greet.print_goodbye_message()
            break  

if __name__ == "__main__":
    main()