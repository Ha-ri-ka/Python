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

game=True
score=0
while game:
    screen.update()
    time.sleep(0.1)    
    snake.move()
    if snake.head.distance(food)<15:
        food.MakeFood(screen)
        snake.Extend()
        score+=1
        ScoreBoard.addScore(score)
    if snake.head.xcor() > x_cord-20 or snake.head.xcor() <-(x_cord-20) or snake.head.ycor() > y_cord-20 or snake.head.ycor() < -(y_cord-20):
        game = False
        ScoreBoard.GameOver()    
    for seg in snake.SnakeBody[1:]:
            if snake.head.distance(seg)<10:
                game=False
                ScoreBoard.GameOver()
screen.exitonclick()