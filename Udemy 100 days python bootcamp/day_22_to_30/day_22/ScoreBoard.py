import turtle as t
FONT="Trebuchet MS"
FONTSIZE=45
class Score():
    def __init__(self,screen):
        self.screen=screen
        w=self.screen.window_width()
        h=self.screen.window_height()
        self.Rightscore=0
        self.Leftscore=0
        self.LeftTurtle=self.MakeTurtles(-70,h//2-70)
        self.RightTurtle=self.MakeTurtles(40,h//2-70)

    def DrawLines(self):
        w=self.screen.window_width()
        h=self.screen.window_height()
        self=t.Turtle()
        self.pensize(5)
        self.hideturtle()
        self.pencolor('white')
        self.penup()
        self.goto(0,h//2)
        self.setheading(-90)
        for i in range(h):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
    
    def MakeTurtles(self,x,y):
        new_turt=t.Turtle()
        new_turt.hideturtle()
        new_turt.pencolor('white')
        new_turt.penup()
        new_turt.goto(x,y)
        new_turt.pendown()
        return new_turt
    
    def Showscore(self):        
        self.LeftTurtle.clear()
        self.RightTurtle.clear()
        self.LeftTurtle.write(self.Leftscore,font=(FONT,FONTSIZE,"normal"))        
        self.RightTurtle.write(self.Rightscore,font=(FONT,FONTSIZE,"normal"))
    
    def EndGame(self):
        turt=t.Turtle()
        turt.goto(0,0)
        turt.pencolor('red')
        if self.Rightscore > self.Leftscore: winner="RIGHT PLAYER"
        if self.Rightscore < self.Leftscore: winner="LEFT PLAYER"
        turt.write(f"{winner} WINS THE GAME!",align='Center',font=('Trebuchet MS', 30, 'normal'))
        turt.goto(turt.xcor(),turt.ycor()+50)
        turt.write("GAME OVER",align='Center',font=('Trebuchet MS', 30, 'normal'))




