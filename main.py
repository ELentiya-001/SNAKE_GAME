import turtle
import Snake
import food
import scoreboard

game_is_on = True

screen = turtle.Screen()
screen.bgcolor('black')
screen.title('SNAKE GAME')
screen.setup(width=600, height=600)
screen.tracer(0)

snake = Snake.Snakes()
food = food.Food()
scoreboard = scoreboard.Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

while game_is_on:
    screen.update()
    snake.move()

    # detect collision with food
    if snake.snake_parts[0].distance(food) < 15:
        print("mom nom nom")
        food.refresh()
        snake.extend_snake()
        scoreboard.increase_score()

    # detect collision with wall and game over
    if snake.snake_parts[0].xcor() > 280 or snake.snake_parts[0].xcor() < -300 or snake.snake_parts[0].ycor() > 300 or snake.snake_parts[0].ycor() < -280:
        print("collision  and snake died ")
        # game_is_on = False
        snake.reset_snake()
        scoreboard.game_over()

    # detect collision with tail
    for parts in snake.snake_parts:
        if parts == snake.snake_parts[0]:
            pass
        elif snake.snake_parts[0].distance(parts) < 10:
            # game_is_on = False
            snake.reset_snake()
            scoreboard.game_over()

screen.exitonclick()