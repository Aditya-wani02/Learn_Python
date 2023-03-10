import time
from turtle import Screen
from Food import Food
from Snake import Snake
from scoreboard import Scoreboard

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")


screen.tracer(0)

# creating snake
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.update()

game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    

# Collision with food 
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        
    #  detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # collision with tail
    for segment in snake.segment[1:]:
        # if segment == snake.head:
        #     pass
        if snake.head.distance( segment) < 10:
            scoreboard.reset()
            snake.reset()

 


    




screen.exitonclick()