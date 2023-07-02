# Vergel, Chean Bernard Villanueva
# Car Class

# Import the car
from car_main import Car

# Creating a class for car test
class Car_test():
    car = Car(2023, "Example Make")

    # Print the initial speed
    print("\nInitial Speed:", car.get_speed())

    # Accelerating the car five times
    for _ in range(5):
        car.accelerate()
        print("After Acceleration")
        print("\nCurrent Speed:", car.get_speed())

    # Braking the car five times
    for _ in range(5):
        car.brake()
        print("After Braking")
        print("\nCurrent Speed:", car.get_speed())

if __name__ == "__main__":
    Car_test()