from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.shapesize(stretch_wid=0.75, stretch_len=0.75)
        self.speed("fastest")
        self.new_food()

    def new_food(self):
        self.goto(random.randint(-260, 260), random.randint(-260, 260))
