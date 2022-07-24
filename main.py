from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

# TODO: 1. create a screen
screen = Screen()
screen.setup(height=600, width=800)  # sets screen size.
screen.bgcolor("black")
screen.title("Pone Game")
screen.tracer(0)  # animation is turned off

# right paddle and left paddle created from Paddle class from paddle.py file
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
ball = Ball()
scoreboard = ScoreBoard()


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()  # .tracer(0) -> turning off animation -> .update() to update the screen.
    ball.move()

    # Detect collision with wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -320:
        ball.bounce_x()

    # Detect R_paddle missed
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect R_paddle missed
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


# screen exits ones it clicked
screen.exitonclick()
