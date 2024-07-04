from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=1000, height=1000)
screen.bgcolor("black")
screen.title("Snake_game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.Up,"Up")
screen.onkey(snake.Down,"Down")
screen.onkey(snake.Left,"Left")
screen.onkey(snake.Right,"Right")

game_is_on = True
while game_is_on:
    screen.update()  # to update the body
    time.sleep(0.1)  # to delay from one jump to another

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()

    if snake.head.xcor() > 400 or snake.head.xcor() < -400 or snake.head.ycor() >400 or snake.head.ycor() < -400:
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()