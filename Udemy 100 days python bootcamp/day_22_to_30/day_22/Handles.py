import turtle as t
MOVE=30
class handle(t.Turtle):
    def __init__(self,screen):
        w=screen.window_width()
        h=screen.window_height()
        self.screen=screen
        self.LeftHandle=self.MakeHandle(-(w//2)+20,0)
        self.RightHandle=self.MakeHandle((w//2)-30,0)      
    
    def MakeHandle(self,x,y):
        Handle=t.Turtle('square')
        Handle.color('white')
        Handle.hideturtle()
        Handle.penup()
        Handle.shapesize(stretch_wid=5,stretch_len=1)
        Handle.goto(x,y)
        Handle.showturtle()     
        return Handle    
    
    def Right_MoveUp(self):
        if self.RightHandle.ycor()>=(self.screen.window_height()//2-60): return
        self.RightHandle.goto(self.RightHandle.xcor(),self.RightHandle.ycor()+20)
    def Right_MoveDown(self):
        if self.RightHandle.ycor()<=(-(self.screen.window_height()//2)+60): return
        self.RightHandle.goto(self.RightHandle.xcor(),self.RightHandle.ycor()-20)
    def Left_MoveUp(self):
        if self.LeftHandle.ycor()>=(self.screen.window_height()//2-60): return
        self.LeftHandle.goto(self.LeftHandle.xcor(),self.LeftHandle.ycor()+20)
    def Left_MoveDown(self):
        if self.LeftHandle.ycor()<=(-(self.screen.window_height()//2)+60): return
        self.LeftHandle.goto(self.LeftHandle.xcor(),self.LeftHandle.ycor()-20)
        





