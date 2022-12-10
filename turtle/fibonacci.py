import turtle

fibonacci_list = []


def make_fibonacci_list(n_terms):  #this function will fill in the empty list  with n terms of the fibonacci sequence.
    for i in range (n_terms):
        if i < 2:
            fibonacci_list.append(i)
        else:
            fibonacci_list.append(fibonacci_list[i-1] + fibonacci_list[i-2])


def make_square(): #this function will make squares with the values of the sequence
    screen = turtle.Screen()

    for i in range(3):  #this loop will make the first square.
        turtle.forward(fibonacci_list[1])
        turtle.left(90)
        if i == 2:
            turtle.forward(fibonacci_list[1])


    for i in range(2, n): #this one will make n - 2 squares.
        turtle.backward(fibonacci_list[i-1]) #this make the arrow remake his last move
        turtle.right(90)                     #this too, but, it remakes one before that the line above
        turtle.forward(fibonacci_list[i])    #from now on, just make sides of the squares...
        turtle.left(90)
        turtle.forward(fibonacci_list[i])
        turtle.left(90)
        turtle.forward(fibonacci_list[i])


    screen.exitonclick()



n = int(input('write the number of terms in the sequence\n'))

make_fibonacci_list(n+1)

print(fibonacci_list)

make_square()
