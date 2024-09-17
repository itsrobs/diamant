import turtle as t
from math import sqrt
from random import randint

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
    
    color1 = "black"
    color2 = "white"
    
    colorS = "r"

    t.Screen().bgcolor("black")
    t.speed(0)

    t.setx(-((diagonal/2)*antall))

    t.left(45)
    for mengde in range(antall):
        if colorS.lower() == "r":
            t.colormode(255)
            t.fillcolor(randint(1,255), randint(1,255), randint(1,255))
        else:
            t.colormode(1)
            if counter % 2 == 0:
                t. fillcolor(color1)
            else:
                t.fillcolor(color2)
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
    firkant(50)
