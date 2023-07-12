import turtle as t
import PlayerTurtle
import Cars
import time
import ScoreBoard

screen=t.Screen()
screen.setup(width=600,height=600)
mode=screen.textinput(title=None,prompt="Dark Mode or Light Mode?").lower()
if mode=="light":
    screen.bgcolor('white')
    display_Color='black'
else: 
    screen.bgcolor('black')
    display_Color='white'
screen.tracer(0)
h=screen.window_height()
w=screen.window_width()

Player=PlayerTurtle.CreatePlayer(screen,display_Color)
car_manager=Cars.obstacle(screen)
Display=ScoreBoard.Score(display_Color)

screen.listen()
screen.onkey(key='Up',fun=Player.MoveUp)
screen.onkey(key='Right',fun=Player.MoveRight)
screen.onkey(key='Left',fun=Player.MoveLeft)
Display.ShowLevel()
game=True    
while game:
    time.sleep(0.1)
    screen.update()
    car_manager.CreateCar()
    car_manager.MoveCar()
    for obstacle in car_manager.all_cars:
        if obstacle.distance(Player)<20:
            Display.endgame()
            game=False
    if Player.ycor()>=h//2-50:
        Player.Reset_position()
        Display.level+=1
        Display.ShowLevel()
        car_manager.SpeedUp()

screen.exitonclick()
