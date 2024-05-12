
import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        self.foodConstruction()

    def foodConstruction(self):
        self.food = Turtle('circle')
        self.food.color('green')
        self.food.penup()
        self.food.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.food.goto(random.randint(-280,280),random.randint(-280,280))

    def changepos(self):
        self.food.goto(random.randint(-280,280),random.randint(-280,280))
