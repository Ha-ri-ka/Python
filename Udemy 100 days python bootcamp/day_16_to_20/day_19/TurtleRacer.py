import turtle as t
import random
def MakeTurtle(color,i):
    turt=t.Turtle('turtle')
    turt.color(color)
    turt.penup()
    x=(-t.window_width() / 2)+50
    y=(t.window_height() / 2)-150
    turt.setpos(x,y-i)
    turt.pendown()
    return turt

screen=t.Screen()
screen.setup(width=500,height=600)
colors=['violet','blue','green','yellow','orange','red']
names=['violet','blue','green','yellow','orange','red']
pos=0
for i in range (6):
    names[i]=MakeTurtle(colors[i],pos)
    pos+=50
user_bet=t.textinput(title="Place Bet",prompt="Choose a turtle (violet,blue,green,yellow,orange,red)")
race=True
while race:
    for turtle in names:
        if turtle.xcor()>=220:
            winner=turtle
            if winner.pencolor()==user_bet:
                print(f"YOU WON! {winner.pencolor()} won the race!!")
            else:
                print(f"YOU LOST! {winner.pencolor()} won the race!!")
            race=False                    
        turtle.penup()
        turtle.forward(random.randint(0,10))
        
screen.exitonclick()
