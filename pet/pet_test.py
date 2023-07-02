# Vergel, Chean Bernard Villanueva
# Pet Class

from pet import Pet
from pet_greetings import Greeting

my_pet = Pet()
greet = Greeting()

class Test:
    def user_prompts(self):
        # Ask for the name of the pet
        name = input("\n🌟🌟\033[40m\033[34mEnter the name of your pet:🌟🌟 \033[0m")
        my_pet.set_name(name)

        # Ask for the pet type
        animal_type = input("\n🌟🌟\033[40m\033[34mEnter the type of your pet (e.g., Dog, Cat, Bird):🌟🌟 \033[0m")
        my_pet.set_animal_type(animal_type)

        # Create a while loop for ValueError
        while True:
            try:
                age = int(input("\n🌟🌟\033[40m\033[34mEnter the age of your pet:🌟🌟 \033[0m"))
                if age < 0:
                    raise ValueError
                my_pet.set_age(age)
                break
            except ValueError:
                print("\U0001F6A7 \033[31mInvalid input. Age must be a non-negative integer.\033[0m\U0001F6A7")

    def pet_info(self):
        print("\n♦♦♦\033[32mPet Information:♦♦♦\033[0m")
        print("🧱\U0001F6D1 \033[31mName: \033[0m", my_pet.get_name())
        print("🧱\U0001F6D1 \033[31mType: \033[0m", my_pet.get_animal_type())
        print("🧱\U0001F6D1 \033[31mAge: \033[0m", my_pet.get_age())