# Vergel, Chean Bernard Villanueva
# Car Class

# Create a class called Car
class Car:

    # Make the data atrributes
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
 
    # Create an accelerate method
    def accelerate(self):
        self.__speed += 5

    # Create a brake method
    def brake(self):
        self.__speed -= 5

    # Create a speed method
    def get_speed(self):
        return self.__speed
    
   
        