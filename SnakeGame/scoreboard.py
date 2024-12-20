from turtle import Turtle

# CONSTANTS
ALIGN = 'center'
FONT_FAMILY = 'Courier'
FONT_SIZE = 18
FONT_TYPE = 'normal'


# Scoreboard Class
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()

    # Updating scoreboard text
    def update_scoreboard(self):
        self.write(f"Score: {self.score} ", align=ALIGN, font=(FONT_FAMILY, FONT_SIZE, FONT_TYPE))

    # Game Over Text
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align=ALIGN, font=(FONT_FAMILY, FONT_SIZE, FONT_TYPE))

    # Updating score every time the snake eats food
    def update_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
