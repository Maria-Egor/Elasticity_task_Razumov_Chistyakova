import math
import models
from RungeKutta import runge_kutta

def create_Body(n):
    coord_x = []  # массив из координат точек
    coord_y = []  # массив из координат точек
    x_c = 3  # положение центра кольца
    y_c = 3
    for r in range(2):
        for i in range(n):
            alpha = 2 * math.pi * i / n #угол
            x1 = x_c + (r + 1) * math.cos(alpha)
            y1 = y_c + (r + 1) * math.sin(alpha)

            coord_x.append(x1)
            coord_y.append(y1)
    return coord_x, coord_y


def move(t0, t, n, x0, y0):
    h = t / n
    tr = models.Trajectory()
    prx = x0
    pry = y0
    for i in range(n):
        x, y = runge_kutta(t0 + h * i, h, prx, pry)
        tr.add(x, y)
        prx = x
        pry = y
    return tr
