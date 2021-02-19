from turtle import Turtle


class MyCar(Turtle):
    def __init__(self):
        super().__init__()
        self.my_turtle = 0
        self.score = 0
        self.create_mycar()

    def create_mycar(self):
        tur = Turtle('turtle')
        tur.shapesize()
        tur.color('red')
        tur.penup()
        tur.goto(0, -270)
        tur.setheading(90)
        self.my_turtle = tur

    def moveup(self):
        if self.my_turtle.ycor() > 0:
            if self.my_turtle.ycor() < 280:
                self.my_turtle.setheading(90)
                self.my_turtle.forward(20)
            else:
                self.my_turtle.goto(self.my_turtle.xcor(), 270)
        else:
            if self.my_turtle.ycor() > -280:
                self.my_turtle.setheading(90)
                self.my_turtle.forward(20)
            else:
                self.my_turtle.goto(self.my_turtle.xcor(), -270)

    def movedown(self):
        if self.my_turtle.ycor() > 0:
            if self.my_turtle.ycor() < 280:
                self.my_turtle.setheading(90)
                self.my_turtle.back(20)
            else:
                self.my_turtle.goto(self.my_turtle.xcor(), 270)
        else:
            if self.my_turtle.ycor() > -280:
                self.my_turtle.setheading(90)
                self.my_turtle.back(20)
            else:
                self.my_turtle.goto(self.my_turtle.xcor(), -270)

    def moveleft(self):
        self.my_turtle.setheading(180)
        self.my_turtle.forward(20)

    def moveright(self):
        self.my_turtle.setheading(0)
        self.my_turtle.forward(20)


