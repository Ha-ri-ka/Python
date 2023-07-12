import turtle as t
class CreatePlayer(t.Turtle):
    def __init__(self,screen,color):
        super().__init__()
        self.screen=screen
        self.hideturtle()
        w=self.screen.window_width()
        h=self.screen.window_height()
        self.shape('turtle')
        self.color(color)
        self.penup()
        self.hideturtle()
        self.goto(0,-(h//2)+30)
        self.setheading(90)
        self.showturtle()
        self.speed(10)
    def MoveUp(self):
        h=self.screen.window_height()
        if self.ycor()>=h//2-50: return
        self.forward(20)
    def MoveRight(self):
        self.right(90)
    def MoveLeft(self):
        self.left(90)
    def Reset_position(self):
        h=self.screen.window_height()
        self.goto(0,-(h//2)+30)

