import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import PillowWriter
import math


def get_dataA(times, x0, y0, vA, xsB, ysB, tick):
    """
    Funkcja obliczająca współrzędne (x, y) obiektu goniącego.

    :param times: lista czasów
    :param x0: położenie początkowe na osi Ox
    :param y0: położenie początkowe na osi Oy
    :param vA: prędkość obiektu
    :param xsB: lista współrzędnych x obiektu uciekającego
    :param ysB: lista współrzędnych y obiektu uciekającego
    :param tick: krok czasowy
    :return: xs, ys
    """

    xs, ys = [], []
    for time in times:
        if time == 0:
            xs.append(x0)
            ys.append(y0)
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


# KLASYCZNA KRZYWA POGONI

def get_dataB_classic(times, x0, vB, tick):
    """
    Funkcja obliczająca współrzędne (x, y) obiektu uciekającego po linii prostej.

    :param times: lista czasów
    :param x0: odległość obiektu od osi Oy
    :param vB: prędkość obiektu
    :param tick: krok czasowy
    :return: xs, ys
    """

    xs, ys = [], []
    for time in times:
        if time == 0:
            xs.append(x0)
            ys.append(0)
        else:
            y = ys[-1]
            xs.append(x0)
            ys.append(y + vB*tick)

    return xs, ys


def classic_pursuit(x0, vA, vB):
    """
    Funkcja tworząca animację pościgu, gdy ciało ucieka po linii prostej.

    :param x0: położenie początkowe obiektu B
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
    TICK = MAX_TIME/NUMBER_OF_TIMES

    times = np.linspace(0, MAX_TIME, NUMBER_OF_TIMES)

    xsB, ysB = get_dataB_classic(times, x0, vB, TICK)
    xsA, ysA = get_dataA(times, 0, 0, vA, xsB, ysB, TICK)

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


# OKRĄG WEWNĄTRZ

def get_dataB_circle_inside(times, r, vB, tick):
        """
        Funkcja obliczająca współrzędne (x, y) obiektu uciekającego po okręgu.

        :param times: lista czasów
        :param r: promień okręgu
        :param vB: prędkość obiektu
        :param tick: krok czasowy
        :return: xs, ys
        """

        xs, ys, alphas = [], [], []
        for time in times:
            if time == 0:
                xs.append(r)
                ys.append(0)
                alphas.append(0)
            else:
                alpha = alphas[-1]
                alpha = alpha + vB * tick / r

                alphas.append(alpha)
                xs.append(r * np.cos(alpha))
                ys.append(r * np.sin(alpha))

        return xs, ys


def circle_pursuit_inside(r, vA, vB):
        """
        Funkcja tworząca animację pościgu po okręgu.

        :param r: promień okręgu
        :param vA: prędkość obiektu goniącego
        :param vB: prędkość obiektu uciekającego
        :return: animacja
        """

        fig, ax = plt.subplots()
        xdataB, xdataA, ydataB, ydataA, xdataB2, ydataB2, xdataA2, ydataA2 = [], [], [], [], [0], [0], [0], [0]
        lnB, = plt.plot([], [], 'r', animated=True)
        lnB2, = plt.plot([], [], 'r', marker='o', animated=True)
        lnA, = plt.plot([], [], 'b', animated=True)
        lnA2, = plt.plot([], [], 'b', marker='o', animated=True)

        MAX_TIME = 20
        NUMBER_OF_TIMES = 400
        TICK = 0.02

        times = np.linspace(0, MAX_TIME, NUMBER_OF_TIMES)

        xsB, ysB = get_dataB_circle_inside(times, r, vB, TICK)
        xsA, ysA = get_dataA(times, -r, 0, vA, xsB, ysB, TICK)

        counter = 0
        for i in range(NUMBER_OF_TIMES):
            counter += 1
            if abs(xsA[i] - xsB[i]) < 0.01 and abs(ysA[i] - ysB[i]) < 0.01:
                break

        times = np.linspace(0, MAX_TIME * counter / NUMBER_OF_TIMES, counter)
        xsB, ysB = xsB[0:counter], ysB[0:counter]
        xsA, ysA = xsA[0:counter], ysA[0:counter]

        def init():
            ax.set_xlim(-r - 1, r + 1)
            ax.set_ylim(-r - 1, r + 1)
            ax.set_xlabel("x")
            ax.set_ylabel("y")
            ax.set_title("Krzywa pogoni po okręgu")
            ax.set_aspect(aspect='equal')
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
            xdataB2[0] = xsB[i]
            xdataA2[0] = xsA[i]
            ydataB.append(ysB[i])
            ydataB2[0] = ysB[i]
            ydataA2[0] = ysA[i]
            ydataA.append(ysA[i])
            lnB.set_data(xdataB, ydataB)
            lnA.set_data(xdataA, ydataA)
            lnB2.set_data(xdataB2, ydataB2)
            lnA2.set_data(xdataA2, ydataA2)
            return lnB, lnA, lnB2, lnA2,

        ani = FuncAnimation(fig, update, frames=times,
                            init_func=init, blit=True, interval=2, repeat=False)

        # writer = PillowWriter(fps=40)
        # ani.save("circle_pursuit_inside.gif", writer=writer)

        plt.show()


# OKRĄG NA ZEWNĄTRZ

def get_dataB_circle(times, x0, r, vB, tick):
        """
        Funkcja obliczająca współrzędne (x, y) obiektu uciekającego po okręgu.

        :param times: lista czasów
        :param x0: położenie środka okręgu
        :param r: promień okręgu
        :param vB: prędkość obiektu
        :return: xs, ys
        """

        xs, ys, alphas = [], [], []
        for time in times:
            if time == 0:
                xs.append(x0 + r)
                ys.append(0)
                alphas.append(0)
            else:
                x, y, alpha = xs[-1], ys[-1], alphas[-1]

                alphas.append(alpha + vB * tick / r)

                xs.append(x0 + r * np.cos(alphas[-1]))
                ys.append(r * np.sin(alphas[-1]))

        return xs, ys


def circle_pursuit(x0, r, vA, vB):
        """
        Funkcja tworząca animację pościgu, gdy ciało ucieka po okręgu a ciało goniące znajduje się poza nim.

        :param x0: położenie środka okręgu
        :param r: promień okręgu
        :param vA: prędkość obiektu goniącego
        :param vB: prędkość obiektu uciekającego
        :return: animacja
        """

        fig, ax = plt.subplots()
        xdataB, xdataA, ydataB, ydataA, xdataB2, xdataA2, ydataB2, ydataA2 = [], [], [], [], [0], [0], [0], [0]
        lnB, = plt.plot([], [], 'r', animated=True)
        lnB2, = plt.plot([], [], 'r', marker='o', animated=True)
        lnA, = plt.plot([], [], 'b', animated=True)
        lnA2, = plt.plot([], [], 'b', marker='o', animated=True)

        MAX_TIME = 20
        NUMBER_OF_TIMES = 400
        TICK = 0.02

        times = np.linspace(0, MAX_TIME, NUMBER_OF_TIMES)

        xsB, ysB = get_dataB_circle(times, 0, r, vB, TICK)
        xsA, ysA = get_dataA(times, 15, 3, vA, xsB, ysB, TICK)

        counter = 0
        for i in range(NUMBER_OF_TIMES):
            counter += 1
            if abs(xsA[i] - xsB[i]) < 0.01 and abs(ysA[i] - ysB[i]) < 0.01:
                break

        times = np.linspace(0, MAX_TIME * counter / NUMBER_OF_TIMES, counter)
        xsB, ysB = xsB[0:counter], ysB[0:counter]
        xsA, ysA = xsA[0:counter], ysA[0:counter]

        def init():
            ax.set_xlim(-r - 1, 15 + 1)
            ax.set_ylim(-r - 1, r + 1 + 1)
            ax.set_xlabel("x")
            ax.set_ylabel("y")
            ax.set_title("Krzywa pogoni po okręgu")
            ax.set_aspect(aspect='equal')
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
        #
        # writer = PillowWriter(fps=40)
        # ani.save("circle_pursuit.gif", writer=writer)

        plt.show()


# HIPOCYKLOIDA

def hypocycloid(t, R, r):
    '''
    Funkcja opisująca hipocykloidę.

    :param t: parametr t
    :param R: promień dużego koła
    :param r: promień małego koła
    :return: x, y
    '''

    return (R - r)*np.cos(t) + r*np.cos(t*(R - r)/r), (R - r)*np.sin(t) - r*np.sin(t*(R- r)/r)


def get_dataB_hypocycloid(times, R, r, vB, tick):
    """
    Funkcja obliczająca współrzędne (x, y) obiektu uciekającego po hipocykloidzie.

    :param times: lista czasów
    :param R: promień dużego koła
    :param r: promień małego koła
    :param vB: prędkość obiektu
    :param tick: krok czasowy
    :return: xs, ys
    """

    xs, ys, ts = [], [], []

    for time in times:
        if time == 0:
            x0, y0 = hypocycloid(0, R, r)
            xs.append(x0)
            ys.append(y0)
            ts.append(0)
        else:
            t = ts[-1]
            x0, y0 = hypocycloid(t, R, r)
            x, y = x0, y0

            while (x-x0)**2 + (y-y0)**2 <= (vB*tick)**2:
                t += 0.005
                x, y = hypocycloid(t, R, r)

            xs.append(x)
            ys.append(y)
            ts.append(t)

    return xs, ys


def hypocycloid_pursuit(R, r, vA, vB):
    """
    Funkcja tworząca animację pościgu po hipocykloidzie.

    :param R: promień dużego okręgu
    :param r: promień małego okręgu
    :param vA: prędkość obiektu goniącego
    :param vB: prędkość obiektu uciekającego
    :return: animacja
    """

    fig, ax = plt.subplots()
    xdataA, ydataA, xdataA2, ydataA2 = [], [], [0], [0]
    xdataB, ydataB, xdataB2, ydataB2 = [], [], [0], [0]
    lnA, = plt.plot([], [], 'b', animated=True)
    lnA2, = plt.plot([], [], 'b', marker='o', animated=True)
    lnB, = plt.plot([], [], 'r', animated=True)
    lnB2, = plt.plot([], [], 'r', marker='o', animated = True)

    MAX_TIME = 300
    NUMBER_OF_TIMES = 100
    TICK = 0.03

    times = np.linspace(0, MAX_TIME, NUMBER_OF_TIMES)

    xsB, ysB = get_dataB_hypocycloid(times, R, r, vB, TICK)
    xsA, ysA = get_dataA(times, 5, 0, vA, xsB, ysB, TICK)

    counter = 0
    for i in range(NUMBER_OF_TIMES):
        counter+=1
        if abs(xsA[i] - xsB[i]) < 0.01 and abs(ysA[i] - ysB[i]) < 0.01:
            break

    times = np.linspace(0, MAX_TIME*counter/NUMBER_OF_TIMES, counter)
    xsB, ysB = xsB[0:counter], ysB[0:counter]
    xsA, ysA = xsA[0:counter], ysA[0:counter]

    def init():
        ax.set_xlim(-3, 6)
        ax.set_ylim(-3, 3)
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_title("Krzywa pogoni po hipocykloidzie")
        ax.set_aspect(aspect='equal')

        lnA.set_data(xdataA, ydataA)
        lnA2.set_data(xdataA2, ydataA2)

        lnB.set_data(xdataB, ydataB)
        lnB2.set_data(xdataB2, ydataB2)

        return lnB, lnB2, lnA, lnA2

    def update(frame):
        i = 0
        while times[i] != frame:
            i += 1

        xdataA.append(xsA[i])
        ydataA.append(ysA[i])
        xdataA2[0] = xsA[i]
        ydataA2[0] = ysA[i]

        xdataB.append(xsB[i])
        ydataB.append(ysB[i])
        xdataB2[0] = xsB[i]
        ydataB2[0] = ysB[i]

        lnA.set_data(xdataA, ydataA)
        lnA2.set_data(xdataA2, ydataA2)

        lnB.set_data(xdataB, ydataB)
        lnB2.set_data(xdataB2, ydataB2)

        return lnB, lnB2, lnA, lnA2,

    ani = FuncAnimation(fig, update, frames=times,
                        init_func=init, blit=True, interval=15, repeat=False)

    # writer = PillowWriter(fps=30)
    # ani.save("hypocycloid_pursuit.gif", writer=writer)

    plt.show()


# HIPOCYKLOIDA WYDŁUŻONA

def elongated_hypocycloid(t, R, r, h):
    '''
    Funkcja opisująca hipocykloidę wydłużoną.

    :param t: parametr t
    :param R: promień dużego koła
    :param r: promień małego koła
    :param h: odległość punktu od środka koła o promieniu r
    :return: x, y
    '''

    return (R - r)*np.cos(t) + h*np.cos(t*(R - r)/r), (R - r)*np.sin(t) - h*np.sin(t*(R- r)/r)


def get_dataB_elongated_hypocycloid(times, R, r, h, vB, tick):
    """
    Funkcja obliczająca współrzędne (x, y) obiektu uciekającego po lemniskacie Bernoulliego.

    :param times: lista czasów
    :param R: promień dużego koła
    :param r: promień małego koła
    :param h: odległość punktu od środka koła o promieniu r
    :param vB: prędkość obiektu
    :param tick: krok czasowy
    :return: xs, ys
    """

    xs, ys, ts = [], [], []

    for time in times:
        if time == 0:
            x0, y0 = elongated_hypocycloid(0, R, r, h)
            xs.append(x0)
            ys.append(y0)
            ts.append(0)
        else:
            t = ts[-1]
            x0, y0 = elongated_hypocycloid(t, R, r, h)
            x, y = x0, y0

            while (x-x0)**2 + (y-y0)**2 <= (vB*tick)**2:
                t += 0.001
                x, y = elongated_hypocycloid(t, R, r, h)

            xs.append(x)
            ys.append(y)
            ts.append(t)

    return xs, ys


def elongated_hypocycloid_pursuit(R, r, h, vA, vB):
    """
    Funkcja tworząca animację pościgu po hipocykloidzie wydłużonej.

    :param R: promień dużego okręgu
    :param r: promień małego okręgu
    :param h: odległość punktu od środka koła o promieniu r
    :param vA: prędkość obiektu goniącego
    :param vB: prędkość obiektu uciekającego
    :return: animacja
    """

    fig, ax = plt.subplots()
    xdataA, ydataA, xdataA2, ydataA2 = [], [], [0], [0]
    xdataB, ydataB, xdataB2, ydataB2 = [], [], [0], [0]
    lnA, = plt.plot([], [], 'b', animated=True)
    lnA2, = plt.plot([], [], 'b', marker='o', animated=True)
    lnB, = plt.plot([], [], 'r', animated=True)
    lnB2, = plt.plot([], [], 'r', marker='o', animated = True)

    MAX_TIME = 300
    NUMBER_OF_TIMES = 300
    TICK = 0.03

    times = np.linspace(0, MAX_TIME, NUMBER_OF_TIMES)

    xsB, ysB = get_dataB_elongated_hypocycloid(times, R, r, h, vB, TICK)
    xsA, ysA = get_dataA(times, 5, 0, vA, xsB, ysB, TICK)

    counter = 0
    for i in range(NUMBER_OF_TIMES):
        counter+=1
        if abs(xsA[i] - xsB[i]) < 0.01 and abs(ysA[i] - ysB[i]) < 0.01:
            break

    times = np.linspace(0, MAX_TIME*counter/NUMBER_OF_TIMES, counter)
    xsB, ysB = xsB[0:counter], ysB[0:counter]
    xsA, ysA = xsA[0:counter], ysA[0:counter]

    def init():
        ax.set_xlim(-10, 10)
        ax.set_ylim(-7, 7)
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_title("Krzywa pogoni po hipocykloidzie wydłużonej")
        ax.set_aspect(aspect='equal')

        lnA.set_data(xdataA, ydataA)
        lnA2.set_data(xdataA2, ydataA2)

        lnB.set_data(xdataB, ydataB)
        lnB2.set_data(xdataB2, ydataB2)

        return lnB, lnB2, lnA, lnA2

    def update(frame):
        i = 0
        while times[i] != frame:
            i += 1

        xdataA.append(xsA[i])
        ydataA.append(ysA[i])
        xdataA2[0] = xsA[i]
        ydataA2[0] = ysA[i]

        xdataB.append(xsB[i])
        ydataB.append(ysB[i])
        xdataB2[0] = xsB[i]
        ydataB2[0] = ysB[i]

        lnA.set_data(xdataA, ydataA)
        lnA2.set_data(xdataA2, ydataA2)

        lnB.set_data(xdataB, ydataB)
        lnB2.set_data(xdataB2, ydataB2)

        return lnB, lnB2, lnA, lnA2,

    ani = FuncAnimation(fig, update, frames=times,
                        init_func=init, blit=True, interval=1, repeat=False)

    # writer = PillowWriter(fps=40)
    # ani.save("elongated_hypocycloid_pursuit.gif", writer=writer)

    plt.show()


# CYKLOIDA

def cycloid(t, r):
    '''
    Funkcja opisująca cykloidę
    :param t: parametr t
    :param r: promień
    :return: x(t), y(t)
    '''

    return r*(t - np.sin(t)), r* (1 - np.cos(t))


def get_dataB_cycloid(times, r, vB, tick):
    """
    Funkcja obliczająca współrzędne (x, y) obiektu uciekającego po cykloidzie.

    :param times: lista czasów
    :param r: promień
    :param vB: prędkość obiektu
    :param tick: krok czasowy
    :return: xs, ys
    """

    xs, ys, ts = [], [], []

    for time in times:
        if time == 0:
            x0, y0 = cycloid(0, r)
            xs.append(x0)
            ys.append(y0)
            ts.append(0)
        else:
            t = ts[-1]
            x0, y0 = cycloid(t, r)
            x, y = x0, y0

            while (x-x0)**2 + (y-y0)**2 <= (vB*tick)**2:
                t += 0.01
                x, y = cycloid(t, r)

            xs.append(x)
            ys.append(y)
            ts.append(t)

    return xs, ys


def cycloid_pursuit(r, vA, vB):
    """
    Funkcja tworząca animację pościgu po cykloidzie.

    :param r: promień
    :param vA: prędkość obiektu goniącego
    :param vB: prędkość obiektu uciekającego
    :return: animacja
    """

    fig, ax = plt.subplots()
    xdataA, ydataA, xdataA2, ydataA2 = [], [], [0], [0]
    xdataB, ydataB, xdataB2, ydataB2 = [], [], [0], [0]
    lnA, = plt.plot([], [], 'b', animated=True)
    lnA2, = plt.plot([], [], 'b', marker='o', animated=True)
    lnB, = plt.plot([], [], 'r', animated=True)
    lnB2, = plt.plot([], [], 'r', marker='o', animated = True)

    MAX_TIME = 300
    NUMBER_OF_TIMES = 120
    TICK = 0.1

    times = np.linspace(0, MAX_TIME, NUMBER_OF_TIMES)

    xsB, ysB = get_dataB_cycloid(times, r, vB, TICK)
    xsA, ysA = get_dataA(times, 15, 0, vA, xsB, ysB, TICK)

    counter = 0
    for i in range(NUMBER_OF_TIMES):
        counter+=1
        if abs(xsA[i] - xsB[i]) < 0.01 and abs(ysA[i] - ysB[i]) < 0.01:
            break

    times = np.linspace(0, MAX_TIME*counter/NUMBER_OF_TIMES, counter)
    xsB, ysB = xsB[0:counter], ysB[0:counter]
    xsA, ysA = xsA[0:counter], ysA[0:counter]

    def init():
        ax.set_xlim(-1, 100)
        ax.set_ylim(-20, 30)
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_title("Krzywa pogoni po cykloidzie")
        ax.set_aspect(aspect='equal')

        lnA.set_data(xdataA, ydataA)
        lnA2.set_data(xdataA2, ydataA2)

        lnB.set_data(xdataB, ydataB)
        lnB2.set_data(xdataB2, ydataB2)

        return lnB, lnB2, lnA, lnA2

    def update(frame):
        i = 0
        while times[i] != frame:
            i += 1

        xdataA.append(xsA[i])
        ydataA.append(ysA[i])
        xdataA2[0] = xsA[i]
        ydataA2[0] = ysA[i]

        xdataB.append(xsB[i])
        ydataB.append(ysB[i])
        xdataB2[0] = xsB[i]
        ydataB2[0] = ysB[i]

        lnA.set_data(xdataA, ydataA)
        lnA2.set_data(xdataA2, ydataA2)

        lnB.set_data(xdataB, ydataB)
        lnB2.set_data(xdataB2, ydataB2)

        return lnB, lnB2, lnA, lnA2,

    ani = FuncAnimation(fig, update, frames=times,
                        init_func=init, blit=True, interval=5, repeat=False)

    # writer = PillowWriter(fps=30)
    # ani.save("cycloid_pursuit.gif", writer=writer)

    plt.show()


# KRZYWA LISSAJOUS

def lissajous_curve(t, A, B, a, b, d):
    '''
    Funkcja opisująca krzywą Lissajous
    :param t: parametr t
    :param A: współczynnik A
    :param B: współczynnik B
    :param a: współczynnik a
    :param b: współczynnik b
    :param d: współczynnik d
    :return: x(t), y(t)
    '''

    return A*np.sin(a*t + d), B*np.sin(b*t)


def get_dataB_lissajous_curve(times, A, B, a, b, d, vB, tick):
    """
    Funkcja obliczająca współrzędne (x, y) obiektu uciekającego po krzywej Lissajous.

    :param times: lista czasów
    :param A: współczynnik A
    :param B: współczynnik B
    :param a: współczynnik a
    :param b: współczynnik b
    :param d: współczynnik d
    :param vB: prędkość obiektu
    :param tick: krok czasowy
    :return: xs, ys
    """
    xs, ys, ts = [], [], []

    for time in times:
        if time == 0:
            x0, y0 = lissajous_curve(0, A, B, a, b, d)
            xs.append(x0)
            ys.append(y0)
            ts.append(0)
        else:
            t = ts[-1]
            x0, y0 = lissajous_curve(t, A, B, a, b, d)
            x, y = x0, y0

            while (x-x0)**2 + (y-y0)**2 <= (vB*tick)**2:
                t += 0.001
                x, y = lissajous_curve(t, A, B, a, b, d)

            xs.append(x)
            ys.append(y)
            ts.append(t)

    return xs, ys


def lissajous_curve_pursuit(A, B, a, b, d, vA, vB):
    """
    Funkcja tworząca animację pościgu po krzywej Lissajous.

    :param A: współczynnik A
    :param B: współczynnik B
    :param a: współczynnik a
    :param b: współczynnik b
    :param d: współczynnik d
    :param vA: prędkość obiektu goniącego
    :param vB: prędkość obiektu uciekającego
    :return: animacja
    """

    fig, ax = plt.subplots()
    xdataA, ydataA, xdataA2, ydataA2 = [], [], [0], [0]
    xdataB, ydataB, xdataB2, ydataB2 = [], [], [0], [0]
    lnA, = plt.plot([], [], 'b', animated=True)
    lnA2, = plt.plot([], [], 'b', marker='o', animated=True)
    lnB, = plt.plot([], [], 'r', animated=True)
    lnB2, = plt.plot([], [], 'r', marker='o', animated = True)

    MAX_TIME = 300
    NUMBER_OF_TIMES = 600
    TICK = 0.012

    times = np.linspace(0, MAX_TIME, NUMBER_OF_TIMES)

    xsB, ysB = get_dataB_lissajous_curve(times, A, B, a, b, d, vB, TICK)
    xsA, ysA = get_dataA(times, 0, 1, vA, xsB, ysB, TICK)

    counter = 0
    for i in range(NUMBER_OF_TIMES):
        counter+=1
        if abs(xsA[i] - xsB[i]) < 0.01 and abs(ysA[i] - ysB[i]) < 0.01:
            break

    times = np.linspace(0, MAX_TIME*counter/NUMBER_OF_TIMES, counter)
    xsB, ysB = xsB[0:counter], ysB[0:counter]
    xsA, ysA = xsA[0:counter], ysA[0:counter]

    def init():
        ax.set_xlim(-A - 1, A + 1)
        ax.set_ylim(-B - 1, B + 1)
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_title("Krzywa pogoni po krzywej Lissajous")
        ax.set_aspect(aspect='equal')

        lnA.set_data(xdataA, ydataA)
        lnA2.set_data(xdataA2, ydataA2)

        lnB.set_data(xdataB, ydataB)
        lnB2.set_data(xdataB2, ydataB2)

        return lnB, lnB2, lnA, lnA2

    def update(frame):
        i = 0
        while times[i] != frame:
            i += 1

        xdataA.append(xsA[i])
        ydataA.append(ysA[i])
        xdataA2[0] = xsA[i]
        ydataA2[0] = ysA[i]

        xdataB.append(xsB[i])
        ydataB.append(ysB[i])
        xdataB2[0] = xsB[i]
        ydataB2[0] = ysB[i]

        lnA.set_data(xdataA, ydataA)
        lnA2.set_data(xdataA2, ydataA2)

        lnB.set_data(xdataB, ydataB)
        lnB2.set_data(xdataB2, ydataB2)

        return lnB, lnB2, lnA, lnA2,

    ani = FuncAnimation(fig, update, frames=times,
                        init_func=init, blit=True, interval=1, repeat=False)

    # writer = PillowWriter(fps=50)
    # ani.save("lissajous_curve_pursuit.gif", writer=writer)

    plt.show()


# LEMNISKATA BERNOULLIEGO

def infinity_symbol(t, a):
    '''
    Funkcja opisująca lemniskatę Bernoulliego
    :param t: parametr t
    :param a: współczynnik a
    :return: x(t), y(t)
    '''

    return a*math.sqrt(2)*np.cos(t)/(1 + (np.sin(t))**2), a*math.sqrt(2)*np.cos(t)*np.sin(t)/(1 + (np.sin(t))**2)


def get_dataB_infinity_symbol(times, a, vB, tick):
    """
    Funkcja obliczająca współrzędne (x, y) obiektu uciekającego po lemniskacie Bernoulliego.

    :param times: lista czasów
    :param a: współczynnik a
    :param vB: prędkość obiektu
    :param tick: krok czasowy
    :return: xs, ys
    """

    xs, ys, ts = [], [], []

    for time in times:
        if time == 0:
            x0, y0 = infinity_symbol(0, a)
            xs.append(x0)
            ys.append(y0)
            ts.append(0)
        else:
            t = ts[-1]
            x0, y0 = infinity_symbol(t, a)
            x, y = infinity_symbol(t, a)

            while (x-x0)**2 + (y-y0)**2 <= (vB*tick)**2:
                t += 0.001
                x, y = infinity_symbol(t, a)

            xs.append(x)
            ys.append(y)
            ts.append(t)

    return xs, ys


def infinity_symbol_pursuit(a, vA, vB):
    """
    Funkcja tworząca animację pościgu po lemniskacie Bernoulliego.

    :param a: parametr a
    :param vA: prędkość obiektu goniącego
    :param vB: prędkość obiektu uciekającego
    :return: animacja
    """

    fig, ax = plt.subplots()
    xdataA, ydataA, xdataA2, ydataA2 = [], [], [0], [0]
    xdataB, ydataB, xdataB2, ydataB2 = [], [], [0], [0]
    lnA, = plt.plot([], [], 'b', animated=True)
    lnA2, = plt.plot([], [], 'b', marker='o', animated=True)
    lnB, = plt.plot([], [], 'r', animated=True)
    lnB2, = plt.plot([], [], 'r', marker='o', animated = True)

    MAX_TIME = 300
    NUMBER_OF_TIMES = 600
    TICK = 0.012

    times = np.linspace(0, MAX_TIME, NUMBER_OF_TIMES)

    xsB, ysB = get_dataB_infinity_symbol(times, a, vB, TICK)
    xsA, ysA = get_dataA(times, 0, 0, vA, xsB, ysB, TICK)

    counter = 0
    for i in range(NUMBER_OF_TIMES):
        counter+=1
        if abs(xsA[i] - xsB[i]) < 0.01 and abs(ysA[i] - ysB[i]) < 0.01:
            break

    times = np.linspace(0, MAX_TIME*counter/NUMBER_OF_TIMES, counter)
    xsB, ysB = xsB[0:counter], ysB[0:counter]
    xsA, ysA = xsA[0:counter], ysA[0:counter]

    def init():
        ax.set_xlim(-3, 3)
        ax.set_ylim(-3, 3)
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_title("Krzywa pogoni po lemniskacie Bernoulliego")
        ax.set_aspect(aspect='equal')



        lnB.set_data(xdataB, ydataB)
        lnB2.set_data(xdataB2, ydataB2)
        lnA.set_data(xdataA, ydataA)
        lnA2.set_data(xdataA2, ydataA2)

        return lnB, lnB2, lnA, lnA2

    def update(frame):
        i = 0
        while times[i] != frame:
            i += 1



        xdataB.append(xsB[i])
        ydataB.append(ysB[i])
        xdataB2[0] = xsB[i]
        ydataB2[0] = ysB[i]
        xdataA.append(xsA[i])
        ydataA.append(ysA[i])
        xdataA2[0] = xsA[i]
        ydataA2[0] = ysA[i]


        lnB.set_data(xdataB, ydataB)
        lnB2.set_data(xdataB2, ydataB2)
        lnA.set_data(xdataA, ydataA)
        lnA2.set_data(xdataA2, ydataA2)


        return lnB, lnB2, lnA, lnA2,

    ani = FuncAnimation(fig, update, frames=times,
                        init_func=init, blit=True, interval=2, repeat=False)
    #
    # writer = PillowWriter(fps=40)
    # ani.save("infinity_symbol_pursuit.gif", writer=writer)

    plt.show()


# SINUSOIDA

def get_dataB_sine(times, A, vB, tick):
    """
    Funkcja obliczająca współrzędne (x, y) obiektu uciekającego po sinusoidzie.

    :param times: lista czasów
    :param A: amplituda
    :param vB: prędkość obiektu
    :param tick: krok czasowy
    :return: xs, ys
    """
    xs, ys = [], []
    for time in times:
        if time == 0:
            xs.append(0)
            ys.append(0)
        else:
            x0 = xs[-1]
            y0 = ys[-1]

            x, y = x0, y0

            i = 0
            while (x-x0)**2 + (y-y0)**2 <= (vB*tick)**2:
                x += 0.01
                i+=1
                y = A*np.sin(x)

            xs.append(x)
            ys.append(y)

    return xs, ys


def sine_pursuit(x0, A, vA, vB):
    """
    Funkcja tworząca animację pościgu po sinusoidzie.

    :param x0: odległość początowa między obiektami
    :param A: amplituda
    :param vA: prędkość obiektu goniącego
    :param vB: prędkość obiektu uciekającego
    :return: animacja
    """

    fig, ax = plt.subplots()
    xdataA, ydataA, xdataA2, ydataA2 = [], [], [0], [0]
    xdataB, ydataB, xdataB2, ydataB2 = [], [], [0], [0]
    lnA, = plt.plot([], [], 'b', animated=True)
    lnA2, = plt.plot([], [], 'b', marker='o', animated=True)
    lnB, = plt.plot([], [], 'r', animated=True)
    lnB2, = plt.plot([], [], 'r', marker='o', animated = True)

    MAX_TIME = 700
    NUMBER_OF_TIMES = 400
    TICK = 0.08 # czas trwania jednej klatki

    times = np.linspace(0, MAX_TIME, NUMBER_OF_TIMES)

    xsB, ysB = get_dataB_sine(times, A, vB, TICK)
    xsA, ysA = get_dataA(times, -x0, 0, vA, xsB, ysB, TICK)

    counter = 0
    for i in range(NUMBER_OF_TIMES):
        counter+=1
        if abs(xsA[i] - xsB[i]) < 0.01 and abs(ysA[i] - ysB[i]) < 0.01:
            break

    times = np.linspace(0, MAX_TIME*counter/NUMBER_OF_TIMES, counter)
    xsB, ysB = xsB[0:counter], ysB[0:counter]
    xsA, ysA = xsA[0:counter], ysA[0:counter]

    def init():
        ax.set_xlim(-1 -x0, 41)
        ax.set_ylim(-A - 1, A + 1)
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_title("Krzywa pogoni po sinusoidzie")
        ax.set_aspect(aspect='equal')



        lnB.set_data(xdataB, ydataB)
        lnB2.set_data(xdataB2, ydataB2)

        lnA.set_data(xdataA, ydataA)
        lnA2.set_data(xdataA2, ydataA2)

        return lnB, lnB2, lnA, lnA2

    def update(frame):
        i = 0
        while times[i] != frame:
            i += 1

        xdataB.append(xsB[i])
        ydataB.append(ysB[i])
        xdataB2[0] = xsB[i]
        ydataB2[0] = ysB[i]

        xdataA.append(xsA[i])
        ydataA.append(ysA[i])
        xdataA2[0] = xsA[i]
        ydataA2[0] = ysA[i]


        lnB.set_data(xdataB, ydataB)
        lnB2.set_data(xdataB2, ydataB2)


        lnA.set_data(xdataA, ydataA)
        lnA2.set_data(xdataA2, ydataA2)

        return lnB, lnB2, lnA, lnA2,

    ani = FuncAnimation(fig, update, frames=times,
                        init_func=init, blit=True, interval=1, repeat=False)

    # writer = PillowWriter(fps=40)
    # ani.save("sine_pursuit.gif", writer=writer)

    plt.show()


if __name__ == "__main__":
    # classic_pursuit(6, 2, 1)
    # circle_pursuit_inside(5, 6, 20)
    # circle_pursuit(10, 5, 12, 20)
    # hypocycloid_pursuit(3, 1, 3, 10)
    # elongated_hypocycloid_pursuit(5, 3, 5, 6, 10)
    # cycloid_pursuit(5, 8, 10)
    # lissajous_curve_pursuit(3, 3, 3, 2, np.pi/2, 3, 10)
    #  infinity_symbol_pursuit(2, 6, 10)
    # sine_pursuit(3, 5, 2, 4)