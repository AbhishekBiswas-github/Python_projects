import random
from turtle import Turtle

# CONSTANTS
FOOD_COLOR = 'green'
FOOD_SHAPE = 'turtle'
FOOD_FACE = 90


# Food Class
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color(FOOD_COLOR)
        self.shape(FOOD_SHAPE)
        self.setheading(FOOD_FACE)
        self.speed('fastest')
        self.refresh()

    # Put food in different coordinates every time.
    def refresh(self):
        random_x = random.randint(-260, 260)
        random_y = random.randint(-260, 260)
        self.goto(random_x, random_y)
