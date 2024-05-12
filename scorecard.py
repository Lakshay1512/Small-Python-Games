
from turtle import Turtle , Screen
screen = Screen()
screen.tracer(0)
class Scorecard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0,265)
        self.hideturtle()
        self.updatescore()
        screen.update()
        
    def updatescore(self):
        self.write(f"score : {self.score}", align='center',font=('Arial',24,'normal'))

    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER", align='center', font='ARIAL')
        screen.update()

    def addscore(self):
        self.score += 1
        self.clear()
        self.updatescore()
        screen.update()
    
    def scorereset(self):
        self.score = 0
        self.clear
        self.updatescore()
        screen.update()