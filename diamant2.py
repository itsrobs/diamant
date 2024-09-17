import turtle as t
from math import sqrt
import random

def firkant(antall):

    def tegn(sider):
        for side in range(sider):
            t.forward(xLengde)
            t.right(vinkel)

    
    lengde = 20
    xLengde = lengde*antall
    vinkel = 90
    sider = 4
    diagonal = sqrt((lengde**2)+(lengde**2))
    counter = 1
    t.speed(10)
    t.Screen().bgcolor("black")
    colorS = "r"

    t.left(45)
    for mengde in range(antall):
        if colorS == "r":
            t.colormode(255)
            t.fillcolor(random.randint(1,255), random.randint(1,255), random.randint(1,255))
        else:
            if counter % 2 != 0:
                t.colormode(1)
                t. fillcolor("black")
            else:
                t.colormode(1)
                t.fillcolor("white")
        t.begin_fill()
        tegn(sider)
        t.end_fill()
        t.penup()
        t.right(45)
        t.forward(diagonal/2)
        t.left(45)
        xLengde -= lengde
        counter += 1
        t.pendown()
    t.exitonclick()




if __name__=="__main__":
    firkant(10)
