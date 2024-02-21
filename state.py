from turtle import Turtle


class State(Turtle):
    def __init__(self):
        super().__init__()
        self.create_state()

    def create_state(self):
        self.speed(1)
        self.shape("circle")
        self.shapesize(stretch_wid=.25)
