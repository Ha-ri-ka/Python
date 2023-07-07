import turtle as t
import random
import colorgram
artist=t.Turtle()
artist.shape('turtle')
t.colormode(255)
palette=colorgram.extract('[insert path of image]',10)
colors=[]
for i in range(len(palette)):
    colors.append(palette[i].rgb)
artist.hideturtle()
artist.penup()
x = -t.window_width() / 2
y = t.window_height() / 2
artist.setpos(x+50,y-25)
artist.pendown()

for j in range(16):
    if j%2==0 and j!=0:
        artist.left(90)
        artist.penup()
        artist.forward(40)
        artist.left(90)
        artist.forward(50)
    if j%2!=0 and j!=0:
        artist.right(90)
        artist.penup()
        artist.forward(40)
        artist.right(90)
        artist.forward(50)
    for i in range(14):
        artist.dot(15,random.choice(colors))
        artist.penup()
        artist.forward(50)

screen=t.Screen()
screen.exitonclick()
