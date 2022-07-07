from random import randint
from turtle import Turtle
BOUNCING_STEP = 10


class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.seth(90)
        self.step_x = BOUNCING_STEP
        self.step_y = BOUNCING_STEP
    
    def move(self):
        self.goto(self.xcor() + self.step_x, self.ycor() + self.step_y)
    
    def bounce_x(self):
        self.step_y *= -1
    
    def bounce_y(self):
        self.step_x *= -1
    
    def special_bounce(self):
        self.step_x *= -1
        self.step_y *= -1
    
    def restart_ball(self, ball):
        ball.goto(randint(-300, 300), 50)
        self.step_y *= -1
