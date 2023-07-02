# Vergel, Chean Bernard Villanueva
# Pet Class

# Write a class named Pet
class Pet:

    # _ _name (for the name of a pet)
    # _ _animal_type (for the type of animal that a pet is. Example values are ‘Dog’, ‘Cat’, and ‘Bird’)
    # _ _age (for the pet’s age)
    # The Pet class should have an _ _init_ _ method that creates these attributes. It should also have the following methods:
    def __init__(self):
        self.__name = ""
        self.__animal_type = ""
        self.__age = 0

    # Set_name() This method assigns a value to the _ _name field.
    def set_name(self, name):
        self.__name = name

    # Set_animal_type() This method assigns a value to the _ _animal_type field.
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    # Set_age() This method assigns a value to the _ _age field.
    def set_age(self, age):
        self.__age = age

    # Get_name() This method returns the value of the _ _ name field.
    def get_name(self):
        return self.__name

    # get_animal_type() This method returns the value of the _ _animal_type field
    def get_animal_type(self):
        return self.__animal_type

    # Get_age() This method returns the value of the _ _age field.
    def get_age(self):
        return self.__age


