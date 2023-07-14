import turtle as t
ALIGNMENT='Center'
FONT='Trebuchet MS'
class ScoreBoard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.hideturtle()
        self.pencolor('white')
        self.goto(0,270)
        self.pendown()
    def ReadFile(self):
        with open("D:/python/udemy/DAY_11_TO_20/day20/Snake_file.txt",mode="r") as file:
            contents=int(file.read())
        return contents    
    def ShowScore(self):
        contents=self.ReadFile()
        self.clear() 
        self.write(f"SCORE:{self.score}    HIGH SCORE:{contents}",align='Center',font=('Trebuchet MS', 15, 'normal'))

    def reset_game(self):
        if self.score>self.ReadFile():
            with open("D:/python/udemy/DAY_11_TO_20/day20/Snake_file.txt",mode="w+") as file:
                file.write(str(self.score))
        self.score=0
        self.ShowScore()    
        
    def GameOver(self):
        self.goto(0,0)
        self.write("GAME OVER",align='Center',font=('Trebuchet MS', 50, 'normal'))
