import turtle
import pygame

pygame.init()

# draw screen
screen = turtle.Screen()
screen.title("My Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)


# draw paddle
def draw_paddle(paddle, x):
    paddle.speed(0)
    paddle.shape("square")
    paddle.color("white")
    paddle.shapesize(stretch_wid=5, stretch_len=1)
    paddle.penup()
    paddle.goto(x, 0)


paddle_1 = turtle.Turtle()
draw_paddle(paddle_1, -350)

paddle_2 = turtle.Turtle()
draw_paddle(paddle_2, 350)

# draw ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.25
ball.dy = 0.25

# score
score_1 = 0
score_2 = 0

# head-up display
hud = turtle.Turtle()
hud.speed(0)
hud.shape("square")
hud.color("white")
hud.penup()
hud.hideturtle()
hud.goto(0, 260)
hud.write("0 : 0", align="center", font=("Press Start 2P", 24, "normal"))


def paddle_1_up():
    y = paddle_1.ycor()
    if y < 250:
        y = paddle_1.ycor()
        y += 30
    else:
        y = 250
    paddle_1.sety(y)


def paddle_1_down():
    y = paddle_1.ycor()
    if y > -250:
        y += -30
    else:
        y = -250
    paddle_1.sety(y)


def paddle_2_up():
    y = paddle_2.ycor()
    if y < 250:
        y += 30
    else:
        y = 250
    paddle_2.sety(y)


def paddle_2_down():
    y = paddle_2.ycor()
    if y > -250:
        y += -30
    else:
        y = -250
    paddle_2.sety(y)


# keyboard

screen.listen()
screen.onkeypress(paddle_1_up, "w")
screen.onkeypress(paddle_1_down, "s")
screen.onkeypress(paddle_2_up, "Up")
screen.onkeypress(paddle_2_down, "Down")


# collision with left or right side function
def collision_rl():
    hud.clear()
    hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
    pygame.mixer.music.load('beep2.mp3')
    pygame.mixer.music.play()
    ball.goto(0, 0)
    ball.dx *= -1


while True:
    screen.update()

    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # collision with the upper wall
    if ball.ycor() > 290:
        pygame.mixer.music.load('beep.mp3')
        pygame.mixer.music.play()
        ball.sety(290)
        ball.dy *= -1
    # collision with lower wall
    if ball.ycor() < -290:
        pygame.mixer.music.load('beep.mp3')
        pygame.mixer.music.play()
        ball.sety(-290)
        ball.dy *= -1

    # collision with left wall
    if ball.xcor() < -368:
        score_2 += 1
        collision_rl()

    # collision with right wall
    if ball.xcor() > 368:
        score_1 += 1
        collision_rl()

    # collision with the paddle 1
    if ball.xcor() <= -330 and paddle_1.ycor() + 57 > ball.ycor() > paddle_1.ycor() - 57:
        if ball.xcor() < -349:
            score_2 += 1
            collision_rl()

        ball.dx *= -1
        pygame.mixer.music.load('beep.mp3')
        pygame.mixer.music.play()

    # collision with the paddle 2
    if ball.xcor() >= 330 and paddle_2.ycor() + 57 > ball.ycor() > paddle_2.ycor() - 57:
        if ball.xcor() > 349:
            score_1 += 1
            collision_rl()
        ball.dx *= -1
        pygame.mixer.music.load('beep.mp3')
        pygame.mixer.music.play()
