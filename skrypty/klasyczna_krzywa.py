import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

def get_dataA(times, vA, xsB, ysB, tick):
    """
    Funkcja obliczająca współrzędne (x, y) obiektu goniącego.

    :param times: lista czasów
    :param vA: prędkość obiektu
    :param xsB: lista współrzędnych x obiektu uciekającego
    :param ysB: lista współrzędnych y obiektu uciekającego
    :param tick: krok czasowy
    :return: xs, ys
    """
    xs, ys = [], []
    for time in times:
        if time == 0:
            xs.append(0)
            ys.append(0)
        else:
            xA = xs[-1]
            yA = ys[-1]

            i = 0
            while times[i] != time:
                i += 1

            xB = xsB[i-1]
            yB = ysB[i-1]

            c = math.sqrt((yB-yA)**2 + (xB-xA)**2)

            xs.append(xA + (xB - xA)*vA*tick/c)
            ys.append(yA + (yB - yA)*vA*tick/c)

    return xs, ys


def get_dataB_classic(times, x0, vB):
    """
    Funkcja obliczająca współrzędne (x, y) obiektu uciekającego po linii prostej.

    :param times: lista czasów
    :param x0: odległość obiektu od osi Oy
    :param vB: prędkość obiektu
    :return: xs, ys
    """
    xs, ys = [], []
    for time in times:
        xs.append(x0)
        ys.append(vB*time)

    return xs, ys


def classic_curve(x0, vA, vB):
    """
    Funkcja tworząca animację pościgu.

    :param x0: położenie środka okręgu
    :param vA: prędkość obiektu goniącego
    :param vB: prędkość obiektu uciekającego
    :return: animacja
    """

    fig, ax = plt.subplots()
    xdataB, xdataA, ydataB, ydataA, xdataB2, xdataA2, ydataB2, ydataA2 = [], [], [], [], [0], [0], [0], [0]
    lnB, = plt.plot([], [], 'r', animated=True)
    lnB2, = plt.plot([], [], 'r', marker='o', animated = True)
    lnA, = plt.plot([], [], 'b', animated=True)
    lnA2, = plt.plot([], [], 'b', marker='o', animated=True)

    MAX_TIME = x0/(vA*(1 - (vB/vA)**2))
    NUMBER_OF_TIMES = 200

    times = np.linspace(0, MAX_TIME, NUMBER_OF_TIMES)

    xsB, ysB = get_dataB_classic(times, x0, vB)
    xsA, ysA = get_dataA(times, vA, xsB, ysB, MAX_TIME/NUMBER_OF_TIMES)

    def init():
        ax.set_xlim(0, x0 + 1)
        ax.set_ylim(0, vB*MAX_TIME + 1)
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_title("Klasyczna krzywa pogoni")
        lnB.set_data(xdataB, ydataB)
        lnA.set_data(xdataA, ydataA)
        lnB2.set_data(xdataB2, ydataB2)
        lnA2.set_data(xdataA2, ydataA2)
        return lnB, lnA, lnB2, lnA2


    def update(frame):
        i = 0
        while times[i] != frame:
            i += 1

        xdataB.append(xsB[i])
        xdataA.append(xsA[i])
        ydataB.append(ysB[i])
        ydataA.append(ysA[i])
        xdataB2[0] = xsB[i]
        xdataA2[0] = xsA[i]
        ydataB2[0] = ysB[i]
        ydataA2[0] = ysA[i]
        lnB.set_data(xdataB, ydataB)
        lnA.set_data(xdataA, ydataA)
        lnB2.set_data(xdataB2, ydataB2)
        lnA2.set_data(xdataA2, ydataA2)
        return lnB, lnA, lnB2, lnA2,

    ani = FuncAnimation(fig, update, frames=times,
                        init_func=init, blit=True, interval=2.5, repeat=False)

    # writer = PillowWriter(fps=25)
    # ani.save("classic_pursuit.gif", writer=writer)

    plt.show()


if __name__ == '__main__':
    classic_curve(6, 2, 1)