import turtle as t
import random 
torto=t.Turtle()
torto.shape('turtle')
torto.pensize(10)
stepSize=30

angles=[0,90,180,270]
def goLeft():
    torto.left(random.choice(angles))
    torto.forward(stepSize)

def goRight():
    torto.right(random.choice(angles))
    torto.forward(stepSize)

directions=[torto.forward,torto.back,goLeft,goRight]
colors=['gold', 'turquoise', 'blue', 'teal', 'green', 'orange', 'purple', 'brown', 'lime', 'magenta']
for i in range(90):
    torto.pencolor(random.choice(colors))
    execute=random.choice(directions)
    if execute==torto.forward or execute==torto.back: execute(stepSize)
    else: execute()
screen=t.Screen()
screen.exitonclick()
