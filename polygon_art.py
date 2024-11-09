import turtle
import random


class Polygon:
    def __init__(self, num_sides, size, orientation, location, color, border_size):
        self.num_sides = num_sides
        self.size = size
        self.orientation = orientation
        self.location = location
        self.color = color
        self.border_size = border_size

    def draw(self):
        # Setup turtle
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()

        # Draw the polygon
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360 / self.num_sides)

        turtle.penup()

    def get_new_color(self):
        # Return a random color
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def reduce_size(self, reduction_ratio):
        # Reduce the size of the polygon based on the reduction ratio
        self.size *= reduction_ratio

    def reposition(self, reduction_ratio):
        # Reposition the turtle to draw a smaller polygon inside the original
        turtle.penup()
        turtle.forward(self.size * (1 - reduction_ratio) / 2)
        turtle.left(90)
        turtle.forward(self.size * (1 - reduction_ratio) / 2)
        turtle.right(90)
        self.location = [turtle.pos()[0], turtle.pos()[1]]


# Main script
def main():
    # Set up the environment
    turtle.speed(0)
    turtle.bgcolor('black')
    turtle.tracer(0)
    turtle.colormode(255)

    # Generate random values
    num_sides = random.randint(3, 5)  # Triangle, square, or pentagon
    size = random.randint(50, 150)
    orientation = random.randint(0, 90)
    location = [random.randint(-300, 300), random.randint(-200, 200)]
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    border_size = random.randint(1, 10)

    # Create the first polygon
    polygon1 = Polygon(num_sides, size, orientation, location, color, border_size)
    polygon1.draw()

    # Specify a reduction ratio
    reduction_ratio = 0.618

    # Create the second, smaller polygon inside the first one
    polygon2 = Polygon(polygon1.num_sides, polygon1.size, polygon1.orientation, polygon1.location, polygon1.color,
                       polygon1.border_size)
    polygon2.reduce_size(reduction_ratio)
    polygon2.reposition(reduction_ratio)
    polygon2.draw()

    # Hold the window open until clicked
    turtle.done()


# Run the program
if __name__ == "__main__":
    main()
