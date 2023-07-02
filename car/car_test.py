# Vergel, Chean Bernard Villanueva
# Car Class

# Import the other file
from car_main import Car
from car_outputs import Outputs
from car_greetings import Greeting
from car_user_interface import Userinterface

if __name__ == "__main__":
    greet = Greeting()
    ui = Userinterface()

    greet.print_welcome_message()
    ui.name_user()


    # Creating a class for car test
    car = Car(2023, "Toyota")
    out = Outputs()
    # Print the initial speed
    print("\n\U0001F6D1 \033[31mInitial Speed:\U0001F6D1 \033[31m", car.get_speed())
        
    out.accelerate(car)
    out.braking(car)

    greet.print_goodbye_message()