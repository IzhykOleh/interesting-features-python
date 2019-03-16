class Rectangle():
    def __init__(self, x_side, y_side):
        self.x = x_side
        self.y = y_side

    def __repr__(self):
        return "Rectangle: %.1f , %.1f" % (self.x, self.y)

class Circle():
    def __init__(self, radius):
        self.radius = radius
        
    @classmethod
    def from_rectangle(cls, rectangle):
        radius = (rectangle.x ** 2 + rectangle.y ** 2) ** 0.5 / 2
        return cls(radius)

    def __repr__(self):
        return "Circle(%.3f)" % self.radius

def Main():
    rectangle = Rectangle(3, 4)
    print(rectangle)

    first_circle = Circle(3)
    print(first_circle)

    second_circle = Circle.from_rectangle(rectangle)
    print(second_circle)

if __name__ == '__main__':
    Main()
        
