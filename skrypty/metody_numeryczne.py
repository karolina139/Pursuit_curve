import numpy as np
import matplotlib.pyplot as plt


def numerical_methods(y_prim, h, x0, vA, vB, y_func):
    '''
    Funkcja rozwiązująca równanie różniczkowe metodą Eulera.
    :param y_prim: string dy/dx =  f(x, y)
    :param h: krok całkowania
    :param x0: położenie początkowe statku
    :param vA: prędkość okrętu
    :param vB: prędkość statku
    :param y_func: string f(x) - funckcja wyznaczona analitycznie

    :return: wykres
    '''
    X = np.arange(0, x0, h)
    Y = [0]
    Y_e = [0]
    Y_a = [0]
    Y_m = [0]

    for i in range(len(X) - 1):
        # metoda Eulera
        x = X[i]
        y_prim_n = eval(y_prim)

        y_e = Y_e[i] + h * y_prim_n

        Y_e.append(y_e)

        # metoda Adamsa-Bashfortha
        if i == 0:
            x = X[i]
            y_prim_n = eval(y_prim)

            y_a = Y_a[i] + h * y_prim_n
            Y_a.append(y_a)
        else:
            x = X[i - 1]
            y_prim_back = eval(y_prim)
            x = X[i]
            y_prim_n = eval(y_prim)

            y_a = Y_a[i] + 0.5 * h * (3 * y_prim_n - y_prim_back)
            Y_a.append(y_a)

        # metoda Adamsa-Moultona
        x = X[i+1]
        y_prim_forward = eval(y_prim)
        x = X[i]
        y_prim_n = eval(y_prim)

        y_m = Y_m[i] + h * 0.5 * (y_prim_forward + y_prim_n)
        Y_m.append(y_m)


        # funkcja wyznaczona analitycznie
        Y.append(eval(y_func))


    #plt.figure()
    plt.title("Klasyczna krzywa pościgowa dla x0 = %s i prędkości vA = %s, vB =  %s"%(str(x0), str(vA), str(vB)), fontsize = 20)
    plt.plot(X, Y_e, 'b', label = "metoda Eulera")
    plt.plot(X, Y_a, 'g', label = 'metoda Adamsa-Bashfortha')
    plt.plot(X, Y_m, 'c', label='metoda Adamsa-Moultona')
    plt.plot(X, Y, 'r--', label = "rozwiązanie analityczne")
    plt.legend()
    plt.show()









