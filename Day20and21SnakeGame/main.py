from turtle import Screen
import scoreboard
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time

#SettingUpScreen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_counter = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
current_score = 0

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.3)
    snake.move()

    if snake.head.distance(food) < 30:
        snake.extend_snake()
        current_score = current_score + 1
        food.new_food()
        score_counter.update_score(current_score)

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score_counter.wall_collision()

    segment = []

    #Detect tail collision
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            score_counter.tail_collision()

screen.exitonclick()