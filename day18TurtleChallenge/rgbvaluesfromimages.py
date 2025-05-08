import turtle as t
from turtle import Turtle
import random
from turtle import Screen
import colorgram

'''colors = colorgram.extract('image.jpg', 10)
print(colors)
rgb_colors = []

for color in colors:
    rgb_colors.append(color.rgb)

print(rgb_colors)'''

random_colors = [
    (34, 139, 34),
    (255, 105, 180),
    (72, 61, 139),
    (255, 165, 0),
    (70, 130, 180),
    (220, 20, 60),
    (255, 255, 0),
    (0, 191, 255),
    (186, 85, 211),
    (47, 79, 79),
    (255, 99, 71),
    (123, 104, 238),
    (60, 179, 113),
    (199, 21, 133),
    (240, 230, 140)
]

t.colormode(255)
tim = t.Turtle()
tim.pensize(30)
screen = Screen()

for _ in range(20):
    tim.dot(20, random.choice(random_colors))
    tim.penup()
    tim.forward(50)

screen.exitonclick()