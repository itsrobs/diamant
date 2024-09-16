import turtle as t
from math import sqrt
import random

def firkant(antall):

    def tegn(sider):
        for side in range(sider):
            t.forward(xLengde)
            t.right(vinkel)

    
    lengde = 40
    xLengde = lengde*antall
    vinkel = 90
    sider = 4
    diagonal = sqrt((lengde**2)+(lengde**2))
    t.speed(20)
    t.Screen().bgcolor("black")

    t.left(45)
    for mengde in range(antall):
        t.colormode(255)
        t.fillcolor(random.randint(1,255), random.randint(1,255), random.randint(1,255))
        t.begin_fill()
        tegn(sider)
        t.end_fill()
        t.penup()
        t.right(45)
        t.forward(diagonal/2)
        t.left(45)
        xLengde -= lengde
        t.pendown()
    t.exitonclick()




if __name__=="__main__":
    firkant(5)
