# Vergel, Chean Bernard Villanueva
# Fan Class

from fan_main import Fan

# Create a class named TestFan
class TestFan:

    # Make a def run test 
    def run_test(self):
        
        # Create two Fan objects
        fan1 = Fan(speed=Fan.FAST, radius=10, color='yellow', on=True)
        fan2 = Fan(speed=Fan.MEDIUM, radius=5, color='blue', on=False)

        # Display fan properties
        print("Fan 1:")
        print("Speed:", fan1.get_speed())
        print("Radius:", fan1.get_radius())
        print("Color:", fan1.get_color())
        print("On:", fan1.get_on())

        print("\nFan 2:")
        print("Speed:", fan2.get_speed())
        print("Radius:", fan2.get_radius())
        print("Color:", fan2.get_color())
        print("On:", fan2.get_on())


# Create an instance of TestFan and run the test
test = TestFan()
test.run_test()