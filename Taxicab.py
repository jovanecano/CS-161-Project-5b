# Author: Jovane Cano
# Github Username: jovanecano
# Date: 05/01/2024
# Description:
"""This program contains a class named Taxicab that contains 3 private data members x_coord, y_coord, and odometer"""

class Taxicab:
    """
    A class that represents the movement of a taxicab
    """
    def __init__(self, initialX, initialY):
        self._x_coord = initialX
        self._y_coord = initialY
        self._odometer = 0

    def get_x_coord(self):
        """function to x coordinates"""
        return self._x_coord

    def get_y_coord(self):
        """function to get x coordinates"""
        return self._y_coord

    def get_odometer(self):
        """function to get x coordinates"""
        return self._odometer

    def move_x(self, distance):
        """Moves the Taxicab in the horizontal direction"""
        self._odometer += abs(distance)
        self._x_coord += distance

    def move_y(self, distance):
        """MOves the Taxicab in the veritical direction"""
        self._odometer += abs(distance)
        self._y_coord += distance


"""
commented out the code for the example from the intial repo whcih I used to test class

cab = Taxicab(5, -8)       # creates a Taxicab object at coordinates (5, -8)
cab.move_x(3)              # moves cab 3 units "right"
cab.move_y(-4)             # moves cab 4 units "down"
cab.move_x(-1)             # moves cab 1 unit "left"
print(cab.get_odometer())  # prints the current odometer reading
# At this point the cab has traveled 3 + 4 + 1 = 8 units and is now at coordinates (7, -12)
"""