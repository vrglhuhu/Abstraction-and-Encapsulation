# Vergel, Chean Bernard Villanueva
# Car Class

from car_main import Car

class Outputs:
    def accelerate(self,car):
        # Accelerating the car five times
        print("\n🎯\033[40m\033[34mAfter Acceleration\033[0m")
        for _ in range(5):
            car.accelerate()
            
            print("🌀\033[31mCurrent Speed:\033[0m", car.get_speed())

    def braking(self,car):
        # Braking the car five times
        print("\n🎯\033[40m\033[34mAfter Braking\033[0m")
        for _ in range(5):
            car.brake()
            
            print("🌀\033[33mCurrent Speed:\033[0m", car.get_speed())