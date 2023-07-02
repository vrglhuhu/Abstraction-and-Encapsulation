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