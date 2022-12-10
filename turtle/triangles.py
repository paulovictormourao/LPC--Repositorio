import turtle


def make_triangle(x, y):

    turtle.penup()  # the arrow stops to draw

    turtle.goto(x, y)  # the arrow go to where the user clicks

    turtle.pendown()  # the arrow returns to draw
    
    for i in range(3):  # makes a triangle
        turtle.forward(100)
        turtle.left(120)


sc = turtle.Screen()

turtle.onscreenclick(make_triangle, 1)

turtle.done()
