from turtle import Turtle, Screen

class Paddle (Turtle):
    def __init__ (self):
        super().__init__()
    
    def create_paddle (self):
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x=350, y=0)
        
    def go_up (self):
        new_y = self.ycor()+20
        self.goto(x=350, y=new_y)

    def go_down (self):
        new_y = self.ycor()-20
        self.goto(x=350, y=new_y)