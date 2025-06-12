from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-20,280)
        self.color("white")
        self.write("Score: ",False,align="center",font=("Arial",12,"bold"))

    def update_score(self,score_counter):
        self.clear()
        self.write(f"Score: {score_counter}",False,align="center",font=("Arial",12,"bold"))

    def wall_collision(self):
        self.goto(0,0)
        self.write("YOU MET AMBUJA CEMENT'S WALL", False, align="center", font=("Arial", 12, "bold"))

    def tail_collision(self):
        self.goto(0,0)
        self.write("ANOTHER ONE BITES THE DUST!", False, align="center", font=("Arial", 12, "bold"))