import turtle as t
import time
import SnakeUtil
import FoodUtil
import Score    
 
screen=t.Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)
w=screen.window_width()
h=screen.window_height()
x_cord=w//2
y_cord=h//2

snake=SnakeUtil.snake()
food=FoodUtil.food(screen)
ScoreBoard=Score.ScoreBoard()

screen.listen()
screen.onkey(key='Up',fun=snake.moveUp)
screen.onkey(key='Right',fun=snake.moveRight)
screen.onkey(key='Left',fun=snake.moveLeft)
screen.onkey(key='Down',fun=snake.moveDown)
ScoreBoard.ShowScore()
game=True
while game:
    screen.update()
    time.sleep(0.1)    
    snake.move()
    if snake.head.distance(food)<15:
        food.MakeFood(screen)
        snake.Extend()
        ScoreBoard.score+=1
        ScoreBoard.ShowScore()
    if snake.head.xcor() > x_cord-20 or snake.head.xcor() <-(x_cord-20) or snake.head.ycor() > y_cord-20 or snake.head.ycor() < -(y_cord-20):
        choice=screen.textinput(title="enter choice",prompt="Continue Playing? (y/n)").lower()
        if choice=="y":
            ScoreBoard.reset_game()
            snake.resetSnake()
            screen.listen()
        else:
             ScoreBoard.GameOver()
             game=False
    for seg in snake.SnakeBody[1:]:
            if snake.head.distance(seg)<10:
                choice=screen.textinput(title="enter choice",prompt="Continue Playing? (y/n)").lower()
                if choice=="y":
                    ScoreBoard.reset_game()
                    snake.resetSnake()
                    screen.listen()
                else:
                    ScoreBoard.GameOver()
                    game=False
screen.exitonclick()