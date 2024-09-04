from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

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
scores = Scoreboard()

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

    # detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() <-280:
        ball.bounce_y()

    # detect collision with the right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320: # measures the distance from the middle points of the objects
        ball.bounce_x()
    # detect ball miss
    elif ball.xcor() > 380:
        ball.reset_position()
        scores.left_point()
    elif ball.xcor() < -380:
        ball.reset_position()
        scores.right_point()



screen.exitonclick()