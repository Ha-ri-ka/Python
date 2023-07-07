import turtle as t
import random

def RandomColor():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)

torti=t.Turtle()
torti.shape('turtle')
t.colormode(255)
torti.speed("fastest")
for _ in range(72):
    torti.pencolor(RandomColor())
    torti.circle(radius=100)
    torti.right(5)

    
screen=t.Screen()
screen.exitonclick()
