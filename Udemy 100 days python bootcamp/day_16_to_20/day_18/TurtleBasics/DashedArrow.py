import turtle as t

kishhi=t.Turtle()
kishhi.shape('turtle')
print("Drawing a dashed arrow")
kishhi.penup()
kishhi.goto(-300,0)
for i in range (12):
    kishhi.penup()
    kishhi.forward(20)
    kishhi.pendown()
    kishhi.forward(20)
kishhi.color('Black')
kishhi.begin_fill()
kishhi.pendown()
kishhi.left(90)
kishhi.forward(20)
for i in range(2):
    kishhi.right(120)
    kishhi.forward(40)
kishhi.right(120)
kishhi.forward(20)
kishhi.end_fill()

screen=t.Screen()
screen.exitonclick()