from turtle import Turtle,Screen
import random
import time
from snakeclass import Snake
from foodclass import Food
from scorecard import Scorecard
score = Scorecard()
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

khana = Food()
food = khana.food

screen.update()
screen.listen()

snake = Snake()

gameison = True
while gameison:
    screen.update()
    snake.forward()

    screen.onkey(snake.up,'Up')
    screen.onkey(snake.down,'Down')
    screen.onkey(snake.left,'Left')
    screen.onkey(snake.right,'Right')

    (x,y) = snake.list[0].pos()
    (a,b) = food.pos()

    if x >= (290.0) or x <= (-290.0):
        gameison = False
        score.gameover()
        again = screen.textinput('Game Over', 'You Want to play again or not' ) 
        if again == 'no':
            screen.bye()
        if again == 'yes':
            snake.list[0].setx(0)
            continue
    if y >= (290.0) or y <= (-290.0):
        gameison = False
        score.gameover()
        again = screen.textinput('Game Over', 'You Want to play again or not' ) 
        if again == 'no':
            screen.bye()
        if again == 'yes':
            snake.list[0].setx(0)
            continue
    for segment in snake.list:
        if snake.list[0].distance(segment.pos()) < (0.5):
            if segment == snake.list[0]:
                pass
            else:
                gameison = False
                score.gameover()
   
    if snake.list[0].distance(a,b)<=15.0 :
        khana.changepos()
        score.addscore()
        snake.add()
        screen.update()
        continue

    screen.update()

screen.exitonclick()