# Vergel, Chean Bernard Villanueva
# Car Class

# Import the car
from car_main import Car
from car_outputs import Outputs

class Car_test():
    # Creating a class for car test
    class Car_test():
        car = Car(2023, "Toyota")
        out = Outputs()
        # Print the initial speed
        print("\nInitial Speed:", car.get_speed())
        
        out.accelerate(car)
        out.braking(car)
        

if __name__ == "__main__":
    Car_test()