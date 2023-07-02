# Vergel, Chean Bernard Villanueva
# Fan Class

from fan_main import Fan

# Make a def run test for fan 1
class Outputs:
    def runfan1_test(self): 
        # Create Fan object
        fan1 = Fan(speed=Fan.FAST, radius=10, color='yellow', on=True)
        
        # Display fan 1 properties
        print("🌀\033[31mFan 1:\033[0m")
        print("♦\033[40m\033[34mSpeed:\033[0m", fan1.get_speed())
        print("♦\033[40m\033[34mRadius:\033[0m", fan1.get_radius())
        print("♦\033[40m\033[34mColor:\033[0m", fan1.get_color())
        print("♦\033[40m\033[34mOn:\033[0m", fan1.get_on())

    # Make a def run test for fan 1
    def runfan2_test(self):
        
        # Create Fan object
        fan2 = Fan(speed=Fan.MEDIUM, radius=5, color='blue', on=False)
        
        # Display fan 1 properties
        print("🌀\033[31mFan 2:\033[0m")
        print("♦\033[40m\033[34mSpeed:\033[0m", fan2.get_speed())
        print("♦\033[40m\033[34mRadius:\033[0m", fan2.get_radius())
        print("♦\033[40m\033[34mColor:\033[0m", fan2.get_color())
        print("♦\033[40m\033[34mOn:\033[0m", fan2.get_on())  