from turtle import Turtle , Screen
screen = Screen()

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,265)
        self.write(f"score : {0000000}", align='center',font=('Arial',24,'normal'))
