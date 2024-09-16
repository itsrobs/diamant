import turtle as t
from math import sqrt

'''
roter45 grader
tegn firkant
doble lengden på sidene
gå en halv lengde ned
repeat
'''

def firkant(antall):
    def tegn(sider):
        for side in range(sider):
            t.forward(xLengde)
            t.right(vinkel)
    lengde = 40
    xLengde = lengde
    vinkel = 90
    sider = 4
    diagonal = sqrt((lengde**2)+(lengde**2))
    teller = 1
    t.left(45)
    for mengde in range(antall):
        if teller % 2 != 0:
            t.begin_fill()
            tegn(sider)
            t.end_fill()
        else:
            tegn(sider)
        t.penup()
        t.left(90+45)
        t.forward(diagonal/2)
        t.right(90+45)
        xLengde += lengde
        t.pendown()
        teller += 1


    
    
    t.exitonclick()



'''    for menger in range(antall):
        for side in range(sider):
            t.forward(lengde)
            t.left(vinkel)
        t.penup()
        t.right(90+45)
        t.forward(20)
        t.left(90+45)
        lengde = lengde*2
        t.pendown()'''
    




if __name__=="__main__":
    firkant(5)
