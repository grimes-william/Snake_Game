from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.speed(0)
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.pencolor("white")
        self.update_scoreboard()

    # Show the score
    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=("Arial", 10, "normal"))

    # Add score when food is eaten
    def add_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    # Move score to middle and have a special message for final score
    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg=f"Game Over!\nFinal Score: {self.score}", move=False, align="center", font=("Arial", 48, "normal"))
