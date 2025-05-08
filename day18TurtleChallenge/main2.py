import turtle as t
import random

t.colormode(255)
tim = t.Turtle()

#colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

directions = [0, 90, 180, 270]
tim.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return tim.color(r, g, b)

for _ in range(20):
    #tim.color(random.choice(colours))
    random_color()
    tim.pensize(random.randint(5, 40))
    tim.forward(random.randint(5, 80))
    tim.setheading(random.choice(directions))