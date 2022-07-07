from time import time
from turtle import Screen
from paddle import Paddle
from bricks import Brick
from ball import Ball
from scoreboard import ScoreBoard, LifeBoard, RecordBoard
import time

SCREEN_SIZE = (750, 600)
X = - SCREEN_SIZE[0] // 2 + 23
Y = 200
SPEED_BALL = 0.06

screen = Screen()
screen.setup(width=SCREEN_SIZE[0], height=SCREEN_SIZE[1])
screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer(0)
screen.cv._rootwindow.resizable(False, False)

paddle = Paddle(screen_size=SCREEN_SIZE)
ball = Ball()
bricks = Brick(x=X, y=Y, screen_size=SCREEN_SIZE, start_increase_speed=True)
scoreboard = ScoreBoard()
lifeboard = LifeBoard()
recordboard = RecordBoard()

screen.listen()
screen.onkey(paddle.move_left, 'Left')
screen.onkeypress(paddle.move_left, 'Left')
screen.onkey(paddle.move_right, 'Right')
screen.onkeypress(paddle.move_right, 'Right')

is_game_on = True

while is_game_on:
    screen.update()       
    time.sleep(SPEED_BALL)
    ball.move()
    lifeboard.show_life()
    recordboard.show_record()
    
    # Detect collision with bricks:
    for brick in bricks.all_bricks:
                          
        if ball.distance(brick) <= 25:
            # Detect collision with side of bricks:
            if ball.ycor() > brick.ycor() - 6 and ball.ycor() < brick.ycor() + 6:
                # Detect if there is a collision with corner of bricks:
                if ball.ycor() == brick.ycor():
                    ball.special_bounce()
                else:
                    ball.bounce_y()
            else:
                ball.bounce_x()
            
            # Increase speed of ball:
            try:
                if brick.ycor() in bricks.all_bricks_y:
                    SPEED_BALL -= 0.01
                    bricks.all_bricks_y.remove(brick.ycor())
            except AttributeError:
                bricks.all_bricks_y = []
            
            brick.goto(-500, 0)
            brick.hideturtle()
            bricks.all_bricks.remove(brick)
            scoreboard.increase_score()
            
    # Generate new wall of bricks if the current one is fully destroyed:
    if len(bricks.all_bricks) == 0 and ball.distance(paddle) <= 40 and ball.ycor() <= SCREEN_SIZE[1] - 870:
        bricks = Brick(x=X, y=Y, screen_size=SCREEN_SIZE, start_increase_speed=False)
            
    # Detect colision with wall:
    if ball.xcor() >= SCREEN_SIZE[0] // 2 - 15 or ball.xcor() <= - SCREEN_SIZE[0] // 2 + 15:
        ball.bounce_y()
        
    # Detect collision with top:
    if ball.ycor() >= SCREEN_SIZE[1] // 2 - 15:
        ball.bounce_x()
    
    # Detect paddle misses:
    if ball.ycor() <= SCREEN_SIZE[1] - 890:
        if lifeboard.decrease_life():
            ball.restart_ball(ball)
        else:
            if scoreboard.score > recordboard.old_record:
                recordboard.write_new_record(new_record=scoreboard.score)
            is_game_on = False
    
    # Detect collision with paddle:
    if ball.distance(paddle) <= 40 and ball.ycor() <= SCREEN_SIZE[1] - 870:
        if ball.ycor() <= SCREEN_SIZE[1] - 880:
            if lifeboard.decrease_life():
                ball.restart_ball(ball)
            else:
                if scoreboard.score > recordboard.old_record:
                    recordboard.write_new_record(new_record=scoreboard.score)
                is_game_on = False
        elif ball.ycor() == paddle.ycor():
            ball.special_bounce()
        else:
            ball.bounce_x()
            
screen.exitonclick()
