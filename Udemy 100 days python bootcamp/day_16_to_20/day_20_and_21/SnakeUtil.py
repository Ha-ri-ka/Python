import turtle as t
MOVE=20
class snake:
    def __init__(self):
        pos=(0,0)
        self.SnakeBody=[]
        for _ in range(3):
            self.AddSegment(pos)
            pos=(pos[0]-20,0)            
        self.head=self.SnakeBody[0]

    def AddSegment(self,pos):
        part=t.Turtle('square')
        part.color('white')
        part.penup()
        part.goto(pos)
        self.SnakeBody.append(part)

    def Extend(self):
        self.AddSegment(self.SnakeBody[-1].position())

    def move(self):
        for i in range (len(self.SnakeBody)-1,0,-1):
            new_x=self.SnakeBody[i-1].xcor()
            new_y=self.SnakeBody[i-1].ycor()
            self.SnakeBody[i].goto(new_x,new_y)
        self.SnakeBody[0].forward(MOVE)
    def moveUp(self):
        if self.head.heading()==270: return
        self.head.setheading(90)
    def moveLeft(self):
        if self.head.heading()==0: return
        self.head.setheading(180)
    def moveRight(self):
        if self.head.heading()==180: return
        self.head.setheading(0)
    def moveDown(self):
        if self.head.heading()==90: return
        self.head.setheading(-90)        
