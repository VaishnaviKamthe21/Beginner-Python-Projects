from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("yellow")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(randint(-280,280),randint(-280,280))
