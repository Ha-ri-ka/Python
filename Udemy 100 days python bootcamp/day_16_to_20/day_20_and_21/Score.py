import turtle as t
ALIGNMENT='Center'
FONT='Trebuchet MS'
class ScoreBoard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.pencolor('white')
        self.goto(0,270)
        self.pendown()
        
    def addScore(self,score):
        self.clear()    
        self.write(f"SCORE:{score}",align=ALIGNMENT,font=(FONT, 15, 'normal'))
        
    def GameOver(self):
        self.goto(0,0)
        self.write("GAME OVER",align='Center',font=('Trebuchet MS', 50, 'normal'))
