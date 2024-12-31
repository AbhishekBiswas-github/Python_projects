from turtle import Turtle
TOTAL_SCORE = 37
FONT = ("arial", 18, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.score_turtle = Turtle()
        self.score_turtle.speed('fastest')
        self.score_turtle.color('black')
        self.score_turtle.penup()
        self.score_turtle.hideturtle()
        self.set_highscore()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.score_turtle.goto(170, 350)
        self.score_turtle.write(f"Your Score: {self.score}/{TOTAL_SCORE}", font=FONT)

    def update_score(self):
        self.score += 1
        self.score_turtle.clear()
        self.set_highscore()
        self.update_scoreboard()

    def end_game(self):
        self.score_turtle.goto(-100, 0)
        self.score_turtle.write("Game Over", font=("arial", 20, 'bold'))

    def get_highScore(self):
        with open("./ScoreBoard/highscore.txt") as file:
            self.highscore = int(file.read())

    def update_highscore(self):
        self.highscore = self.score
        with open("./ScoreBoard/highscore.txt", mode='w') as file:
            file.write(f"{self.highscore}")

    def set_highscore(self):
        self.get_highScore()
        self.score_turtle.goto(-350, 350)
        self.score_turtle.write(f"Highscore: {self.highscore}", font=FONT)
