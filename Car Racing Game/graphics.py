from turtle import Turtle

ROAD = 40


class Graphics(Turtle):
    def __init__(self):
        super().__init__()
        self.create_road()
        self.create_road_path()
        self.write()

    def create_road(self):
        for i in range(11):
            tur = Turtle('square')
            tur.color('blue')
            tur.pensize(4)
            tur.penup()
            tur.speed('fastest')
            tur.goto(-300, -(300-50*(i+1)))
            tur.pendown()
            tur.speed('fastest')
            tur.forward(600)
            tur.hideturtle()

    def create_road_path(self):
        tur2 = Turtle('square')
        tur2.color('white')
        tur2.pensize(2)
        tur2.penup()
        tur2.speed('fastest')
        for i in range(10):
            tur2.goto(-300, -(275-50*(i+1)))
            for j in range(15):
                tur2.pendown()
                tur2.speed(0)
                tur2.forward(20)
                tur2.penup()
                tur2.speed(0)
                tur2.forward(20)
            tur2.hideturtle()

    def write(self):
        tur3 = Turtle()
        tur3.penup()
        tur3.speed(10)
        tur3.goto(-10, -285)
        tur3.color('green')
        tur3.write(f'Starting Point', align='center', font=("Comic Sans MS", 20, "normal"))

        tur3.penup()
        tur3.goto(-20, 260)
        tur3.color('red')
        tur3.write(f'End Point', align='center', font=("Comic Sans MS", 20, "normal"))
        tur3.hideturtle()