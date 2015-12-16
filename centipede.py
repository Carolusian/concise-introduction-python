# centipede.py

from turtle import *

def centipede(length, step, life):
    penup()
    theta = 0
    dtheta = 1
    for i in range(life):
        forward(step)
        left(theta)
        theta += dtheta
        stamp()
        if i > length:
            clearstamps(1)
        if theta > 10 or theta < -10:
            dtheta = -dtheta
        if ycor() > 350:
            left(30)
    
def main():
    setworldcoordinates(-400, -400, 400, 400)
    centipede(14, 10, 200)
    exitonclick()

main()
