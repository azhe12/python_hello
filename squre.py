import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor('red')

    point = turtle.Turtle()

    point.shape('turtle')
    point.color('black')

    point.forward(100)
    point.right(90)
    point.forward(100)
    point.right(90)
    point.forward(100)
    point.right(90)
    point.forward(100)

    apple = turtle.Turtle()
    apple.color('blue')
    apple.circle(100)

    window.exitonclick()

draw_square()
