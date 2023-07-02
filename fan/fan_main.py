# Vergel, Chean Bernard Villanueva
# Fan Class

# Create a class called fan.
class Fan:

# Create 3 constants with values of 1,2, and 3.
    SLOW = 1
    MEDIUM = 2
    FAST = 3
 
 # Define the constructor with required arguments
    def __init__(self, speed, radius, color, on):
        self._speed = speed
        self._radius = radius
        self._color = color
        self._on = on

# Accessor Methods
# Make a private integer method for speed.
    def get_speed(self):
        return self._speed
    
# Make a private boolean method to on the fan.
    def get_on(self):
        return self._on
    
# Make a private float method for the radius of the fan.
    def get_radius(self):
        return self._radius
    
# Make a private string method for the color of the fan.
    def get_color(self):
        return self._color

# Mutator Methods  
# Make a mutator method for speed.
    def set_speed(self, speed):
        self._speed = speed

# Make a mutator method to on the fan.
    def set_on(self, on):
        self._on = on
# Make a mutator method for the radius of the fan.
    def set_radius(self, radius):
        self._radius = radius

# Make a mutator method for the color of the fan.
    def set_color(self, color):
        self._color = color
        
# Make a def run test for fan 1
    def runfan1_test(self):
        
        # Create Fan object
        fan1 = Fan(speed=Fan.FAST, radius=10, color='yellow', on=True)
        
        # Display fan 1 properties
        print("Fan 1:")
        print("Speed:", fan1.get_speed())
        print("Radius:", fan1.get_radius())
        print("Color:", fan1.get_color())
        print("On:", fan1.get_on())

    # Make a def run test for fan 1
    def runfan2_test(self):
        
        # Create Fan object
        fan2 = Fan(speed=Fan.MEDIUM, radius=5, color='blue', on=False)
        
        # Display fan 1 properties
        print("\nFan 2:")
        print("Speed:", fan2.get_speed())
        print("Radius:", fan2.get_radius())
        print("Color:", fan2.get_color())
        print("On:", fan2.get_on())  