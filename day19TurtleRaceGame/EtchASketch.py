from turtle import Turtle, Screen
import random

screen = Screen()
screen.listen()

tim = Turtle()

def move_forward():
    tim.forward(20)

def move_backward():
    tim.backward(20)

def turn_left():
    tim.left(20)

def turn_right():
    tim.right(20)

screen.onkey(turn_right,"d")
screen.onkey(turn_left,"a")
screen.onkey(move_forward,"w")
screen.onkey(move_backward,"s")

screen.exitonclick()