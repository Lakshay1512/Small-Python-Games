from turtle import Turtle , Screen
import time

screen = Screen()
screen.tracer(0)

class Snake():
    def __init__(self):
        self.list = []
        self.CreateSnake()

    def CreateSnake(self):
        for n in range(3):
            segment = Turtle('square')
            segment.color('white')
            segment.penup()
            segment.setx(n*(-20))
            (self.list).append(segment)
            screen.update() 

    def forward(self):

        list_of_positions = []
        for n in self.list:
            a = n.pos()
            list_of_positions.append(a)
        for n in range(1,len(self.list)):
            self.list[n].goto(list_of_positions[n-1])

        self.list[0].forward(20)
        time.sleep(0.1)
        screen.update()
    
    def up(self):
        if self.list[0].heading() != 270:
            self.list[0].setheading(90)

    def down(self):
        if self.list[0].heading() != 90:
            self.list[0].setheading(270)

    def left(self):
        if self.list[0].heading() != 0:
            self.list[0].setheading(180)

    def right(self):
        if self.list[0].heading() != 180:
            self.list[0].setheading(0)

    def add(self):
        a,b = self.list[-1].pos()
        segment = Turtle('square')
        segment.setposition(a,b)
        segment.penup()
        segment.color('white')
        segment.penup()
        (self.list).append(segment)
              
