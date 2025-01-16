import math


def create_Body(n):
    coord_x = []  # массив из координат точек
    coord_y = []  # массив из координат точек
    x_c = 1  # положение центра кольца
    y_c = 1
    for r in range(3):
        for i in range(n):
            alpha = 2 * math.pi * i / n #угол
            x1 = x_c + (1 + r * 0.5) * math.cos(alpha)
            y1 = y_c + (1 + r * 0.5) * math.sin(alpha)

            coord_x.append(x1)
            coord_y.append(y1)
    return coord_x, coord_y

""" проверка работы кода
import matplotlib.pyplot as plt

x, y = create_Body(24)
plt.plot(x, y,'o')
plt.show()"""
