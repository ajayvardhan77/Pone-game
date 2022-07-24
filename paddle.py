from turtle import Turtle


# TODO: 2.create a paddle
class Paddle(Turtle):  # inherit turtle(superclass) in paddle class : paddle class now can use all turtle methods.

    def __init__(self, position):
        super().__init__()  # should mention super().__init__() whn your inheriting.
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)  # tuple is passed as the input to the goto method.

    def go_up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)
