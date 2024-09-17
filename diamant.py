import turtle as t
from math import sqrt
from random import randint


def firkant(antall=5, colorS="n", lengde=20, vinkel=90, sider=4):

    def tegn(sider):
        for side in range(sider):
            t.forward(xLengde)
            t.right(vinkel)

    xLengde = lengde*antall
    diagonal = sqrt((lengde**2)+(lengde**2))
    counter = antall
    
    color1 = "black"
    color2 = "white"
    
    t.Screen().bgcolor("brown")
    t.speed(0)

    t.setx(-((diagonal/2)*antall))

    t.left(45)
    for mengde in range(antall):
        if colorS.lower() == "y":
            t.colormode(255)
            t.fillcolor(randint(1,255), randint(1,255), randint(1,255))
            t.Screen().bgcolor(randint(1,255), randint(1,255), randint(1,255))
        else:
            t.colormode(1)
            if counter % 2 != 0:
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
        counter -= 1
        t.pendown()
    t.exitonclick()


def main():
    def tall_input(beskjed):
        while True:
            try:
                tall = int(input(beskjed))
                return tall
            except ValueError:
                print("Skriv et gyldig tall...")
            except KeyboardInterrupt:
                print("\nPeace out!")
                exit()
    antall_firkanter = tall_input("Hvor mange diamanter?: ")
    lengde = tall_input("Størrelse: ")
    fargevalg = input("Crazy farge modus? (y/N): ")
    firkant(antall_firkanter,colorS=fargevalg, lengde=lengde)


if __name__=="__main__":
    main()
