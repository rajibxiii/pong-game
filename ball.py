from turtle import Turtle

class Ball (Turtle):
    def __init__ (self):
        super().__init__()

    def create_ball (self):
        self.shape("circle")
        self.color("magenta")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.x_move = 15
        self.y_move = 10
        self.ballspeed = 0.1

    def moveball (self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def bounce_y (self):
        self.y_move *= -1 # changing ball's direction to exactly opposite
        
    def bounce_x (self):
        self.x_move *= -1
        self.ballspeed *= 0.9 # changing the speed of the ball when successfully touched a paddle

    def reset_position (self):
        self.goto(0, 0)
        self.ballspeed = 0.5