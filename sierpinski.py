# sierpinski.py

from turtle import Turtle, setworldcoordinates, exitonclick

class SierpinskiTriangle(Turtle):
    size = 2
    def __init__(self, n, x, y):
        Turtle.__init__(self, visible=False)
        self.n = n
        self.speed(0)
        self.penup()
        self.goto(x, y)
        
    def draw(self):
        if self.n == 0:
            self.begin_fill()
            for i in range(3):
                self.forward(SierpinskiTriangle.size)
                self.left(120)
            self.end_fill()
        else:
            for i in range(3):
                SierpinskiTriangle(self.n - 1,
                                   self.xcor(),
                                   self.ycor()).draw()
                self.forward(SierpinskiTriangle.size ** self.n)
                self.left(120)
        
def main():
    setworldcoordinates(0, 0, 75, 75)
    SierpinskiTriangle(5, 5, 5).draw()
    exitonclick()
    
if __name__ == "__main__":
    main()
