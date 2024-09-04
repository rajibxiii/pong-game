from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("The Pong Game")

padd = Paddle()
padd.create_paddle()


screen.listen()
screen.onkey(padd.go_up, "Up")
screen.onkey(padd.go_down, "Down")








screen.exitonclick()