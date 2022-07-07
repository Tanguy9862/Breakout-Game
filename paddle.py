from turtle import Turtle
PADDLE_STEP = 20


class Paddle(Turtle):
    
    def __init__(self, screen_size):
        super().__init__()
        self.screensize = screen_size
        self.shape("square")
        self.shapesize(0.7, 4)
        self.color("brown")
        self.penup()
        self.goto(0, screen_size[1] - 880)
    
    def move_left(self):
        if self.xcor() > - self.screensize[0] // 2 + 45:
            self.goto(self.xcor() - PADDLE_STEP, self.ycor())
        
    def move_right(self):
        if self.xcor() < self.screensize[0] // 2 - 45:
            self.goto(self.xcor() + PADDLE_STEP, self.ycor())
