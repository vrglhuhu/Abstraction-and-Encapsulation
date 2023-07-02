# Vergel, Chean Bernard Villanueva
# Fan Class

class User_interface:
# Get user's choice of operation
    def get_user_choice(self):
        choice = input("\033[40m\033[33mEnter your choice:\033[0m ")
        return choice.upper()

# Ask the user if they want to perform another calculation
    def continue_calculation(self):
        while True:
            next_choice = input("\U0001F4CC \033[40m\033[33mDo you want to see the other fan?\033[0m \033[40m\033[34mYES\033[0m or \033[40m\033[34mNO:\033[0m ")
            if next_choice.upper() == "YES":
                print("\033[31mYEY!\033[0m")
                return True
            elif next_choice.upper() == "NO":
                return False
            else:
                print("\U0001F6A7 \033[31mINVALID INPUT! Please enter either YES or NO.\033[0m\U0001F6A7")
