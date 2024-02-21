from turtle import Turtle


class Map(Turtle):
    def __init__(self):
        super().__init__()
        self.create_map()

    def create_map(self):
        self.shape("blank_states_img.gif")

