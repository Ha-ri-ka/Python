import turtle as t
import Handles
import Puck
import ScoreBoard
import time

screen=t.Screen()
screen.setup(width=800,height=600)
screen.bgcolor('black')
screen.tracer(0)
maxscore=t.textinput(title=None,prompt="Use up and down arrows to move right handle\nUse w and s keys to move left handle\nEnter number of points youd like to play for:")
if maxscore==None: maxscore=10

puck=Puck.puck()
handles=Handles.handle(screen)
obj=ScoreBoard.Score(screen)
obj.DrawLines()
def HandleCollision():
    if puck.distance(handles.RightHandle)<50 and puck.xcor()>(screen.window_width()//2)-60:
        return True
    if puck.distance(handles.LeftHandle)<30 and puck.xcor()<-(screen.window_width()//2)+50:
        return True
def Right_HandleMiss():
    if puck.distance(handles.RightHandle)>50 and puck.xcor()>(screen.window_width()//2)-15:
        return True
def Left_HandleMiss():
    if puck.distance(handles.LeftHandle)>30 and puck.xcor()<-(screen.window_width()//2)+30:
        return True

screen.listen()
screen.onkey(key='Up',fun=handles.Right_MoveUp)
screen.onkey(key='Down',fun=handles.Right_MoveDown)
screen.onkey(key='w',fun=handles.Left_MoveUp)
screen.onkey(key='s',fun=handles.Left_MoveDown)

game=True
obj.Showscore()
score=0
while game:
    time.sleep(puck.move_speed) 
    screen.update()
    puck.MovePuck()
    if puck.ycor()>280 or puck.ycor()<-280:
        puck.bounce_y() 
    if HandleCollision():    
        puck.bounce_x()
    if Right_HandleMiss():
        obj.Leftscore+=1
        obj.Showscore()
        puck.reset_pos()
    if Left_HandleMiss():
        obj.Rightscore+=1
        obj.Showscore()
        puck.reset_pos()
    if obj.Rightscore==maxscore or obj.Leftscore==maxscore: 
        obj.EndGame()
        game=False    
screen.exitonclick()