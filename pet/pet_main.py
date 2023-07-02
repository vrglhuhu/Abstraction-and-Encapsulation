# Vergel, Chean Bernard Villanueva
# Pet Class

from pet import Pet

def main():
    my_pet = Pet()

    name = input("Enter the name of your pet: ")
    my_pet.set_name(name)

    animal_type = input("Enter the type of your pet (e.g., Dog, Cat, Bird): ")
    my_pet.set_animal_type(animal_type)

    while True:
        try:
            age = int(input("Enter the age of your pet: "))
            if age < 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Age must be a non-negative integer.")

    my_pet.set_age(age)

    print("\nPet Information:")
    print("Name:", my_pet.get_name())
    print("Type:", my_pet.get_animal_type())
    print("Age:", my_pet.get_age())


if __name__ == "__main__":
    main()
