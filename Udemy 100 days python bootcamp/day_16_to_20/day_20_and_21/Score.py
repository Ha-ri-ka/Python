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
        self.write("SCORE:0",align=ALIGNMENT,font=(FONT, 15, 'normal'))

    def DrawBorders(self,height,width,screen):
        turt=t.Turtle()
        turt.penup()
        turt.pencolor('white')
        turt.goto(-(width//2)+20,(height//2)+20)
        turt.pendown()
        turt.forward(width-40)        
    def addScore(self,score):
        self.clear()    
        self.write(f"SCORE:{score}",align='Center',font=('Trebuchet MS', 15, 'normal'))
    def GameOver(self):
        self.goto(0,0)
        self.write("GAME OVER",align='Center',font=('Trebuchet MS', 50, 'normal'))
