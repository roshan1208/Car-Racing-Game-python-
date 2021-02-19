import turtle as t
from turtle import Turtle
import random
t.colormode(255)

class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.car_speed = 10
        self.carcollection = []
        self.create_cars()

    def create_cars(self):
        tur = Turtle('square')
        tur.color('white')
        x_loc = -260
        # x_loc = random.randint(-280, 280)
        y_loc = random.randint(0, 9)
        tur.penup()
        tur.goto(x_loc, -225 + y_loc*50)
        self.carcollection.append(tur)
        # tur.forward(20)

    def move(self):
        for tur in self.carcollection:
            tur.forward(self.car_speed)

    def random_cars(self):
        tur = Turtle('square')
        r = random.randint(20,255)
        g = random.randint(20, 255)
        b = random.randint(20, 255)
        tur.color((r, g, b))
        x_loc = -310
        # x_loc = random.randint(-280, 280)
        y_loc = random.randint(0, 9)
        tur.penup()
        tur.goto(x_loc, -225 + y_loc*50)
        self.carcollection.append(tur)
        #tur.forward(20)

    def reset(self):
        for car in self.carcollection:
            car.reset()
            car.hideturtle()
        self.carcollection = []

    def level_up(self):
        self.car_speed += 2





