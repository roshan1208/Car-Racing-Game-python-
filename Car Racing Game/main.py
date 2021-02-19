from turtle import Turtle, Screen
from graphics import Graphics
from cars import Cars
from mycar import MyCar
from score import Score
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.title('Car Race Game')
screen.bgcolor('black')
screen.tracer(0)

cars = Cars()
graphics = Graphics()
mycar = MyCar()
score = Score()

screen.listen()
screen.onkeypress(key='Up', fun=mycar.moveup)
screen.onkeypress(key='Down', fun=mycar.movedown)
screen.onkeypress(key='Left', fun=mycar.moveleft)
screen.onkeypress(key='Right', fun=mycar.moveright)

is_true = True
i = 1
while is_true:
    screen.update()
    time.sleep(0.03)
    if i%3 == 0:
        cars.random_cars()

    for car in cars.carcollection:
        if car.distance(mycar.my_turtle) <= 20:
            mycar.my_turtle.forward(20)
            is_true = False
            score.game_over()

    cars.move()
    i += 1
    if mycar.my_turtle.distance(mycar.my_turtle.xcor(), 280) <= 10:
        mycar.my_turtle.forward(20)
        i = 1
        score.level_up()
        time.sleep(2)
        score.score_turtle.clear()
        mycar.my_turtle.goto(0, -280)
        cars.reset()
        cars.level_up()
        score.scoreboard()


screen.exitonclick()