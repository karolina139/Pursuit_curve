import numpy as np
import matplotlib.pyplot as plt


def numerycznie(curve, x_prim, y_prim, h, t_end, x_0, y_0, n):
    """
    Wylicza numerycznie układ równań różniczkowych pierwszego stopnia.
    :param curve: nazwa krzywej po której porusza się obiekt uciekający
    :param x_prim:  string dx/dt = f(x, y ,t)
    :param y_prim: string dy/dt = f(x, y ,t)
    :param h: krok całkowania
    :param t_end: koniec czasu, początek jest liczony od zera
    :param x_0: warunek początkowy równania dx/dt
    :param y_0: warunek początkowy równania dy/dt
    :param n: stosunek prędkości
    :return: wykres
    """

    z = np.arange(0, t_end, h)

    X = [x_0]
    Y = [y_0]
    X_e = [x_0]
    Y_e = [y_0]
    X_m = [x_0]
    Y_m = [y_0]

    for i in range(len(z) - 1):
        # metoda Adams-Bashfortha
        y = Y[i - 1]
        x = X[i - 1]
        t = z[i - 1]
        y_prim_back = eval(y_prim)
        x_prim_back = eval(x_prim)
        y = Y[i]
        x = X[i]
        t = z[i]
        y_prim_n = eval(y_prim)
        x_prim_n = eval(x_prim)

        y = Y[i] + 0.5 * h * (3 * y_prim_n - y_prim_back)
        x = X[i] + 0.5 * h * (3 * x_prim_n - x_prim_back)
        Y.append(y)
        X.append(x)

        # metoda ekstrapolacyjna eulera
        y = Y_e[i]
        x = X_e[i]
        t = z[i]
        y_prim_n = eval(y_prim)
        x_prim_n = eval(x_prim)

        y_e = Y_e[i] + h * y_prim_n
        x_e = X_e[i] + h * x_prim_n

        Y_e.append(y_e)
        X_e.append(x_e)

    plt.title(
        "Pościg dla n=%s i startowej pozycji (%s, %s) obiektu ścigającego." % (str(n), str(x_0), str(y_0)),
        fontsize=10)
    plt.plot(X, Y, "b", label="metoda Adams-Bashfortha")
    plt.plot(X_e, Y_e, "g", label="metoda Euler")

    if curve == "kolo":
        plt.plot(5 * np.cos(z), 5 * np.sin(z), "r", label="trajektoria obiektu ściganego")
    if curve == "hipocykloida":
        plt.plot(2 * np.cos(z) + np.cos(2 * z), 2 * np.sin(z) - np.sin(2 * z), "r",
                 label="trajektoria obiektu ścigającego")
        plt.axes().set_aspect('equal', 'datalim')
    if curve == "hipotrochoida":
        plt.plot(2 * np.cos(z) + 5 * np.cos((2 / 3) * z), 2 * np.sin(z) - 5 * np.sin((2 / 3) * z), "r",
                 label="trajektoria obiektu ściganego")
        plt.axes().set_aspect('equal', 'datalim')
    if curve == "cykloida":
        plt.plot(5 * (z - np.sin(z)), 5 * (1 - np.cos(z)), "r", label="trajektoria obiektu ściganego")
        plt.axes().set_aspect('equal', 'datalim')
    if curve == "lissajous":
        plt.plot(3 * (np.sin(3*z + np.pi /2)), 3 * (np.sin(2*z)), "r", label="trajektoria obiektu ściganego")
    if curve == "sinusoida":
        plt.plot(z, 5*np.sin(z), "r", label="trajektoria obiektu ściganego")
    if curve == "lemniskata":
        plt.axes().set_aspect('equal', 'datalim')
        plt.plot(2*np.sqrt(2)*np.cos(z)/(1 + (np.sin(z))**2), 2*np.sqrt(2)*np.cos(z)*np.sin(z)/(1 + (np.sin(z))**2), "r", label="trajektoria obiektu ściganego")

    plt.scatter(x_0, y_0, color="green")
    plt.legend()

    return plt.show()



