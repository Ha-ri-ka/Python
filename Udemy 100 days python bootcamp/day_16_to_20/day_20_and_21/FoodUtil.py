import turtle as t
import random
class food(t.Turtle):
    def __init__(self,screen):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.5,0.5)
        self.color('Magenta')
        self.speed('fastest')
        w=screen.window_width()
        h=screen.window_height()
        self.goto(random.randint(-w/2+20,w/2-20),random.randint(-h/2+20,h/2-20))

    def MakeFood(self,screen):
        w=screen.window_width()
        h=screen.window_height()
        self.goto(random.randint(-w/2+20,w/2-20),random.randint(-h/2+20,h/2-20))        