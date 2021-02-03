import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import PillowWriter
import math
import random


def mice_pursuit_square(v, r):
    """
    Funkcja tworząca animację pościgu wewnątrz kwadratu.
    :return: animacja
    """

    fig, ax = plt.subplots()
    ax.axis('off')
    xdataA, ydataA, xdataA2, ydataA2 = [], [], [0], [0]
    xdataB, ydataB, xdataB2, ydataB2 = [], [], [0], [0]
    xdataC, ydataC, xdataC2, ydataC2 = [], [], [0], [0]
    xdataD, ydataD, xdataD2, ydataD2 = [], [], [0], [0]
    ln1, = plt.plot([], [], color='black', animated=True, linewidth=0.8)
    ln2, = plt.plot([], [], color='black', animated=True, linewidth=0.8)
    ln3, = plt.plot([], [], color='black', animated=True, linewidth=0.8)
    ln4, = plt.plot([], [], color='black', animated=True, linewidth=0.8)

    lnA, = plt.plot([], [], color='#abcae4', animated=True)
    lnA2, = plt.plot([], [], color='#abcae4', marker='o', animated=True)
    lnB, = plt.plot([], [], color='#619bcc', animated=True)
    lnB2, = plt.plot([], [], color='#619bcc', marker='o', animated = True)
    lnC, = plt.plot([], [], color='#316a9a', animated=True)
    lnC2, = plt.plot([], [], color='#316a9a', marker='o', animated=True)
    lnD, = plt.plot([], [], color='#193750', animated=True)
    lnD2, = plt.plot([], [], color='#193750', marker='o', animated=True)

    MAX_TIME = 10
    NUMBER_OF_TIMES = 200

    times = np.linspace(0, MAX_TIME, NUMBER_OF_TIMES)
    tick = MAX_TIME/NUMBER_OF_TIMES

    # xsA, ysA = [random.uniform(0, r/2)], [random.uniform(0, r/2)]
    # xsB, ysB = [random.uniform(r/2, r)], [random.uniform(0, r/2)]
    # xsC, ysC = [random.uniform(r/2, r)], [random.uniform(r/2, r)]
    # xsD, ysD = [random.uniform(0, r/2)], [random.uniform(r/2, r)]

    xsA, ysA = [0], [0]
    xsB, ysB = [r], [0]
    xsC, ysC = [r], [r]
    xsD, ysD = [0], [r]

    for i in range(len(times)-1):
        c = math.sqrt((ysB[i] - ysA[i]) ** 2 + (xsB[i] - xsA[i]) ** 2)
        xsA.append(xsA[i] + (xsB[i] - xsA[i]) * v * tick / c)
        ysA.append(ysA[i] + (ysB[i] - ysA[i]) * v * tick / c)

        c = math.sqrt((ysC[i] - ysB[i]) ** 2 + (xsC[i] - xsB[i]) ** 2)
        xsB.append(xsB[i] + (xsC[i] - xsB[i]) * v * tick / c)
        ysB.append(ysB[i] + (ysC[i] - ysB[i]) * v * tick / c)

        c = math.sqrt((ysD[i] - ysC[i]) ** 2 + (xsD[i] - xsC[i]) ** 2)
        xsC.append(xsC[i] + (xsD[i] - xsC[i]) * v * tick / c)
        ysC.append(ysC[i] + (ysD[i] - ysC[i]) * v * tick / c)

        c = math.sqrt((ysA[i] - ysD[i]) ** 2 + (xsA[i] - xsD[i]) ** 2)
        xsD.append(xsD[i] + (xsA[i] - xsD[i]) * v * tick / c)
        ysD.append(ysD[i] + (ysA[i] - ysD[i]) * v * tick / c)


    counter = 0
    for i in range(NUMBER_OF_TIMES):
        counter+=1
        if abs(xsA[i] - xsB[i]) < 0.05 and abs(ysA[i] - ysB[i]) < 0.05:
            break

    times = np.linspace(0, MAX_TIME*counter/NUMBER_OF_TIMES, counter)
    xsA, ysA = xsA[0:counter], ysA[0:counter]
    xsB, ysB = xsB[0:counter], ysB[0:counter]
    xsC, ysC = xsC[0:counter], ysC[0:counter]
    xsD, ysD = xsD[0:counter], ysD[0:counter]

    xs1, ys1 = [0, r], [0, 0]
    xs2, ys2 = [r, r], [0, r]
    xs3, ys3 = [0, r], [r, r]
    xs4, ys4 = [0, 0], [0, r]

    def init():
        ax.set_xlim(-1, r + 1)
        ax.set_ylim(-1, r + 1)
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_title("Krzywa pogoni wewnątrz kwadratu")
        ax.set_aspect(aspect='equal')
        lnA.set_data(xdataA, ydataA)
        lnB.set_data(xdataB, ydataB)
        lnC.set_data(xdataC, ydataC)
        lnD.set_data(xdataD, ydataD)
        lnA2.set_data(xdataA2, ydataA2)
        lnB2.set_data(xdataB2, ydataB2)
        lnC2.set_data(xdataC2, ydataC2)
        lnD2.set_data(xdataD2, ydataD2)

        ln1.set_data(xs1, ys1)
        ln2.set_data(xs2, ys2)
        ln3.set_data(xs3, ys3)
        ln4.set_data(xs4, ys4)
        return lnA, lnB, lnC, lnD, lnA2, lnB2, lnC2, lnD2, ln1, ln2, ln3, ln4


    def update(frame):
        i = 0
        while times[i] != frame:
            i += 1
        xdataA.append(xsA[i])
        xdataB.append(xsB[i])
        xdataC.append(xsC[i])
        xdataD.append(xsD[i])

        xdataA2[0] = xsA[i]
        xdataB2[0] = xsB[i]
        xdataC2[0] = xsC[i]
        xdataD2[0] = xsD[i]

        ydataA.append(ysA[i])
        ydataB.append(ysB[i])
        ydataC.append(ysC[i])
        ydataD.append(ysD[i])

        ydataA2[0] = ysA[i]
        ydataB2[0] = ysB[i]
        ydataC2[0] = ysC[i]
        ydataD2[0] = ysD[i]

        lnA.set_data(xdataA, ydataA)
        lnB.set_data(xdataB, ydataB)
        lnC.set_data(xdataC, ydataC)
        lnD.set_data(xdataD, ydataD)
        lnA2.set_data(xdataA2, ydataA2)
        lnB2.set_data(xdataB2, ydataB2)
        lnC2.set_data(xdataC2, ydataC2)
        lnD2.set_data(xdataD2, ydataD2)

        ln1.set_data(xs1, ys1)
        ln2.set_data(xs2, ys2)
        ln3.set_data(xs3, ys3)
        ln4.set_data(xs4, ys4)
        return lnA, lnB, lnC, lnD, lnA2, lnB2, lnC2, lnD2, ln1, ln2, ln3, ln4,

    ani = FuncAnimation(fig, update, frames=times,
                        init_func=init, blit=True, interval=2.5, repeat=False)

    # writer = PillowWriter(fps=25)
    # ani.save("four_mice_pursuit.gif", writer=writer)

    plt.show()


def mice_pursuit_hexagon(v, r):
    """
    Funkcja tworząca animację pościgu wewnątrz sześciokąta.
    :return: animacja
    """

    fig, ax = plt.subplots()
    ax.axis('off')
    xdataA, ydataA, xdataA2, ydataA2 = [], [], [0], [0]
    xdataB, ydataB, xdataB2, ydataB2 = [], [], [0], [0]
    xdataC, ydataC, xdataC2, ydataC2 = [], [], [0], [0]
    xdataD, ydataD, xdataD2, ydataD2 = [], [], [0], [0]
    xdataE, ydataE, xdataE2, ydataE2 = [], [], [0], [0]
    xdataF, ydataF, xdataF2, ydataF2 = [], [], [0], [0]

    lnA, = plt.plot([], [], color='#abcae4', animated=True)
    lnA2, = plt.plot([], [], color='#abcae4', marker='o', animated=True)
    lnB, = plt.plot([], [], color='#86b2d8', animated=True)
    lnB2, = plt.plot([], [], color='#86b2d8', marker='o', animated = True)
    lnC, = plt.plot([], [], color='#619bcc', animated=True)
    lnC2, = plt.plot([], [], color='#619bcc', marker='o', animated=True)
    lnD, = plt.plot([], [], color='#3d84bf', animated=True)
    lnD2, = plt.plot([], [], color='#3d84bf', marker='o', animated=True)
    lnE, = plt.plot([], [], color='#316a9a', animated=True)
    lnE2, = plt.plot([], [], color='#316a9a', marker='o', animated=True)
    lnF, = plt.plot([], [], color='#255075', animated=True)
    lnF2, = plt.plot([], [], color='#255075', marker='o', animated=True)
    ln1, = plt.plot([], [], color='black', animated=True, linewidth=0.8)
    ln2, = plt.plot([], [], color='black', animated=True, linewidth=0.8)
    ln3, = plt.plot([], [], color='black', animated=True, linewidth=0.8)
    ln4, = plt.plot([], [], color='black', animated=True, linewidth=0.8)
    ln5, = plt.plot([], [], color='black', animated=True, linewidth=0.8)
    ln6, = plt.plot([], [], color='black', animated=True, linewidth=0.8)

    MAX_TIME = 20
    NUMBER_OF_TIMES = 300

    times = np.linspace(0, MAX_TIME, NUMBER_OF_TIMES)
    tick = MAX_TIME/NUMBER_OF_TIMES

    xsA, ysA = [r/2], [0]
    xsB, ysB = [3*r/2], [0]
    xsC, ysC = [2*r], [r*math.sqrt(3)/2]
    xsD, ysD = [3*r/2], [r*math.sqrt(3)]
    xsE, ysE = [r/2], [r*math.sqrt(3)]
    xsF, ysF = [0], [r*math.sqrt(3)/2]

    for i in range(len(times)-1):
        c = math.sqrt((ysB[i] - ysA[i]) ** 2 + (xsB[i] - xsA[i]) ** 2)
        xsA.append(xsA[i] + (xsB[i] - xsA[i]) * v * tick / c)
        ysA.append(ysA[i] + (ysB[i] - ysA[i]) * v * tick / c)

        c = math.sqrt((ysC[i] - ysB[i]) ** 2 + (xsC[i] - xsB[i]) ** 2)
        xsB.append(xsB[i] + (xsC[i] - xsB[i]) * v * tick / c)
        ysB.append(ysB[i] + (ysC[i] - ysB[i]) * v * tick / c)

        c = math.sqrt((ysD[i] - ysC[i]) ** 2 + (xsD[i] - xsC[i]) ** 2)
        xsC.append(xsC[i] + (xsD[i] - xsC[i]) * v * tick / c)
        ysC.append(ysC[i] + (ysD[i] - ysC[i]) * v * tick / c)

        c = math.sqrt((ysE[i] - ysD[i]) ** 2 + (xsE[i] - xsD[i]) ** 2)
        xsD.append(xsD[i] + (xsE[i] - xsD[i]) * v * tick / c)
        ysD.append(ysD[i] + (ysE[i] - ysD[i]) * v * tick / c)

        c = math.sqrt((ysF[i] - ysE[i]) ** 2 + (xsF[i] - xsE[i]) ** 2)
        xsE.append(xsE[i] + (xsF[i] - xsE[i]) * v * tick / c)
        ysE.append(ysE[i] + (ysF[i] - ysE[i]) * v * tick / c)


        c = math.sqrt((ysA[i] - ysF[i]) ** 2 + (xsA[i] - xsF[i]) ** 2)
        xsF.append(xsF[i] + (xsA[i] - xsF[i]) * v * tick / c)
        ysF.append(ysF[i] + (ysA[i] - ysF[i]) * v * tick / c)

    counter = 0
    for i in range(NUMBER_OF_TIMES):
        counter+=1
        if abs(xsA[i] - xsB[i]) < 0.2 and abs(ysA[i] - ysB[i]) < 0.2:
            break

    times = np.linspace(0, MAX_TIME*counter/NUMBER_OF_TIMES, counter)
    xsA, ysA = xsA[0:counter], ysA[0:counter]
    xsB, ysB = xsB[0:counter], ysB[0:counter]
    xsC, ysC = xsC[0:counter], ysC[0:counter]
    xsD, ysD = xsD[0:counter], ysD[0:counter]
    xsE, ysE = xsE[0:counter], ysE[0:counter]
    xsF, ysF = xsF[0:counter], ysF[0:counter]

    xs1, ys1 = [r/2, 3*r/2], [0, 0]
    xs2, ys2 = np.linspace(3*r/2, 2*r, 200), np.linspace(0, r*math.sqrt(3)/2, 200)
    xs3, ys3 = np.linspace(2 * r,3 * r / 2, 200), np.linspace(r * math.sqrt(3) / 2, r * math.sqrt(3),200)
    xs4, ys4 = [r / 2, 3 * r / 2], [r * math.sqrt(3), r * math.sqrt(3)]
    xs5, ys5 = np.linspace(0, r/2, 200), np.linspace(r * math.sqrt(3) / 2, r * math.sqrt(3), 200)
    xs6, ys6 = np.linspace(0, r/2, 200), np.linspace(r * math.sqrt(3) / 2, 0, 200)

    def init():
        ax.set_xlim(-1, 2*r + 1)
        ax.set_ylim(-1, 2*r + 1)
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_title("Krzywa pogoni wewnątrz sześciokąta")
        ax.set_aspect(aspect='equal')
        lnA.set_data(xdataA, ydataA)
        lnB.set_data(xdataB, ydataB)
        lnC.set_data(xdataC, ydataC)
        lnD.set_data(xdataD, ydataD)
        lnE.set_data(xdataE, ydataE)
        lnF.set_data(xdataF, ydataF)
        lnA2.set_data(xdataA2, ydataA2)
        lnB2.set_data(xdataB2, ydataB2)
        lnC2.set_data(xdataC2, ydataC2)
        lnD2.set_data(xdataD2, ydataD2)
        lnE2.set_data(xdataE2, ydataE2)
        lnF2.set_data(xdataF2, ydataF2)

        ln1.set_data(xs1, ys1)
        ln2.set_data(xs2, ys2)
        ln3.set_data(xs3, ys3)
        ln4.set_data(xs4, ys4)
        ln5.set_data(xs5, ys5)
        ln6.set_data(xs6, ys6)
        return lnA, lnB, lnC, lnD, lnE, lnF, lnA2, lnB2, lnC2, lnD2, lnE2, lnF2, ln1, ln2, ln3, ln4, ln5, ln6


    def update(frame):
        i = 0
        while times[i] != frame:
            i += 1
        xdataA.append(xsA[i])
        xdataB.append(xsB[i])
        xdataC.append(xsC[i])
        xdataD.append(xsD[i])
        xdataE.append(xsE[i])
        xdataF.append(xsF[i])

        xdataA2[0] = xsA[i]
        xdataB2[0] = xsB[i]
        xdataC2[0] = xsC[i]
        xdataD2[0] = xsD[i]
        xdataE2[0] = xsE[i]
        xdataF2[0] = xsF[i]

        ydataA.append(ysA[i])
        ydataB.append(ysB[i])
        ydataC.append(ysC[i])
        ydataD.append(ysD[i])
        ydataE.append(ysE[i])
        ydataF.append(ysF[i])

        ydataA2[0] = ysA[i]
        ydataB2[0] = ysB[i]
        ydataC2[0] = ysC[i]
        ydataD2[0] = ysD[i]
        ydataE2[0] = ysE[i]
        ydataF2[0] = ysF[i]

        lnA.set_data(xdataA, ydataA)
        lnB.set_data(xdataB, ydataB)
        lnC.set_data(xdataC, ydataC)
        lnD.set_data(xdataD, ydataD)
        lnE.set_data(xdataE, ydataE)
        lnF.set_data(xdataF, ydataF)
        lnA2.set_data(xdataA2, ydataA2)
        lnB2.set_data(xdataB2, ydataB2)
        lnC2.set_data(xdataC2, ydataC2)
        lnD2.set_data(xdataD2, ydataD2)
        lnE2.set_data(xdataE2, ydataE2)
        lnF2.set_data(xdataF2, ydataF2)

        ln1.set_data(xs1, ys1)
        ln2.set_data(xs2, ys2)
        ln3.set_data(xs3, ys3)
        ln4.set_data(xs4, ys4)
        ln5.set_data(xs5, ys5)
        ln6.set_data(xs6, ys6)
        return lnA, lnB, lnC, lnD, lnE, lnF, lnA2, lnB2, lnC2, lnD2, lnE2, lnF2, ln1, ln2, ln3, ln4, ln5, ln6,

    ani = FuncAnimation(fig, update, frames=times,
                        init_func=init, blit=True, interval=2.5, repeat=False)

    # writer = PillowWriter(fps=25)
    # ani.save("six_mice_pursuit.gif", writer=writer)

    plt.show()


def mice_pursuit_octagon(v, r):
    """
    Funkcja tworząca animację pościgu wewnątrz ośmiokąta.
    :return: animacja
    """

    fig, ax = plt.subplots()
    ax.axis('off')
    xdataA, ydataA, xdataA2, ydataA2 = [], [], [0], [0]
    xdataB, ydataB, xdataB2, ydataB2 = [], [], [0], [0]
    xdataC, ydataC, xdataC2, ydataC2 = [], [], [0], [0]
    xdataD, ydataD, xdataD2, ydataD2 = [], [], [0], [0]
    xdataE, ydataE, xdataE2, ydataE2 = [], [], [0], [0]
    xdataF, ydataF, xdataF2, ydataF2 = [], [], [0], [0]
    xdataG, ydataG, xdataG2, ydataG2 = [], [], [0], [0]
    xdataH, ydataH, xdataH2, ydataH2 = [], [], [0], [0]

    lnA, = plt.plot([], [], color='#d0e1f0', animated=True)
    lnA2, = plt.plot([], [], color='#d0e1f0', marker='o', animated=True)
    lnB, = plt.plot([], [], color='#abcae4', animated=True)
    lnB2, = plt.plot([], [], color='#abcae4', marker='o', animated = True)
    lnC, = plt.plot([], [], color='#86b2d8', animated=True)
    lnC2, = plt.plot([], [], color='#86b2d8', marker='o', animated=True)
    lnD, = plt.plot([], [], color='#619bcc', animated=True)
    lnD2, = plt.plot([], [], color='#619bcc', marker='o', animated=True)
    lnE, = plt.plot([], [], color='#3d84bf', animated=True)
    lnE2, = plt.plot([], [], color='#3d84bf', marker='o', animated=True)
    lnF, = plt.plot([], [], color='#316a9a', animated=True)
    lnF2, = plt.plot([], [], color='#316a9a', marker='o', animated=True)
    lnG, = plt.plot([], [], color='#255075', animated=True)
    lnG2, = plt.plot([], [], color='#255075', marker='o', animated=True)
    lnH, = plt.plot([], [], color='#193750', animated=True)
    lnH2, = plt.plot([], [], color='#193750', marker='o', animated=True)

    ln1, = plt.plot([], [], color='black', animated=True, linewidth=0.8)
    ln2, = plt.plot([], [], color='black', animated=True, linewidth=0.8)
    ln3, = plt.plot([], [], color='black', animated=True, linewidth=0.8)
    ln4, = plt.plot([], [], color='black', animated=True, linewidth=0.8)
    ln5, = plt.plot([], [], color='black', animated=True, linewidth=0.8)
    ln6, = plt.plot([], [], color='black', animated=True, linewidth=0.8)
    ln7, = plt.plot([], [], color='black', animated=True, linewidth=0.8)
    ln8, = plt.plot([], [], color='black', animated=True, linewidth=0.8)

    MAX_TIME = 40
    NUMBER_OF_TIMES = 300

    times = np.linspace(0, MAX_TIME, NUMBER_OF_TIMES)
    tick = MAX_TIME/NUMBER_OF_TIMES

    xsA, ysA = [-r * math.sqrt(2) / 2], [-r * math.sqrt(2) / 2]
    xsB, ysB = [0], [-r]
    xsC, ysC = [r*math.sqrt(2)/2], [-r*math.sqrt(2)/2]
    xsD, ysD = [r], [0]
    xsE, ysE = [r*math.sqrt(2)/2], [r*math.sqrt(2)/2]
    xsF, ysF = [0], [r]
    xsG, ysG = [-r*math.sqrt(2)/2], [r*math.sqrt(2)/2]
    xsH, ysH = [-r], [0]


    for i in range(len(times)-1):
        c = math.sqrt((ysB[i] - ysA[i]) ** 2 + (xsB[i] - xsA[i]) ** 2)
        xsA.append(xsA[i] + (xsB[i] - xsA[i]) * v * tick / c)
        ysA.append(ysA[i] + (ysB[i] - ysA[i]) * v * tick / c)

        c = math.sqrt((ysC[i] - ysB[i]) ** 2 + (xsC[i] - xsB[i]) ** 2)
        xsB.append(xsB[i] + (xsC[i] - xsB[i]) * v * tick / c)
        ysB.append(ysB[i] + (ysC[i] - ysB[i]) * v * tick / c)

        c = math.sqrt((ysD[i] - ysC[i]) ** 2 + (xsD[i] - xsC[i]) ** 2)
        xsC.append(xsC[i] + (xsD[i] - xsC[i]) * v * tick / c)
        ysC.append(ysC[i] + (ysD[i] - ysC[i]) * v * tick / c)

        c = math.sqrt((ysE[i] - ysD[i]) ** 2 + (xsE[i] - xsD[i]) ** 2)
        xsD.append(xsD[i] + (xsE[i] - xsD[i]) * v * tick / c)
        ysD.append(ysD[i] + (ysE[i] - ysD[i]) * v * tick / c)

        c = math.sqrt((ysF[i] - ysE[i]) ** 2 + (xsF[i] - xsE[i]) ** 2)
        xsE.append(xsE[i] + (xsF[i] - xsE[i]) * v * tick / c)
        ysE.append(ysE[i] + (ysF[i] - ysE[i]) * v * tick / c)

        c = math.sqrt((ysG[i] - ysF[i]) ** 2 + (xsG[i] - xsF[i]) ** 2)
        xsF.append(xsF[i] + (xsG[i] - xsF[i]) * v * tick / c)
        ysF.append(ysF[i] + (ysG[i] - ysF[i]) * v * tick / c)

        c = math.sqrt((ysH[i] - ysG[i]) ** 2 + (xsH[i] - xsG[i]) ** 2)
        xsG.append(xsG[i] + (xsH[i] - xsG[i]) * v * tick / c)
        ysG.append(ysG[i] + (ysH[i] - ysG[i]) * v * tick / c)

        c = math.sqrt((ysA[i] - ysH[i]) ** 2 + (xsA[i] - xsH[i]) ** 2)
        xsH.append(xsH[i] + (xsA[i] - xsH[i]) * v * tick / c)
        ysH.append(ysH[i] + (ysA[i] - ysH[i]) * v * tick / c)


    counter = 0
    for i in range(NUMBER_OF_TIMES):
        counter+=1
        if abs(xsA[i] - xsB[i]) < 0.1 and abs(ysA[i] - ysB[i]) < 0.1:
            break

    times = np.linspace(0, MAX_TIME*counter/NUMBER_OF_TIMES, counter)
    xsA, ysA = xsA[0:counter], ysA[0:counter]
    xsB, ysB = xsB[0:counter], ysB[0:counter]
    xsC, ysC = xsC[0:counter], ysC[0:counter]
    xsD, ysD = xsD[0:counter], ysD[0:counter]
    xsE, ysE = xsE[0:counter], ysE[0:counter]
    xsF, ysF = xsF[0:counter], ysF[0:counter]
    xsG, ysG = xsG[0:counter], ysG[0:counter]
    xsH, ysH = xsH[0:counter], ysH[0:counter]

    xs1, ys1 = np.linspace(0, r*math.sqrt(2)/2, 200), np.linspace(-r, -r*math.sqrt(2)/2, 200)
    xs2, ys2 = np.linspace(r*math.sqrt(2)/2, r, 200), np.linspace(-r*math.sqrt(2)/2, 0, 200)
    xs3, ys3 = np.linspace(r, r*math.sqrt(2)/2, 200), np.linspace(0, r*math.sqrt(2)/2, 200)
    xs4, ys4 = np.linspace(r*math.sqrt(2)/2, 0, 200), np.linspace(r*math.sqrt(2)/2, r, 200)
    xs5, ys5 = np.linspace(0, -r*math.sqrt(2)/2, 200), np.linspace(r, r*math.sqrt(2)/2, 200)
    xs6, ys6 = np.linspace(-r*math.sqrt(2)/2, -r, 200), np.linspace(r*math.sqrt(2)/2, 0, 200)
    xs7, ys7 = np.linspace(-r, -r*math.sqrt(2)/2, 200), np.linspace(0, -r*math.sqrt(2)/2, 200)
    xs8, ys8 = np.linspace(-r*math.sqrt(2)/2, 0, 200), np.linspace(-r*math.sqrt(2)/2, -r, 200)

    def init():
        ax.set_xlim(-r - 1, r + 1)
        ax.set_ylim(-r -1, r + 1)
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_title("Krzywa pogoni wewnątrz ośmiokąta")
        ax.set_aspect(aspect='equal')
        lnA.set_data(xdataA, ydataA)
        lnB.set_data(xdataB, ydataB)
        lnC.set_data(xdataC, ydataC)
        lnD.set_data(xdataD, ydataD)
        lnE.set_data(xdataE, ydataE)
        lnF.set_data(xdataF, ydataF)
        lnG.set_data(xdataG, ydataG)
        lnH.set_data(xdataH, ydataH)

        lnA2.set_data(xdataA2, ydataA2)
        lnB2.set_data(xdataB2, ydataB2)
        lnC2.set_data(xdataC2, ydataC2)
        lnD2.set_data(xdataD2, ydataD2)
        lnE2.set_data(xdataE2, ydataE2)
        lnF2.set_data(xdataF2, ydataF2)
        lnG2.set_data(xdataG2, ydataG2)
        lnH2.set_data(xdataH2, ydataH2)

        ln1.set_data(xs1, ys1)
        ln2.set_data(xs2, ys2)
        ln3.set_data(xs3, ys3)
        ln4.set_data(xs4, ys4)
        ln5.set_data(xs5, ys5)
        ln6.set_data(xs6, ys6)
        ln7.set_data(xs7, ys7)
        ln8.set_data(xs8, ys8)
        return lnA, lnB, lnC, lnD, lnE, lnF, lnG, lnH, lnA2, lnB2, lnC2, lnD2, lnE2, lnF2, lnG2, lnH2, ln1, ln2, ln3, ln4, ln5, ln6, ln7, ln8


    def update(frame):
        i = 0
        while times[i] != frame:
            i += 1
        xdataA.append(xsA[i])
        xdataB.append(xsB[i])
        xdataC.append(xsC[i])
        xdataD.append(xsD[i])
        xdataE.append(xsE[i])
        xdataF.append(xsF[i])
        xdataG.append(xsG[i])
        xdataH.append(xsH[i])

        xdataA2[0] = xsA[i]
        xdataB2[0] = xsB[i]
        xdataC2[0] = xsC[i]
        xdataD2[0] = xsD[i]
        xdataE2[0] = xsE[i]
        xdataF2[0] = xsF[i]
        xdataG2[0] = xsG[i]
        xdataH2[0] = xsH[i]

        ydataA.append(ysA[i])
        ydataB.append(ysB[i])
        ydataC.append(ysC[i])
        ydataD.append(ysD[i])
        ydataE.append(ysE[i])
        ydataF.append(ysF[i])
        ydataG.append(ysG[i])
        ydataH.append(ysH[i])

        ydataA2[0] = ysA[i]
        ydataB2[0] = ysB[i]
        ydataC2[0] = ysC[i]
        ydataD2[0] = ysD[i]
        ydataE2[0] = ysE[i]
        ydataF2[0] = ysF[i]
        ydataG2[0] = ysG[i]
        ydataH2[0] = ysH[i]

        lnA.set_data(xdataA, ydataA)
        lnB.set_data(xdataB, ydataB)
        lnC.set_data(xdataC, ydataC)
        lnD.set_data(xdataD, ydataD)
        lnE.set_data(xdataE, ydataE)
        lnF.set_data(xdataF, ydataF)
        lnG.set_data(xdataG, ydataG)
        lnH.set_data(xdataH, ydataH)

        lnA2.set_data(xdataA2, ydataA2)
        lnB2.set_data(xdataB2, ydataB2)
        lnC2.set_data(xdataC2, ydataC2)
        lnD2.set_data(xdataD2, ydataD2)
        lnE2.set_data(xdataE2, ydataE2)
        lnF2.set_data(xdataF2, ydataF2)
        lnG2.set_data(xdataG2, ydataG2)
        lnH2.set_data(xdataH2, ydataH2)

        ln1.set_data(xs1, ys1)
        ln2.set_data(xs2, ys2)
        ln3.set_data(xs3, ys3)
        ln4.set_data(xs4, ys4)
        ln5.set_data(xs5, ys5)
        ln6.set_data(xs6, ys6)
        ln7.set_data(xs7, ys7)
        ln8.set_data(xs8, ys8)
        return lnA, lnB, lnC, lnD, lnE, lnF, lnG, lnH, lnA2, lnB2, lnC2, lnD2, lnE2, lnF2, lnG2, lnH2, ln1, ln2, ln3, ln4, ln5, ln6, ln7, ln8,

    ani = FuncAnimation(fig, update, frames=times,
                        init_func=init, blit=True, interval=1, repeat=False)

    # writer = PillowWriter(fps=25)
    # ani.save("eight_mice_pursuit.gif", writer=writer)

    plt.show()


if __name__ == "__main__":
    # mice_pursuit_square(1,6)
    # mice_pursuit_hexagon(4, 12)
    # mice_pursuit_octagon(1,6)