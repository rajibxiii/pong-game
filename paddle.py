from turtle import Turtle, Screen


class Paddle (Turtle):
    def __init__ (self, paddle_position):
        super().__init__()
        self.paddle_position = paddle_position
    
    def create_paddle (self):
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setpos(self.paddle_position)
        
    def go_up (self):
        new_y = self.ycor()+20
        self.goto(self.xcor(), y=new_y)

    def go_down (self): 
        new_y = self.ycor()-20
        self.goto(self.xcor(), y=new_y)