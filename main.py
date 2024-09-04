from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("The Pong Game")
screen.tracer(0) # turns off animation

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
left_paddle.create_paddle()
right_paddle.create_paddle()


# screen.onkey(padd.go_up, "Up")
# screen.onkey(padd.go_down, "Down")

game_on = True
while game_on:
    screen.update()


screen.exitonclick()