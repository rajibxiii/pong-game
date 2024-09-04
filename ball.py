from turtle import Turtle

class Ball (Turtle):
    def __init__ (self):
        super().__init__()

    def create_ball (self):
        self.shape("circle")
        self.color("magenta")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(0, 0)

    def moveball (self):
        new_x = self.xcor()+10
        new_y = self.ycor()+10
        self.goto(x=new_x, y=new_y)