from turtle import Turtle
ALIGNEMENT = "center"
SCORE_FONT = ("BBB Simulator Black", 30)
EXTRA_FONT = ("BBB Simulator Outline", 25)

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.color("white")
        self.goto(0, 230)
        self.show_score()
    
    def show_score(self):
        self.clear()
        self.formatted_score = "{:02}".format(self.score)
        self.write(f'{self.formatted_score}', align=ALIGNEMENT, font=SCORE_FONT)
    
    def increase_score(self):
        self.score += 1
        self.show_score()
    
    def decrease_life(self):
        self.life -= 1
        self.show_score()


class LifeBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("#af4154")
        self.goto(315, 235)
        self.life = 3
        self.show_life()
        
    def show_life(self):
        self.clear()
        self.write(f'{self.life} ♥', align=ALIGNEMENT, font=EXTRA_FONT)
        
    def decrease_life(self):
        self.life -= 1
        self.show_life()
        if self.life == 0:
            self.show_game_over()
            return False
        else:
            return True
    
    def show_game_over(self):
        game_over = Turtle()
        game_over.color("#96281b")
        game_over.penup()
        game_over.goto(0, -50)
        game_over.write("GAME OVER!", align=ALIGNEMENT, font=EXTRA_FONT)
        
        
class RecordBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("orange")
        self.goto(-305, 235)
        try:
            with open("record.txt", "r") as f:
                self.old_record = int(f.read())
        except FileNotFoundError:
            self.old_record = 0
        self.show_record()
        
    def show_record(self):
        self.clear()
        if self.old_record == 0:
            formatted_record = "-"
        else:
            formatted_record = self.old_record
        self.write(f'🏆 {formatted_record}', align=ALIGNEMENT, font=EXTRA_FONT)
    
    def write_new_record(self, new_record):
        with open("record.txt", "w") as f:
            f.write(str(new_record))
