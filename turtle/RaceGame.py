import random
import turtle


p1 = turtle.Turtle()   # paint the arrow red
p1.color('red')


p2 = p1.clone()   # clone the arrow above and paint the arrow blue
p2.color('blue')


def play_dice():  # simulates a dice

    temp = random.randint(1, 6)   # chose a random number, from 1 to 6.

    return temp


p1.penup()    # makes a circle in the point that the arrow should stop (for player 1)
p1.goto(300, 60)
p1.pendown()
p1.circle(40)

p1.penup()   # moves the arrow to the race start point (for player 1)
p1.goto(-200, 100)
p1.pendown()


p2.penup()   # makes a circle in the point that the arrow should stop (for player 1)
p2.goto(300, -140)
p2.pendown()
p2.circle(40)

p2.penup()   # moves the arrow to the race start point (for player 2)
p2.goto(-200, -100)
p2.pendown()

# The game

stop = 1
while stop == 1:
    if p1.pos() >= (300, 100):    # stop when the player 1 wins
        print('!PLAYER 1 WIN!')
        stop = 0
    elif p2.pos() >= (300, -100):   # stop when the player 2 wins
        print('!PLAYER 2 WIN!')
        stop = 0
    else:   # roll the dice when the player press enter, then he walks 12 pixels
        p1_turn = input("PLAYER 1 TURN: Press 'Enter' to roll the dice")
        play_dice()
        p1_steps = play_dice()
        print(f"PLAYER 1 TURN: The result of the die roll is: {p1_steps}\n")
        p1.forward(12 * p1_steps)

        p2_turn = input("PLAYER 2 TURN: Press 'Enter' to roll the dice")
        play_dice()
        p2_steps = play_dice()
        print(f"PLAYER 2 TURN: The result of the dice roll is: {p2_steps}\n")
        p2.forward(12 * p2_steps)

turtle.done()
