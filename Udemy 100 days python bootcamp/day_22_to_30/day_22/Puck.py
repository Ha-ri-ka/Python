import turtle as t
import random
class puck(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.speed(10)
        self.x_move=10
        self.y_move=10
    def reset_pos(self):
        self.goto(0,0) 
    def MovePuck(self):
        x=self.xcor()+self.x_move
        y=self.ycor()+self.y_move
        self.goto(x,y)
    def bounce_y(self):
        self.y_move*=-1
    def bounce_x(self):
        self.x_move*=-1










