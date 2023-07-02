# Vergel, Chean Bernard Villanueva
# Car Class

from car_main import Car

class Outputs:
    def accelerate(self,car):
        # Accelerating the car five times
        print("\nAfter Acceleration")
        for _ in range(5):
            car.accelerate()
            
            print("Current Speed:", car.get_speed())

    def braking(self,car):
        # Braking the car five times
        print("\nAfter Braking")
        for _ in range(5):
            car.brake()
            
            print("Current Speed:", car.get_speed())