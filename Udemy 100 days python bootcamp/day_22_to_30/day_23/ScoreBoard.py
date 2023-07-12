import turtle as t
import time
FONT="Courier New"
FONTSIZE=20
class Score(t.Turtle):
    def __init__(self,color):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.penup()
        self.setpos((-t.window_width() / 2)+30,(t.window_height() / 2)-50)
        self.pendown()
        self.pencolor(color)

    def ShowLevel(self):
        self.clear()
        self.write(f"Level:{self.level}",font=(FONT,FONTSIZE,"normal"))
    def endgame(self):
        self.goto(0,0)
        self.write("GAME OVER",font=(FONT,30,"normal"),align="center")

