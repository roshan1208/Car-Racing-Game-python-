from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.temp = 0
        self.score_turtle = 0


    def level_up(self):
        self.temp += 1
        tur = Turtle()
        tur.color('yellow')
        tur.hideturtle()
        tur.penup()
        tur.write(f'Level {self.temp} ', align='center', font=("Comic Sans MS", 30, "normal"))
        self.score_turtle = tur

    def game_over(self):
        tur = Turtle()
        tur.color('red')
        tur.hideturtle()
        tur.penup()
        tur.write(f'Game Over ', align='center', font=("Comic Sans MS", 40, "normal"))

    def scoreboard(self):
        self.clear()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(-200, 260)
        self.write(f'Score {self.temp} ', align='center', font=("Comic Sans MS", 20, "normal"))
