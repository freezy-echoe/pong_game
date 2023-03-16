from turtle import Turtle

PADDLE_POSITIONS = [(350, 0), (-350, 0)]


class Paddle(Turtle):
    def __init__(self, cor):
        super().__init__()
        self.cordinate = cor
        self.paddle = self.add_paddle(self.cordinate)


    def add_paddle(self, position):

        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        return self


    def go_up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)