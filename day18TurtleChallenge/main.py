from turtle import Turtle, Screen
#from random import randint

screen = Screen()

'''tim.color('blue')
tim.shape('turtle')
tim.forward(100)
tim.left(90)
tim.forward(100)
tim.left(90)
tim.forward(100)
tim.left(90)
tim.forward(100)'''

sides = 3

for sides in range(sides,11):
    tim = Turtle()
    interior_angle = (sides - 2) * 180/sides
    #print(f"For {sides}, the interior angle is {interior_angle}")

    for i in range(sides):
        #print(f"Value of {i}")
        #tim.color(random.ran(), random.random(), random.random())
        tim.forward(100)
        tim.right(180-interior_angle)

screen.exitonclick()