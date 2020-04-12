import turtle

my_turtle = turtle.Turtle()

def square():
    my_turtle.forward(100)
    my_turtle.left(90)
    my_turtle.forward(100)
    my_turtle.left(90)
    my_turtle.forward(100)
    my_turtle.left(90)
    my_turtle.forward(100)

for count in range(4):
    square()


turtle.done()