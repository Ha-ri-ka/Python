import turtle as t
import random
MOVE_SPEED=5  
class obstacle(t.Turtle):
    def __init__(self,screen):
        self.screen=screen
        self.all_cars=[]
    def CreateCar(self):
        w=self.screen.window_width()
        h=self.screen.window_height()
        max_ycord=h//2-70
        min_ycord=-(h//2)+90
        y=random.randint(min_ycord,max_ycord)
        t.colormode(255)
        random_chance=random.randint(1,6)
        if random_chance==1:
            car=t.Turtle('square')
            car.penup()
            car.goto(w//2,y)
            car.setheading(180)
            car.shapesize(stretch_len=2)
            car.color((random.randint(0,255)),(random.randint(0,255)),(random.randint(0,255)))
            self.all_cars.append(car)   
    def MoveCar(self):
        for c in self.all_cars:
            c.forward(MOVE_SPEED)
    def SpeedUp(self):
        global MOVE_SPEED
        MOVE_SPEED+=5


           
        
