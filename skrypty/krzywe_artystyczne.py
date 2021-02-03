import turtle
import math
import numpy as np
wn = turtle.Screen()

alex = turtle.Turtle()
alex.speed(200)
alex.hideturtle()

def pursuit_curve(n, l_0, x):
    """
      Rysuj krzywe pościgowe w wielokącie foremnym
      :param n: ilość boków
      :param l_0: długość boku
      :param x: odcinek przesunięcia
      """
    i = 0
    base_angle = ((n-2) * 180)/n

    while i <100:



        l = np.sqrt(x**2 + (l_0 - x)**2 - 2*x*(l_0-x)*np.cos(math.radians(base_angle))) #tw cosinusów
        angle = (180* np.arcsin((np.sin(math.radians(base_angle))*x)/l))/np.pi #tw sinusów

        if round(l_0) == round(l):
            break

        for _ in range(n):
            alex.forward(l_0)
            alex.left(180-base_angle)

        alex.up()
        alex.forward(x)
        alex.down()
        alex.left(angle)

        l_0 = l
        i += 1




def join(arg, l_0,x):


    if arg=="6triangles":
        for i in range(int(arg[0])):
            alex.up()
            alex.goto((0, 0))
            alex.down()
            pursuit_curve(3, l_0, x)
            alex.setheading((i+1)*60)

    if arg=="9triangles":
        pos = [(l_0/2, -1*l_0 * math.sqrt(3) /2), (-3*l_0/2, -1*l_0 * math.sqrt(3) /2), (-1*l_0/2, l_0 * math.sqrt(3) /2)]
        for i in range(int(arg[0])-3):
            alex.up()
            alex.goto((0, 0))
            alex.down()
            pursuit_curve(3, l_0, x)
            alex.setheading((i + 1) * 60)

        alex.setheading(0)
        for i in range(3):
            alex.up()
            alex.goto((0,0))
            alex.goto(pos[i])
            alex.down()
            pursuit_curve(3, l_0, x)
            alex.setheading(0)


    if arg=="4squares":
        pos = [(-1, 0), (0,0), (-1,-1), (0,-1)]
        for i in range(int(arg[0])):
            alex.up()
            alex.goto((pos[i][0] *l_0, pos[i][1]*l_0))
            alex.down()
            pursuit_curve(4, l_0, x)
            alex.setheading(0)

    if arg=="9squares":
        pos = [(-3/2, 1/2), (-1/2, 1/2), (1/2,1/2), (-3/2, -1/2), (-1/2, -1/2), (1/2,-1/2), (-3/2, -3/2), (-1/2, -3/2), (1/2,-3/2)]
        for i in range(int(arg[0])):
            alex.up()
            alex.goto((pos[i][0] *l_0, pos[i][1]*l_0))
            alex.down()
            pursuit_curve(4, l_0, x)
            alex.setheading(0)


def main():
    join("9triangles", 150, 10)
    alex.getscreen().getcanvas().postscript(file='9squares.ps')
    wn.exitonclick()

main()


