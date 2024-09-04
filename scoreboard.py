from turtle import Turtle

class Scoreboard (Turtle):
    def __init__ (self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.leftScore = 0
        self.rightScore = 0
        
    def update_scores (self):
        self.clear()
        self.goto(-100, 180)
        self.write(self.leftScore, align="center", font=("Arial", 80, "normal"))
        self.goto(100, 180)
        self.write(self.rightScore, align="center", font=("Arial", 80, "normal"))

    def left_point (self):
        self.leftScore += 1
        self.update_scores()

    def right_point (self):
        self.rightScore += 1
        self.update_scores()