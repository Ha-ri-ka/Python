import turtle as t
import random

kishhi=t.Turtle()
kishhi.shape('turtle')

print("Drawing a very weird design.")
colors = ['red', 'blue', 'green', 'orange', 'yellow', 'purple', 'pink', 'brown', 'black', 'gray']
for sides in range(3,11):
    kishhi.pencolor(random.choice(colors))
    for i in range(sides):
        kishhi.forward(100)
        kishhi.left(360//sides)
    sides+=1

screen=t.Screen()
screen.exitonclick()