import turtle

n = int((input('high of the principal tree stem')))
screen = turtle.Screen()

turtle.left(90)         # this will make the arrow point up.


def makes_y(x):
    if x > 15:  # when the lines are smaller them 15 pixels, the function will stop, and them change your angle

        turtle.forward(x)
        turtle.left(30)
        makes_y(0.7 * x)  # this will make the left side of the "Y"
        turtle.right(60)
        makes_y(0.7 * x)     # this make the right side
        turtle.left(30)
        turtle.backward(x)   # this is to make the arrow go back
    else:
        return


makes_y(n)

screen.exitonclick()
