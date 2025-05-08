import turtle as t
from turtle import Turtle
import random
from turtle import Screen

t.colormode(255)
#tim = t.Turtle()

screen = Screen()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return tim.color(r, g, b)

'''for _ in range(20):
    #tim.color(random.choice(colours))
    random_color()
    tim.pensize(random.randint(5, 40))
    tim.forward(random.randint(5, 80))
    tim.setheading(random.choice(directions))'''

sides = 360

for sides in range(sides,362):
    tim = Turtle()
    tim.speed("fastest")
    interior_angle = (sides - 2) * 180/sides
    #print(f"For {sides}, the interior angle is {interior_angle}")

    for i in range(sides):
        #print(f"Value of {i}")
        #tim.color(random.ran(), random.random(), random.random())
        tim.forward(100)
        tim.right(180-interior_angle)

screen.exitonclick()