class Shape:#this file will be imported into module.py
    def __init__(self, name):
        self.name = name

    def area(self):
        raise NotImplementedError("Subclass must implement area()")

class ColoredShape(Shape):
    def __init__(self, name, color):
        super().__init__(name)  # Call parent class constructor
        self.color = color

class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length

    def area(self):
        return self.length * self.length

class ColoredSquare(ColoredShape, Square):  # Inherits from both Shape and ColoredShape
    def __init__(self, length, color):
        super().__init__("Square", color)  # Call parent class constructor (ColoredShape)
        self.length = length

    def __str__(self):
        return f"Colored {self.name} with color {self.color} and area {self.area()}"


