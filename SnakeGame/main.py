from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# Screen Object
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)
screen.title("Snake Game")

# Snake Object
snake = Snake()

# Food Object
food = Food()

# Scoreboard Object
scoreboard = ScoreBoard()

# Game start trigger
game_is_on = True

# Screen listen on
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Starting the Game
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Eating Process
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.update_score()

    # Wall Collision
    if snake.snake_x_cor() == 280 or snake.snake_y_cor() == 280:
        game_is_on = False
        scoreboard.game_over()

    # Head Collision
    for part in snake.snake_body[1:len(snake.snake_body)]:
        if snake.head.distance(part) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
