import turtle as t

kishhi=t.Turtle()
kishhi.shape('turtle')
print("Drawing a square")
kishhi.pencolor('DarkMagenta')
kishhi.speed(1)
for i in range(4):
    kishhi.forward(100)
    kishhi.left(90)

screen=t.Screen()
screen.exitonclick()
