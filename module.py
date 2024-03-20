#Module is just python file which can be imported into another python file for further use like see
from modulee import ColoredSquare

# Create a colored square object
colored_square = ColoredSquare(5, "red")

# Access attributes and call methods
print(colored_square.name)  # Output: Square
print(colored_square.color)  # Output: red
print(colored_square.area())  # Output: 25
print(colored_square)  # Output: Colored Square with color red and area 25

