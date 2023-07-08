import turtle as t
turti=t.Turtle()
screen=t.Screen()
turti.shape('turtle')
print("UP arrow to move forward\n")
print("\nDOWN arraw to move backward\n")
print("\nRIGHT arrow to move right\n")
print("\nLEFT arrow to move left\n")
print("\n'c' to clear screen.\n")
print("\n'u' to undo.\n")
print("\n'm' to move turtle to a position.\n")
print("\n'd' to start drawing after move.\n")
#-------------------------------------------------------------------
def forward():
    turti.forward(20)
def backward():
    turti.backward(20)
def right():
    turti.right(10)
def left():
    turti.left(10)
def clear():
    turti.reset()
def move():
    turti.penup()
def draw():
    turti.pendown()
def undo():
    turti.undo()

screen.listen()
screen.onkey(key="Up" or "Space",fun=forward)
screen.onkey(key="Down",fun=backward)
screen.onkey(key="Right",fun=right)
screen.onkey(key="Left",fun=left)
screen.onkey(key="c",fun=clear)
screen.onkey(key="m",fun=move)
screen.onkey(key="d",fun=draw)
screen.onkey(key="u",fun=undo)

screen.exitonclick()
