from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("The Pong Game")
screen.tracer(0) # turns off animation

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
left_paddle.create_paddle()
right_paddle.create_paddle()

ball = Ball()
ball.create_ball()

screen.listen()
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.moveball()


screen.exitonclick()