from turtle import Turtle
ROWS_BRICKS = 6
COLUMNS_BRICKS = 18
STEP_Y_BRICKS = 21


class Brick():
    
    def __init__(self, x, y, screen_size, start_increase_speed):
        self.screen_size = screen_size
        self.x = x
        self.y = y
        self.all_bricks = []
        self.colors = ['#D35346', '#D17138', '#BB7A2D', '#A59A24', '#439244', '#404FCE']
        if start_increase_speed:
            self.all_bricks_y = []
            start_y = 116
            for _ in range(5):
                self.all_bricks_y.append(start_y)
                start_y += STEP_Y_BRICKS
        self.generate_wall()
        
    def generate_wall(self):
        for i in range(ROWS_BRICKS):
            for _ in range(COLUMNS_BRICKS):
                brick = Turtle()
                brick.shape("square")
                brick.color(self.colors[i])
                brick.shapesize(1, 2)
                brick.penup()
                brick.goto(self.x, self.y)
                self.all_bricks.append(brick)
                self.x += 41
            self.y -= 21
            self.x = - self.screen_size[0] // 2 + 23
